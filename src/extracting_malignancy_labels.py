
#Imports + NumPy fix for pylidc

import numpy as np
if not hasattr(np, "int"):
    np.int = int
if not hasattr(np, "bool"):
    np.bool = bool

import pandas as pd
import pylidc as pl
from pylidc.utils import consensus
from tqdm import tqdm


# Load LUNA16 list of scans (seriesuids)

luna = pd.read_csv("https://zenodo.org/record/3723295/files/annotations.csv")
luna_seriesuids = set(luna["seriesuid"].astype(str).values)
print("Unique LUNA seriesuids:", len(luna_seriesuids))

# Helper functions

attribute_keys = [
    "calcification",
    "internalStructure",
    "lobulation",
    "malignancy",
    "margin",
    "sphericity",
    "spiculation",
    "subtlety",
    "texture",
]

def consensus_attr(values):
    return int(np.rint(np.mean(values)))

def consensus_bbox_and_centroid(anns):
    _, cbbox, _ = consensus(anns, clevel=0.5, pad=False)
    centroid_zyx = [sl.start + int(0.5 * (sl.stop - sl.start)) for sl in cbbox]
    return cbbox, centroid_zyx


# Get seriesuids that exist in pylidc DB

db_uids = [s.series_instance_uid for s in pl.query(pl.Scan).all()]
seriesuids = sorted(set(db_uids).intersection(luna_seriesuids))

print("Seriesuids present in BOTH pylidc DB and LUNA:", len(seriesuids))


# Iterate scan-by-scan (robust)

rows = []

for seriesuid in tqdm(seriesuids):
    try:
        scan = pl.query(pl.Scan).filter(pl.Scan.series_instance_uid == seriesuid).first()
        if scan is None:
            continue

        clusters = scan.cluster_annotations()
        clusters = [c for c in clusters if len(c) >= 3]

        for nid, cluster in enumerate(clusters):
            cluster_use = [ann for ann in cluster if ann.diameter >= 3]
            if len(cluster_use) < 3:
                continue

            # collect attributes
            attr_lists = {k: [] for k in attribute_keys}
            for ann in cluster_use:
                for k in attribute_keys:
                    attr_lists[k].append(getattr(ann, k))

            # consensus attributes (except malignancy)
            attrs = {k: consensus_attr(v) for k, v in attr_lists.items()}

            # malignancy outputs (ONLY what you want)
            mal_scores = attr_lists["malignancy"]
            mal_mean = float(np.mean(mal_scores))

            cbbox, centroid_zyx = consensus_bbox_and_centroid(cluster_use)

            rows.append({
                "seriesuid": seriesuid,
                "nodule_id": f"nodule_{nid}",
                "centroid_z": centroid_zyx[0],
                "centroid_y": centroid_zyx[1],
                "centroid_x": centroid_zyx[2],
                "bbox": str(cbbox),

                "mal_mean": mal_mean,
                "all_scores": str(mal_scores),
                "source": "LIDC-IDRI",

                "calcification": attrs["calcification"],
                "internalStructure": attrs["internalStructure"],
                "lobulation": attrs["lobulation"],
                "margin": attrs["margin"],
                "sphericity": attrs["sphericity"],
                "spiculation": attrs["spiculation"],
                "subtlety": attrs["subtlety"],
                "texture": attrs["texture"],
            })

    except Exception as e:
        print(f"[SKIP] {seriesuid}: {e}")
        continue


# Save output

df = pd.DataFrame(rows)
print("Output shape:", df.shape)
print(df.head())

out_path =
df.to_csv(out_path, index=False)
print("Saved:", out_path)

# After creating the DataFrame
df = pd.DataFrame(rows)

# Delete the 'source' column if it exists
if 'source' in df.columns:
    del df['source']  # Simpler way to delete a column

# Save to CSV
df.to_csv("name.csv", index=False)
print(df.head())
