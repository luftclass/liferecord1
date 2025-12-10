import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# -------------------------------
# ① 구글 시트 API 인증 설정
# -------------------------------
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Streamlit Secrets에 저장된 인증정보 불러오기
creds = Credentials.from_service_account_info(
    st.secrets["google"], scopes=scope
)

client = gspread.authorize(creds)

# 사용할 구글시트 이름 (시트 제목과 정확히 일치해야 함)
sheet = client.open("2025_구산고_1학년_행발").sheet1

# -------------------------------
# ② 앱 UI 구성
# -------------------------------
st.title("2025 구산고 1학년 학생 정보 입력")
st.write("담당교사: 구산고 행발 프로젝트용 입력 시스템")

# 입력 폼
class_num = st.selectbox("반을 선택하세요", list(range(1, 9)))
student_num = st.selectbox("번호를 선택하세요", list(range(1, 31)))
name = st.text_input("이름을 입력하세요")

# -------------------------------
# ③ 데이터 제출
# -------------------------------
if st.button("제출"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요.")
    else:
        # Google Sheets에 데이터 추가
        sheet.append_row([class_num, student_num, name])
        st.success(f"{class_num}반 {student_num}번 {name} 학생의 정보가 저장되었습니다.")
        st.balloons()
