from datasets import load_dataset
cn_dataset = load_dataset("Helsinki-NLP/opus-100", data_dir="en-zh")


 # For each of the dataset files, save it as parquet.
for name, dataset in cn_dataset.items():
    dataset.to_parquet(f"./data/raw/en-zh-{name}.parquet")