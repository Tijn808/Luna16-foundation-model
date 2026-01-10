# Luna16-foundation-model

1. Main branch is protected
	•	main is stable only
	•	No direct commits to main
	•	main must always run end-to-end

All work happens on feature branches.


2. One feature per branch
Branch naming:
feature/<short-description>
Examples:
	•	feature/dataset-sanity
	•	feature/patch-extraction
	•	feature/embedding-extraction
	•	feature/finetuning

Do not mix unrelated changes in one branch.

3. Pull requests are mandatory
	•	Every branch is merged via a Pull Request
	•	At least one other person reviews
	•	Reviewer checks:
	•	code runs
	•	no data paths hardcoded
	•	no data files committed

No self-merging.

4. No data or model artifacts in Git
Never commit:
	•	CT scans (.mhd, .raw)
	•	CSVs with coordinates
	•	extracted patches
	•	embeddings
	•	trained models

If it contains patient-derived pixels → it does not go in Git.

5. Notebooks must be runnable
Rules for notebooks:
	•	Must run top to bottom
	•	No hidden state
	•	Clear section headings
	•	Heavy logic moved to src/

6. src/ is reusable code only
	•	No experiments
	•	No plotting for exploration
	•	Functions and classes only
	•	Document inputs and outputs

7. Commit discipline
Each commit:
	•	Does one logical thing
	•	Has a clear message describing what changed
Good:
	•	Add patient-level cross-validation split
	•	Implement HU normalization for CT volumes
Bad:
	•	wip
	•	fix
	•	final

8. If in doubt: ask before pushing

If you are unsure whether something should be committed:
	•	Ask in chat
	•	Or open a draft PR

Better to slow down than corrupt the repo.
