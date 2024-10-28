import pandas as pd


all_labels = pd.read_csv("all_labels.csv")
gdc_unique = pd.read_csv("gdc_unique.txt", delimiter="\t")

gdc_unique["case_id"] = gdc_unique["filename"].str[:12]

print(gdc_unique.head())

print(len(gdc_unique))
filtered = gdc_unique[gdc_unique["case_id"].isin(all_labels["case_id"])]

print(len(filtered))

filtered.drop("case_id", axis=1).to_csv("gdc_filtered.txt", index=False, sep="\t")
