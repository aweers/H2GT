import pandas as pd
import os
from glob import glob

OUT_FOLDER = "/mnt/Drive2/aweers/tcga-brca-20/out-folder/*.pkl"
ALL_LABELS = "./all_labels.csv"


def get_set_files(path: str):
    files = glob(path)
    case_ids = [f.split("/")[-1][:12] for f in files]
    files = list(zip(files, case_ids))
    split_60, split_80 = int(len(files) * 0.6), int(len(files) * 0.8)

    return files[:split_60], files[split_60:split_80], files[split_80:]


def copy_labels(files: list, save_path: str):
    df = pd.read_csv(ALL_LABELS)
    filtered = df[df["case_id"].isin([f[1] for f in files])]
    for filename, case_id in files:  # TODO horrible solution
        filtered.loc[filtered["case_id"] == case_id, "graph_path"] = filename
    # print(filtered)
    filtered.to_csv(save_path, index=False, header=True)


train, val, test = get_set_files(OUT_FOLDER)
copy_labels(train, "train.csv")
copy_labels(val, "val.csv")
copy_labels(test, "test.csv")
