"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Which LLM model you\'d like to choose?',
    ('ChatGPT', 'ChatGLM'),key="model"
)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Temperature',
    0.0, 100.0,key="temperature"
)

st.text_input("Enter your prompt here", key="User_input")

"Your model: ",st.session_state.model
"Your temperature: ",st.session_state.temperature
"Your prompt: ",st.session_state.User_input


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
