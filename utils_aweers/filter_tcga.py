import pandas as pd

filename = "gdc_tcga_brca_filtered.txt"
out_path = "gdc_unique.txt"

df = pd.read_csv(filename, sep="\t")

print(df.columns)
print(len(df))


def filter(df, l):
    df["patient_id"] = df["filename"].str[:l]
    df = df.sort_values(by=["filename"])
    df = df.drop_duplicates(subset="patient_id", keep="first")
    df = df.drop(["patient_id"], axis=1)
    return df


df = filter(df, 12)
df.to_csv(out_path, sep="\t", header=True, index=False)

df["slide_id"] = df["filename"].str[:23]
df["slide_id"].to_csv("slide_ids.txt", header=False, index=False)
