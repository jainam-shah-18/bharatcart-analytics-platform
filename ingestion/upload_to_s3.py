from pathlib import Path
import os

import boto3
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
BUCKET = os.getenv("S3_BUCKET_NAME")
REGION = os.getenv("AWS_DEFAULT_REGION")

required_variables = [
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_DEFAULT_REGION",
    "S3_BUCKET_NAME",
]

missing = [name for name in required_variables if not os.getenv(name)]

if missing:
    raise ValueError(f"Missing environment variables: {missing}")

s3 = boto3.client("s3", region_name=REGION)
s3.head_bucket(Bucket=BUCKET)

csv_files = sorted(DATA_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {DATA_DIR}")

for file_path in csv_files:
    object_key = f"raw/{file_path.name}"

    print(f"Uploading {file_path.name}...")
    s3.upload_file(str(file_path), BUCKET, object_key)
    print(f"Uploaded: s3://{BUCKET}/{object_key}")

print(f"\nSuccessfully uploaded {len(csv_files)} files.")
