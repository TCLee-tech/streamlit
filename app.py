import streamlit as st
import pandas as pd
import numpy as np

if 'df' not in st.session_state:
  st.session_state.df = pd.DataFrame(np.random.randn(20,2), columns=["x", "y"])

st.header("choose a datapoint color")
color = st.color_picker("color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)
st.write(st.session_state.df)

st.sidebar.markdown("# Main page")
'''
Instructions to create virtual environment using VS Code
1. create folder. mkdir folder_name
2. cd folder_name
3. create virtual environment. python -m venv .venv.
  - In VS Code, open Command Palette (CTRL + SHIFT + P) and then select 'Python: Create Environment'.
  - Select python installation in 'Python: Select Interpreter' 
  - https://code.visualstudio.com/docs/python/python-tutorial
4. change VS Code terminal to Command Prompt. Select Command Prompt option from drop down in upper right corner of terminal.
5. activate environment. .venv\Scripts\activate.bat
  - should see (.venv) in front of prompt if activated
6. install packages, e.g. pip install streamlit
7. test for successful installation, e.g. streamlit hello, streamlit run app.py
8. to deactivate virtual environment, use 'deactivate'
Ref: https://docs.streamlit.io/get-started/installation/command-line
'''
