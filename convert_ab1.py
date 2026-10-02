import pandas as pd
from Bio import SeqIO

def convert_ab1_to_qscore_csv(ab1_file_path):
    record = SeqIO.read(ab1_file_path, "abi")
    sequence = str(record.seq)
    q_scores = record.letter_annotations.get("phred_quality", [])

    df = pd.DataFrame({
        "Position": range(1, len(sequence) + 1),
        "Base": list(sequence),
        "Q_Score": q_scores
    })

    csv_name = ab1_file_path.replace(".ab1", "_qscore.csv")
    df.to_csv(csv_name, index=False)
    print(f"已成功匯出：{csv_name}")

if __name__ == "__main__":
    convert_ab1_to_qscore_csv("067_C09_K_ISPCR.ab1")