
import streamlit as st

# ====== 여기 정보만 바꾸면 됩니다 ======
name = "홍길동"
job = "중학교 기술 교사"
hobbies = ["코딩 가르치기", "새로운 기술 배우기", "등산"]
skills = ["Python", "HTML/CSS", "수업 자료 만들기"]
message = "학생들과 함께 즐겁게 배우는 것을 좋아합니다!"
# ====================================

st.set_page_config(page_title=f"{name}의 소개", page_icon="👋")

st.title(f"안녕하세요! 저는 {name}입니다 👋")
st.subheader(f"직업: {job}")

st.divider()

st.markdown("### 🎯 취미")
for hobby in hobbies:
    st.markdown(f"- {hobby}")

st.divider()

st.markdown("### 🛠️ 잘 다루는 기술")
for skill in skills:
    st.markdown(f"- {skill}")

st.divider()

st.info(message)
