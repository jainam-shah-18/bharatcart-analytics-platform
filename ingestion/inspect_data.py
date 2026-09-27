from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

csv_files = sorted(DATA_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {DATA_DIR}")

print(f"\nFound {len(csv_files)} CSV files\n")

for file_path in csv_files:
    df = pd.read_csv(file_path)

    print("=" * 70)
    print(f"FILE: {file_path.name}")
    print(f"ROWS: {len(df):,}")
    print(f"COLUMNS: {len(df.columns)}")
    print(f"DUPLICATE ROWS: {df.duplicated().sum():,}")

    print("\nCOLUMN NAMES:")
    for column in df.columns:
        missing = df[column].isna().sum()
        print(f"  - {column}: {missing:,} missing")

    print()