import streamlit as st
import gspread as gs
import pandas as pd

# --------- Import gsheet with recipes
# Use json identifier
gc = gs.service_account(filename='recipe-finder-379006-704429557353.json')
# Open the spreadsheet link to the input form
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oR39MoNU1HP04L8k4zmbt4BdQANouu7KlkEfubFBFMc/edit?usp=sharing')
# Open the correct worksheet
ws = sh.worksheet('Réponses au formulaire 1')
# Convert it in pandas dataframe to be able to work with it
df = pd.DataFrame(ws.get_all_records())

# ----------------------------------
st.write("this is df")
st.write(df)