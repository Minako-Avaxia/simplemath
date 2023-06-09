import streamlit as st
# import snowflake.connector
import time

@st.cache_data
def expensive_computation(a, b):
    time.sleep(2)  #This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)
