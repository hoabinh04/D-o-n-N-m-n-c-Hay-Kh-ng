# 🍄 Ứng dụng phân loại nấm ăn được hay không

## 📌 Bài làm về gì
Đây là ứng dụng web đơn giản giúp dự đoán nấm có ăn được hay độc dựa trên một số đặc điểm cơ bản như:
- Mùi (odor)
- Màu mũ nấm (cap-color)
- Màu phiến nấm (gill-color)

Ứng dụng gồm 2 phần:
- **Backend (Flask API)**: xử lý dự đoán bằng mô hình cây quyết định đã huấn luyện.  
- **Frontend (React + TailwindCSS)**: giao diện trực quan cho phép người dùng chọn đặc điểm và nhận kết quả dự đoán.

---

## 🛠️ Công nghệ sử dụng
- Python + Flask  
- Flask-CORS  
- Pickle (load mô hình)  
- ReactJS + Babel  
- TailwindCSS  
- Axios  

---

## 🖼️ Một số giao diện cơ bản
Ví dụ giao diện khi chọn thông tin và nhận kết quả dự đoán:

<img width="1862" height="913" alt="image" src="https://github.com/user-attachments/assets/c034600f-37e5-475c-bf92-293d2e87392e" />
<img width="1861" height="911" alt="image" src="https://github.com/user-attachments/assets/d5879cf2-6fa3-418f-8207-51090283cb02" />



---

## 🚀 Cách chạy
1. Cài thư viện:
   ```bash
   pip install flask flask-cors
