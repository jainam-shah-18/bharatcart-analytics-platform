from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

required_files = {
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
}

existing_files = {file.name for file in DATA_DIR.glob("*.csv")}
missing_files = required_files - existing_files

assert not missing_files, f"Missing files: {missing_files}"

primary_keys = {
    "olist_customers_dataset.csv": "customer_id",
    "olist_orders_dataset.csv": "order_id",
    "olist_products_dataset.csv": "product_id",
    "olist_sellers_dataset.csv": "seller_id",
}

for filename, primary_key in primary_keys.items():
    df = pd.read_csv(DATA_DIR / filename)

    assert primary_key in df.columns, (
        f"{filename}: column {primary_key} is missing"
    )
    assert df[primary_key].notna().all(), (
        f"{filename}: {primary_key} contains null values"
    )
    assert df[primary_key].is_unique, (
        f"{filename}: {primary_key} contains duplicates"
    )

    print(f"PASSED: {filename} → {primary_key}")

print("\nAll raw-data validation checks passed.")