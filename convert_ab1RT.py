import pandas as pd
from Bio import SeqIO

def convert_ab1_to_qscore_csv(ab1_file_path):
    record = SeqIO.read(ab1_file_path, "abi")
    sequence = str(record.seq.reverse_complement())
    q_scores = record.letter_annotations.get("phred_quality", [])[::-1]

    df = pd.DataFrame({
        "Position": range(1, len(sequence) + 1),
        "Base": list(sequence),
        "Q_Score": q_scores
    })

    csv_name = ab1_file_path.replace(".ab1", "RT_qscore.csv")
    df.to_csv(csv_name, index=False)
    print(f"已成功匯出：{csv_name}")
#改下面檔案名稱就能用
if __name__ == "__main__":
    convert_ab1_to_qscore_csv("068_D09_K_mIGK.ab1")