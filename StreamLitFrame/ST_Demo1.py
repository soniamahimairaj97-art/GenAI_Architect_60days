import streamlit as st
import emoji 

st.title("Welcome to my First Streamlit app")

name=st.text_input("enter ur name")
angry=emoji.emojize(":angry_face:")
happy=emoji.emojize(":smile:")
grumpy=emoji.emojize(":unamused_face:")
st.button("Say Hello")
if name=='soni':
    st.success(f"Hello {name} , welcome to SE community {happy}")
elif name=='s':
    st.header(f"{name} dont leave empty  {angry}")
else:
    st.warning(f"pls enter ur name {grumpy}")