import streamlit as st
import plotly.express as px
import requests
import selectorlib
time

# Back End



# Front End

st.title("Temperatures Scraped from https://programmer100.pythonanywhere.com/")

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)