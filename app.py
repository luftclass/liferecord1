import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# 구글 시트 연결
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("2025_구산고_1학년_행발").sheet1

st.title("2025 구산고 1학년 학생 데이터 입력")

name = st.text_input("이름")
class_num = st.number_input("반", min_value=1, max_value=10, step=1)
student_num = st.number_input("번호", min_value=1, max_value=50, step=1)
activity = st.text_area("희망 활동 / 비고")

if st.button("제출"):
    sheet.append_row([name, class_num, student_num, activity])
    st.success("제출 완료! 감사합니다.")
