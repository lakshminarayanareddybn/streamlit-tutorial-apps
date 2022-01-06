import streamlit as st
import pandas as pd

st.write("LNR: Here's your first attempt to use streamlit cloud to host application")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
