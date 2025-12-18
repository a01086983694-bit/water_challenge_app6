import streamlit as st
from datetime import datetime
import os

# --------------------
# 기본 설정
# --------------------
st.set_page_config(
    page_title="물 한 컵 챌린지",
    page_icon="💧",
    layout="centered"
)

BASE_DIR = os.path.dirname(__file__)

st.title("💧 물 한 컵 챌린지")
st.write("작은 실천으로 환경을 지켜요!")

# --------------------
# 날짜 표시
# --------------------
today = datetime.now().strftime("%Y년 %m월 %d일")
st.caption(f"📅 오늘 날짜: {today}")

st.divider()

# --------------------
# 체크 항목
# --------------------
st.subheader("✅ 오늘의 물 절약 실천")

check_cup = st.checkbox("양치할 때 컵 사용하기")
check_shower = st.checkbox("샤워 시간 줄이기")
check_tap = st.checkbox("사용하지 않을 때 수도 잠그기")

checked_count = sum([check_cup, check_shower, check_tap])

st.divider()

# --------------------
# 실천 완료 버튼
# --------------------
if st.button("실천 완료 👏"):

    if checked_count == 0:
        st.warning("아직 실천한 항목이 없어요! 하나만 체크해도 좋아요 🙂")
        st.image(
            os.path.join(BASE_DIR, "start.png"),
            width=200
        )

    elif checked_count == 1:
        st.success("좋은 시작이에요! 👏")
        st.image(
            os.path.join(BASE_DIR, "clap_small.png"),
            width=200
        )

    elif checked_count == 2:
        st.success("대단해요! 두 가지나 실천했어요 👏👏")
        st.image(
            os.path.join(BASE_DIR, "clap_medium.png"),
            width=220
        )

    elif checked_count == 3:
        st.balloons()
        st.success("완벽해요! 오늘의 물 절약 챔피언 🏆")
        st.image(
            os.path.join(BASE_DIR, "clap_big.png"),
            width=250
        )

    # --------------------
    # 실천 목록 출력
    # --------------------
    if checked_count > 0:
        st.write("### 🌱 오늘 실천한 내용")
        if check_cup:
            st.write("✔️ 양치할 때 컵 사용하기")
        if check_shower:
            st.write("✔️ 샤워 시간 줄이기")
        if check_tap:
            st.write("✔️ 사용하지 않을 때 수도 잠그기")
