# week1assignment.py

import streamlit as st
import time

st.set_page_config(page_title="Score Tracker & Timer", layout="centered")
st.title("🎯 Score Tracker with Timer")

# Initialize state
if 'score_team1' not in st.session_state:
    st.session_state.score_team1 = 0
if 'score_team2' not in st.session_state:
    st.session_state.score_team2 = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = 0
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False

# Timer logic
def start_timer():
    if not st.session_state.timer_running:
        st.session_state.start_time = time.time() - st.session_state.elapsed_time
        st.session_state.timer_running = True

def pause_timer():
    if st.session_state.timer_running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.timer_running = False

def reset_all():
    st.session_state.score_team1 = 0
    st.session_state.score_team2 = 0
    st.session_state.start_time = None
    st.session_state.elapsed_time = 0
    st.session_state.timer_running = False

# Score Section
st.subheader("🏆 Scores")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Team 1")
    if st.button("➕ Add 1", key="add1_team1"):
        st.session_state.score_team1 += 1
    if st.button("➖ Subtract 1", key="sub1_team1"):
        st.session_state.score_team1 = max(0, st.session_state.score_team1 - 1)
    st.markdown(f"**Score: {st.session_state.score_team1}**")

with col2:
    st.markdown("### Team 2")
    if st.button("➕ Add 1", key="add1_team2"):
        st.session_state.score_team2 += 1
    if st.button("➖ Subtract 1", key="sub1_team2"):
        st.session_state.score_team2 = max(0, st.session_state.score_team2 - 1)
    st.markdown(f"**Score: {st.session_state.score_team2}**")

# Timer controls
st.subheader("⏱️ Timer")
col3, col4, col5 = st.columns(3)

with col3:
    if st.button("▶️ Start"):
        start_timer()
with col4:
    if st.button("⏸️ Pause"):
        pause_timer()
with col5:
    if st.button("🔄 Reset All"):
        reset_all()

# Update elapsed time if timer is running
if st.session_state.timer_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time

# Display the elapsed time
minutes, seconds = divmod(int(st.session_state.elapsed_time), 60)
st.markdown(f"### Elapsed Time: **{minutes:02d}:{seconds:02d}**")

# Refresh manually
st.info("⏳ Timer updates when you click or interact with the app.\n\n"
        "For real-time auto-updating, a package like `streamlit-autorefresh` is recommended.")
