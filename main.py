import streamlit as st
import sys
from streamlit.web import cli as stcli

def main():
    st.title("Chạy Streamlit bằng lệnh Python")
    st.write("Xin chào! App này được khởi chạy từ hàm main.")
    
    # Thêm các thành phần giao diện của bạn ở đây
    user_input = st.text_input("Nhập tên của bạn:")
    if user_input:
        st.write(f"Chào {user_input}!")

if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())