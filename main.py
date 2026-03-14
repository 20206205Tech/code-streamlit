import streamlit as st
import pandas as pd

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit đầu tiên của tôi")

# Viết văn bản
st.write("Đây là một ví dụ đơn giản về cách sử dụng Streamlit.")

# Tạo một DataFrame mẫu
df = pd.DataFrame({
    'Tên': ['An', 'Bình', 'Chi'],
    'Điểm': [85, 90, 88]
})

# Hiển thị bảng dữ liệu
st.header("Dữ liệu học sinh")
st.dataframe(df)

# Tạo biểu đồ đơn giản
st.header("Biểu đồ điểm")
st.bar_chart(df.set_index('Tên'))