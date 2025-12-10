import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 구글 시트 연결 설정
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("2025_구산고_1학년_행발").sheet1

st.title("2025 구산고 1학년 학생 정보 입력")

# 입력 폼
class_num = st.selectbox("반", list(range(1, 9)))
student_num = st.selectbox("번호", list(range(1, 31)))
name = st.text_input("이름")

# 제출
if st.button("제출"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요.")
    else:
        sheet.append_row([class_num, student_num, name])
        st.success("제출이 완료되었습니다! 감사합니다.")
