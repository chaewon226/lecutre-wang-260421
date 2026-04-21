import streamlit as st

st.title("자기 소개 페이지")

st.header("안녕하세요!")

st.write("""
저는 [황채원]입니다. 

디지털을 활용한 수학 교육에 관심이 있는 수학교육 전공자입니다.
""")

st.subheader("석사")
st.write("- [고려대학교 교육대학원], [수학교육전공], 2026")

st.subheader("")
st.write("- [개념원리], [온라인사업부 콘텐츠기획팀], 23.07 ~ 24.09")

st.subheader("관심사")
st.write("- 수학 교육")
st.write("- 데이터 분석")
st.write("- 달리기")

st.subheader("연락처")
st.write("- 이메일: [color_h1@korea.ac.kr]")
st.write("- GitHub: [github.com/chaewonhwang226]")

# 선택적으로 이미지 추가 (파일이 있으면)
# st.image("profile.jpg", caption="프로필 사진", width=200)
