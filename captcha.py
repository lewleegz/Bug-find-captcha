import streamlit as st
from time import time
from st_clickable_images import clickable_images
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components

st_autorefresh(interval=1000, key="refresh")


if 'level' not in st.session_state:
    st.session_state['level'] = 1


if 'start_time_lvl1' not in st.session_state:
    st.session_state['start_time_lvl1'] = time()
if 'result_lvl1' not in st.session_state:
    st.session_state['result_lvl1'] = None
if 'lvl1_failed_once' not in st.session_state:
    st.session_state['lvl1_failed_once'] = False


if 'start_time_lvl2' not in st.session_state:
    st.session_state['start_time_lvl2'] = None
if 'result_lvl2' not in st.session_state:
    st.session_state['result_lvl2'] = None
if 'lvl2_failed_once' not in st.session_state:
    st.session_state['lvl2_failed_once'] = False

if 'start_time_lvl3' not in st.session_state:
    st.session_state['start_time_lvl3'] = None
if 'result_lvl3' not in st.session_state:
    st.session_state['result_lvl3'] = None
if 'lvl3_failed_once' not in st.session_state:
    st.session_state['lvl3_failed_once'] = False

def level1():
    st.title("Captcha Level 1")
    st.subheader("Click on the bug in the code to prove you are a human:")

    clicked = clickable_images(
        [
            "https://iili.io/FYakXXS.png",
            "https://iili.io/FYa8YSs.png",
            "https://iili.io/FYaUCjR.png",
            "https://iili.io/FYagYUF.png",
            "https://iili.io/FYarn1I.png",
            "https://iili.io/FYa4awJ.png",
            "https://iili.io/FYa6MWx.png",
            "https://iili.io/FYaPO42.png",
            "https://iili.io/FYainZG.png"
        ],
        titles=[f"Image #{i}" for i in range(9)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )

    elapsed = time() - st.session_state['start_time_lvl1']

    if st.session_state['result_lvl1'] is None:
        if clicked > -1:
            st.session_state['result_lvl1'] = 'failed'
        elif elapsed >= 15:
            st.session_state['result_lvl1'] = 'correct'

    if st.session_state['result_lvl1'] == 'failed':
        st.error("❌ You failed! Try again...")
        st.session_state['lvl1_failed_once'] = True

    if st.session_state['lvl1_failed_once']:
        st.session_state['result_lvl1'] = None
        st.session_state['start_time_lvl1'] = time()
        st.session_state['lvl1_failed_once'] = False

    if st.session_state['result_lvl1'] == 'correct':
        st.success("✅ You waited! Moving on to Level 2...")
        st.session_state['level'] = 2
        st.session_state['start_time_lvl2'] = time()

    if elapsed < 15 and st.session_state['result_lvl1'] is None:
        st.info(f"{int(15 - elapsed)} seconds left!")

    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

def level2():
    st.title("Captcha Level 2")
    st.subheader("Find the bug!")

    clicked = clickable_images(
        [
            "https://iili.io/FazGR1V.png",
            "https://iili.io/FazMdyF.png",
            "https://iili.io/FazV9Vf.png",
        ],
        titles=[f"Image #{i}" for i in range(3)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )

    elapsed = time() - st.session_state['start_time_lvl2']

    if st.session_state['result_lvl2'] is None:
        if clicked == 2:
            st.session_state['result_lvl2'] = 'correct'
        elif clicked != -1:
            st.session_state['result_lvl2'] = 'failed'
        elif elapsed >= 15:
            st.session_state['result_lvl2'] = 'failed'

    if st.session_state['result_lvl2'] == 'failed':
        st.error("😞 You failed! Back to Level 1.")
        st.session_state['lvl2_failed_once'] = True

    if st.session_state['lvl2_failed_once']:
        st.session_state['level'] = 1
        st.session_state['start_time_lvl1'] = time()
        st.session_state['result_lvl1'] = None
        st.session_state['result_lvl2'] = None
        st.session_state['lvl2_failed_once'] = False

    if st.session_state['result_lvl2'] == 'correct':
        st.success("🎉 Correct! Moving on to Level 3...")
        st.session_state['level'] = 3
        st.session_state['start_time_lvl3'] = time()

    if elapsed < 15 and st.session_state['result_lvl2'] is None:
        st.info(f"{int(15 - elapsed)} seconds left!")

    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

def level3():
    st.title("Captcha Level 3")
    st.subheader("One more bug!")

    clicked = clickable_images(
        [
            "https://iili.io/FaEkoQI.png",
            "https://iili.io/FaEveRf.png",
            "https://iili.io/FaESnhQ.png",
            "https://iili.io/FaEgYsp.png"
        ],
        titles=[f"Image #{i}" for i in range(4)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )

    elapsed = time() - st.session_state['start_time_lvl3']

    if st.session_state['result_lvl3'] is None:
        if clicked == 2:
            st.session_state['result_lvl3'] = 'correct'
        elif clicked != -1:
            st.session_state['result_lvl3'] = 'correct'
        elif elapsed >= 15:
            st.session_state['result_lvl3'] = 'correct'

    if st.session_state['result_lvl3'] == 'correct':
        st.text("You probably got it right. I dont know, thats hexadecimal code.")
        st.success("🎉 You did it! Captcha complete.")
        components.html(
            """
            <div class="wavy">✅ ALL DONE</div>
            <style>
            .wavy {
              color: #0f0;
              font-size: 48px;
            }
            </style>
            """,
            height=100
        )

    if elapsed < 15 and st.session_state['result_lvl3'] is None:
        st.info(f"{int(15 - elapsed)} seconds left!")

    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

if st.session_state['level'] == 1:
    level1()
elif st.session_state['level'] == 2:
    level2()
else:
    level3()
