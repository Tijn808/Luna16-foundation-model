
import pandas as pd

# load
labels = pd.read_csv("labels.csv")
patches = pd.read_csv("patch.csv").sort_values("patch_index").reset_index(drop=True)

# make sure label nodules are in a stable order per seriesuid
# (if your CSV already has nodule_0, nodule_1, ... this is safe)
labels["nodule_num"] = labels["nodule_id"].str.extract(r"(\d+)").astype(int)
labels = labels.sort_values(["seriesuid", "nodule_num"]).reset_index(drop=True)

# assign nodule_num to each patch based on sequence within each seriesuid
patches["nodule_num"] = patches.groupby("seriesuid").cumcount()

# merge on (seriesuid, nodule_num)
merged = patches.merge(
    labels,
    on=["seriesuid", "nodule_num"],
    how="left",
    suffixes=("_patch", "_label")
)

print("Total patches:", len(merged))
print("Missing labels:", merged["mal_mean"].isna().sum())

# keep only what you want
final = merged[[
    "patch_index",
    "seriesuid",
    "nodule_num",
    "patch_filename",
    "mal_mean",
    "all_scores",
    "calcification",
    "internalStructure",
    "lobulation",
    "margin",
    "sphericity",
    "spiculation",
    "subtlety",
    "texture",
]]

final.to_csv("name.csv", index=False)
print("name.csv")

# show first few patches per scan
print(final.groupby("seriesuid").head(3)[
    ["patch_index","seriesuid","nodule_num","mal_mean","patch_filename"]
])
