[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23572356&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student ID:** AI20K-0249
**Student Email:** [nq.tri2511@gmail.com]
**Name:** Ninh Quang Tri

---

## Mo ta

Tôi đã xây dựng một **ETL Pipeline** hoàn chỉnh (Extract - Transform - Load).  

Pipeline thực hiện các bước sau:
- **Extract**: Đọc dữ liệu từ file `raw_data.json`
- **Validate (Data Observability)**: Kiểm tra chất lượng dữ liệu (price > 0, category không rỗng), loại bỏ record không hợp lệ
- **Transform**: 
  - Tính `discounted_price` = price × 0.9 (giảm 10%)
  - Chuẩn hóa `category` thành Title Case
  - Thêm cột `processed_at` (timestamp)
- **Load**: Lưu kết quả ra file `processed_data.csv`

Ngoài ra, tôi đã thực hiện **Agent Simulation (Stress Test)** để so sánh pipeline khi chạy với **Clean Data** và **Garbage Data** (dữ liệu chứa nhiều lỗi), từ đó quan sát khả năng xử lý và logging của pipeline (Data Observability).

---

## Cach chay (How to Run)

### Prerequisites
```bash
pip install pandas
```

### Chay ETL Pipeline
```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)
```bash
python agent_simulation.py
```
---

## Cau truc thu muc

```
├── solution.py              # ETL Pipeline script
├── processed_data.csv       # Output cua pipeline
├── experiment_report.md     # Bao cao thi nghiem
└── README.md                # File nay
```

---

## Ket qua

Records extracted: 5 <br>
Records dropped during validation: 2 <br>
Records successfully processed: 3 <br>
Final output: processed_data.csv (có thêm cột discounted_price, category ở dạng Title Case, và timestamp) <br>
Records saved: 3
