import streamlit as st
import random

st.set_page_config(page_title="🎵 유튜브 음악 추천기", layout="centered")

st.title("🎶 유튜브 음악 추천기")
st.write("좋아하는 **장르**와 **아티스트**를 선택하고 음악을 추천받아보세요!")

# ------------------ 데이터 ------------------
music_data = {
    "발라드": {
        "IU": [
            {"title": "밤편지", "url": "https://www.youtube.com/watch?v=BzYnNdJhZQw"},
            {"title": "라일락", "url": "https://www.youtube.com/watch?v=v7bnOxV4jAc"},
            {"title": "스물셋", "url": "https://www.youtube.com/watch?v=42Gtm4-Ax2U"},
            {"title": "Blueming", "url": "https://www.youtube.com/watch?v=D1PvIWdJ8xo"},
        ]
    },
    "K-POP": {
        "BTS": [
            {"title": "Dynamite", "url": "https://www.youtube.com/watch?v=gdZLi9oWNZg"},
            {"title": "Spring Day", "url": "https://www.youtube.com/watch?v=xEeFrLSkMm8"},
            {"title": "Butter", "url": "https://www.youtube.com/watch?v=WMweEpGlu_U"},
            {"title": "IDOL", "url": "https://www.youtube.com/watch?v=pBuZEGYXA6E"},
        ],
        "BLACKPINK": [
            {"title": "DDU-DU DDU-DU", "url": "https://www.youtube.com/watch?v=IHNzOHi8sJs"},
            {"title": "Kill This Love", "url": "https://www.youtube.com/watch?v=2S24-y0Ij3Y"},
            {"title": "Pink Venom", "url": "https://www.youtube.com/watch?v=gQlMMD8auMs"},
            {"title": "Shut Down", "url": "https://www.youtube.com/watch?v=POe9SOEKotk"},
        ],
        "aespa": [
            {"title": "Spicy", "url": "https://www.youtube.com/watch?v=Os_heh8vPfs"},
            {"title": "Next Level", "url": "https://www.youtube.com/watch?v=4TWR90KJl84"},
            {"title": "Savage", "url": "https://www.youtube.com/watch?v=WPdWvnAAurg"},
            {"title": "Drama", "url": "https://www.youtube.com/watch?v=YB9I0bdoLlw"},
            {"title": "Welcome To MY World", "url": "https://www.youtube.com/watch?v=bv-tfLaW2GM"},
            {"title": "Whiplash", "url": "https://www.youtube.com/watch?v=C-8VeuByC3I"},
        ],
        "fromis_9": [
            {"title": "DM", "url": "https://www.youtube.com/watch?v=8s9Kqbh1zPI"},
            {"title": "Talk & Talk", "url": "https://www.youtube.com/watch?v=Rn-qwqg1rNk"},
            {"title": "WE GO", "url": "https://www.youtube.com/watch?v=3gwO2t1fGQE"},
            {"title": "Stay This Way", "url": "https://www.youtube.com/watch?v=4fPVKzPJrRo"},
        ],
    },
    "힙합": {
        "G-DRAGON": [
            {"title": "무제(無題)", "url": "https://www.youtube.com/watch?v=8ABTFWydxLg"},
            {"title": "니가 뭔데", "url": "https://www.youtube.com/watch?v=9kaRWU5fF4I"},
            {"title": "삐딱하게", "url": "https://www.youtube.com/watch?v=tdH2w3n9f1Y"},
            {"title": "HEARTBREAKER", "url": "https://www.youtube.com/watch?v=LOXEVd-Z7NE"},
        ],
        "BIGBANG": [
            {"title": "FANTASTIC BABY", "url": "https://www.youtube.com/watch?v=AAbokV76tkU"},
            {"title": "BANG BANG BANG", "url": "https://www.youtube.com/watch?v=2ips2mM7Zqw"},
            {"title": "LAST DANCE", "url": "https://www.youtube.com/watch?v=I2K1LkZfSxg"},
            {"title": "하루하루", "url": "https://www.youtube.com/watch?v=MzCbEdtNbJ0"},
        ]
    },
}

# ------------------ 인터페이스 ------------------
genre = st.selectbox("🎧 장르 선택", list(music_data.keys()))

artist = st.selectbox("🎤 아티스트 선택", list(music_data[genre].keys()))

if st.button("🎵 노래 추천받기"):
    song = random.choice(music_data[genre][artist])
    st.success(f"**{artist} - {song['title']}**")
    st.markdown(f"[유튜브에서 보기 ▶️]({song['url']})")

