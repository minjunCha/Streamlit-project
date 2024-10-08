import streamlit as st
import random
import datetime

# 타이틀 적용
st.title(":sparkles: 로또 생성기 :sparkles:")

def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 45)  # 1부터 45까지의 숫자를 생성
        lotto.add(number)

    return sorted(lotto)  # 정렬된 로또 번호 반환

button = st.button("로또를 생성해 주세요!")
if button:
    for i in range(1,6):
        lotto = generate_lotto()
        st.write(f"{i}. 행운의 번호: {lotto}")  # 결과 출력