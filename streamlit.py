import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon= "tada", layout= "wide")

original_title = '<b style="text-align:center; color:black; font-size: 70px;">The Pokémon Game</b>'
st.markdown(original_title, unsafe_allow_html=True)

st.sidebar.write("---")
x = st.sidebar.slider('Rate this Pokémon Game:',0,5)
if x==1:
    one_star = st.sidebar.markdown("⭐")
if x==2:
    two_star = st.sidebar.markdown("⭐⭐")
if x==3:
    three_star = st.sidebar.markdown("⭐⭐⭐")
if x==4:
    four_star = st.sidebar.markdown("⭐⭐⭐⭐")
if x==5:
    five_star = st.sidebar.markdown("⭐⭐⭐⭐⭐")

y = st.sidebar.text_area("Feedback:",max_chars=250)
st.sidebar.write("---")
z = st.sidebar.button("Submit")
