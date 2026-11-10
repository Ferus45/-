
import streamlit as st
import random

st.set_page_config(
    page_title="ЯРИК.exe 💀",
    page_icon="🌰",
    layout="centered"
)

memes = [
    "Ярик, ты конченный финик 💀",
    "Ярик — главный враг тыквенных семечек 🎃",
    "Фундук увидел Ярика и сам раскололся 🌰",
    "Ярик, даже финик от тебя отвернулся",
    "Тыквенные семечки требуют защиты от Ярика",
    "Ярик — 99% фундук и 1% здравого смысла",
    "Финик передал, что больше тебя не знает",
    "Ярик, ты не орех, ты ошибка природы",
    "Ярик настолько странный, что даже фундук в шоке",
    "Ярик.exe перестал отвечать"
]

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #160b25, #40204f);
    color: white;
}
h1 {
    color: #e9b5ff !important;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #d6b8e8;
    font-size: 20px;
}
.meme {
    background: #29183b;
    border: 2px solid #a855f7;
    border-radius: 20px;
    padding: 35px 15px;
    text-align: center;
    font-size: 24px;
    margin: 25px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("ЯРИК.exe 💀")
st.markdown(
    '<p class="subtitle">Официальная энциклопедия легенды</p>',
    unsafe_allow_html=True
)

st.markdown("## 🌴 Священные связи Ярика")
st.markdown("""
- 🌴 Финик
- 🎃 Тыквенные семечки
- 🌰 Фундук
""")

if "meme" not in st.session_state:
    st.session_state.meme = memes[0]

st.markdown("## 💀 Генератор мемов")

st.markdown(
    f'<div class="meme">{st.session_state.meme}</div>',
    unsafe_allow_html=True
)

if st.button("🔥 УНИЗИТЬ ЯРИКА", use_container_width=True):
    st.session_state.meme = random.choice(memes)
    st.rerun()

st.markdown("---")
st.caption("ЯРИК.exe | Финиковая империя © 2026")
