import streamlit as st
# import gspread as gs
import pandas as pd

# --------- Import gsheet with recipes
# Use json identifier
# gc = gs.service_account(filename='recipe-finder-379006-704429557353.json')
# Open the spreadsheet link to the input form
# sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oR39MoNU1HP04L8k4zmbt4BdQANouu7KlkEfubFBFMc/edit?usp=sharing')
# Open the correct worksheet
# ws = sh.worksheet('Réponses au formulaire 1')
# Convert it in pandas dataframe to be able to work with it
# df = pd.DataFrame(ws.get_all_records())

# --------- Import csv with recipes
df = pd.read_csv('recipe.csv', encoding='cp1252')

# --------- Sidebar and global things

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')
st.image(image='logo/light-logo.png', width=600)

# That does not work, to check later
# with st.sidebar:
#    st.image(image='logo/chosen_logo_squared.png')

# ----------------------------------

st.title("Niffling généralisé")

col1, col2, col3 = st.columns(3)

with col1:
    hungriness_level = st.radio(label="On fait vite?", options=('OUI J\'AI FAIM', 'Non, j\'ai le temps'))
    if hungriness_level == 'OUI J\'AI FAIM':
        time_to_cook = 30
    else:
        time_to_cook = 2000

with col2:
    cooking_skill = st.slider(label="Skill level", min_value=1, max_value=5, value=3, step=1, help="Ton niveau de cuisine sur une échelle de 1 à 5.")

with col3:
    frigo_rempli = st.slider(label="Ton frigo est rempli?", min_value=1, max_value=5, value=3, step=1, help="Si ton frigo est plus ou moins plein en gros. C'est moi qui fait les hypothèses sur ce que ça veut dire :-) Désactivé pour le moment", disabled=True)

df[(df['Temps de preparation (duree totale, en minutes)'] < time_to_cook) & (df['Complexite'] <= cooking_skill)]