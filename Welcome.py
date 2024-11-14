import streamlit as st
from streamlit_gsheets import GSheetsConnection
import gspread as gs
import pandas as pd

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')

# --------- Import gsheet with recipes
# --------- Import gsheet with data
# Access stuff: https://docs.streamlit.io/develop/tutorials/databases/private-gsheet
# Use json identifier
conn = st.connection("gsheetsRecettes", type=GSheetsConnection)
df = conn.read()

# --------- Import csv with recipes
# df = pd.read_csv('recipe.csv', encoding='cp1252')

# --------- Sidebar and global things

st.image(image='logo/chosen_logo.png', width=600)

# That does not work, to check later
# with st.sidebar:
#    st.image(image='logo/chosen_logo_squared.png')

# ----------------------------------


st.title("Recipe Niffler")
st.write("Le but de ce site est de parcourir une petite base de données de recettes, pour avoir facilement de l'inspiration au moment de se faire un repas.")

st.write("Voici dessous la base de données complète")
st.write(df)