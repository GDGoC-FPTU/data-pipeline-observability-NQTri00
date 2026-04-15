# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-2A202600249  
**Name:** Ninh Quang Tri  
**Date:** 15/04/2026

---

## 1. Ket qua thi nghiem

Chạy `agent_simulation.py` với 2 bộ dữ liệu và ghi lại kết quả:

| Scenario                          | Agent Response                                                   | Accuracy (1-10) | Notes                                             |
| --------------------------------- | ---------------------------------------------------------------- | --------------- | ------------------------------------------------- |
| Clean Data (`processed_data.csv`) | Based on my data, the best choice is Laptop at $1200.            | 9               | Logical, reasonable price, correct recommendation |
| Garbage Data (`garbage_data.csv`) | Based on my data, the best choice is Nuclear Reactor at $999999. | 1               | Completely unrealistic recommendation             |

---

## 2. Phan tich & nhan xet

Khi sử dụng **Clean Data**, AI Agent đưa ra câu trả lời hợp lý, logic và phù hợp với ngữ cảnh (khuyến nghị Laptop với giá $1200). Ngược lại, khi dùng **Garbage Data**, Agent đưa ra kết quả vô lý (Nuclear Reactor giá gần 1 triệu USD).

Lý do chính là chất lượng dữ liệu ảnh hưởng rất lớn đến hiệu suất của AI Agent. Trong Garbage Data tồn tại nhiều vấn đề nghiêm trọng:

- **Outliers cực lớn**: Các record có giá trị price lên đến hàng trăm nghìn hoặc gần 1 triệu USD (ví dụ: Nuclear Reactor) làm lệch kết quả phân tích.
- **Wrong data types / Invalid values**: Một số trường price không phải số, hoặc bị lẫn dữ liệu text, khiến Agent không thể tính toán đúng.
- **Null / Missing values**: Nhiều record thiếu thông tin quan trọng (category, name, price), dẫn đến Agent không có đủ dữ liệu để đưa ra quyết định chính xác.
- **Duplicate IDs**: Dữ liệu trùng lặp làm Agent bị nhầm lẫn về số lượng và phân bố sản phẩm.
- **Irrelevant or toxic data**: Sự xuất hiện của các mặt hàng không liên quan (Nuclear Reactor, Weapon, v.v.) làm ô nhiễm toàn bộ dataset.

Những vấn đề này khiến AI Agent không thể hiểu đúng ngữ cảnh và đưa ra khuyến nghị sai lệch. Điều này chứng minh rằng nếu dữ liệu đầu vào kém chất lượng thì output của Agent cũng sẽ kém theo.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** → **Đồng ý**

Chất lượng dữ liệu quan trọng hơn rất nhiều so với chất lượng prompt. Một prompt hoàn hảo nhưng được cung cấp dữ liệu rác (garbage in) sẽ dẫn đến kết quả rác (garbage out). Ngược lại, khi dữ liệu sạch, được validate và transform tốt, ngay cả với prompt đơn giản, AI Agent vẫn có thể đưa ra câu trả lời chính xác và đáng tin cậy.

Bài học rút ra từ thí nghiệm này:  
**Data Observability và Data Cleaning** là bước quan trọng nhất trong bất kỳ AI/ML pipeline nào. Trước khi tối ưu prompt hay model, chúng ta phải đảm bảo dữ liệu đầu vào phải sạch và đáng tin cậy.

---

**Submitted by:** Ninh Quang Tri  
**Date:** 15/04/2026