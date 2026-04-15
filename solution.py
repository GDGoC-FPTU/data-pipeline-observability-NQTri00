"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-2A202600249  (<-- Thay XXXX bang ma so cua ban)
Name: Ninh Quang Tri

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import datetime
import os

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Đọc dữ liệu JSON từ file.
    """
    print(f"Extracting data from {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Successfully extracted {len(data)} records.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return []
    except Exception as e:
        print(f"Unexpected error during extraction: {e}")
        return []


def validate(data):
    """
    Task 2: Kiểm tra chất lượng dữ liệu.
    Quy tắc:
      - price > 0
      - category không được rỗng
    """
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get('price')
        category = record.get('category', '')

        # Check price > 0
        if not isinstance(price, (int, float)) or price <= 0:
            error_count += 1
            continue

        # Check category not empty
        if not isinstance(category, str) or category.strip() == '':
            error_count += 1
            continue

        valid_records.append(record)

    print(f"Validation summary: {len(valid_records)} valid, {error_count} errors")
    return valid_records


def transform(data):
    """
    Task 3: Transform dữ liệu
      - Tính discounted_price = price * 0.9
      - Category → Title Case
      - Thêm cột processed_at
    """
    if not data:
        print("No valid data to transform.")
        return None

    df = pd.DataFrame(data)

    # Calculate 10% discount
    df['discounted_price'] = df['price'] * 0.9

    # Normalize category to Title Case
    df['category'] = df['category'].str.title()

    # Add timestamp
    df['processed_at'] = datetime.datetime.now().isoformat()

    print(f"Transform completed: {len(df)} records processed.")
    return df


def load(df, output_path):
    """
    Task 4: Lưu DataFrame ra file CSV
    """
    try:
        df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"Data successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("ETL Pipeline Started - Day 10 Lab")
    print("=" * 60)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None and not final_df.empty:
            load(final_df, OUTPUT_FILE)
            print(f"\n🎉 Pipeline completed successfully!")
            print(f"   Total records saved: {len(final_df)}")
        else:
            print("\n⚠️  No data to save after transformation.")
    else:
        print("\n❌ Pipeline aborted: No data extracted.")

    print("=" * 60)