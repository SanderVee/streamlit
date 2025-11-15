import streamlit as st
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
import pandas as pd

# Yhteys MySQL-tietokantaan
conn = mysql.connector.connect(
    host="localhost",
    user="ubuntu",        # vaihda oma käyttäjä
    password=os.getenv("MYSQL_PASSWORD"), # vaihda oma salasana
    database="vaestoluku"
)

cursor = conn.cursor()
cursor.execute("SELECT year, population FROM population ORDER BY year")
rows = cursor.fetchall()

# Muunna Pandas DataFrameksi
df = pd.DataFrame(rows, columns=["Vuosi", "Väkiluku"])

# Näytä Streamlit-sivulla
st.title("Helsingin väkiluku 2010–2020")
st.write("Tieto haetaan MySQL-tietokannasta:")

st.dataframe(df)

# Piirrä kuvaaja
st.line_chart(df.set_index("Vuosi"))

