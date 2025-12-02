import streamlit as st
import time
import random

#---------------------------------------------------------
# PAGE CONFIG
#---------------------------------------------------------
st.set_page_config(page_title="Love u Asha ❤️", page_icon="❤️", layout="centered")

#---------------------------------------------------------
# CUSTOM CSS
#---------------------------------------------------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #ffdde1, #ee9ca7);
}

/* Glowing main heart */
.heart {
    font-size: 130px;
    text-align: center;
    animation: pulse 1.2s infinite;
}

/* Heart pulsing animation */
@keyframes pulse {
    0% { transform: scale(0.9); }
    50% { transform: scale(1.1); }
    100% { transform: scale(0.9); }
}

.love-text {
    font-size: 60px;
    text-align: center;
    font-weight: bold;
    color: white;
    text-shadow: 0px 0px 25px #ff0055;
}

/* Floating hearts */
.floating {
    position: fixed;
    animation: floatUp 6s linear infinite;
    opacity: 0.7;
    font-size: 25px;
}

@keyframes floatUp {
    0% { bottom: 0px; opacity: 1; }
    100% { bottom: 100%; opacity: 0; }
}

/* Surprise button */
button.css-19rxjzo, button.st-bq {
    background-color: #ff0055 !important;
    color: white !important;
    border-radius: 10px;
    font-size: 20px;
    border: 2px solid white;
}
</style>
""", unsafe_allow_html=True)

#---------------------------------------------------------
# FLOATING HEART ANIMATION
#---------------------------------------------------------
for i in range(18):
    x = random.randint(0, 95)
    delay = random.uniform(0, 5)
    st.markdown(
        f"""
        <div class="floating" style="left:{x}%; animation-delay:{delay}s;">
            ❤️
        </div>
        """,
        unsafe_allow_html=True,
    )

#---------------------------------------------------------
# MAIN SCREEN
#---------------------------------------------------------
st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='love-text'>Love u Asha</div>", unsafe_allow_html=True)

#---------------------------------------------------------
# SURPRISE BUTTON
#---------------------------------------------------------
if st.button("Click for Surprise ❤️"):
    msg = "Asha, you make everything feel beautiful ❤️"

    placeholder = st.empty()
    for i in range(len(msg) + 1):
        placeholder.markdown(
            f"<h3 style='text-align:center; color:white;'>{msg[:i]}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(0.06)

    st.balloons()
