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

st.title("Je vais faire les courses, on mange quoi ce soir ?")
st.subheader("Intro")
st.write("L'idée ici est qu'on a le temps d'aller faire les courses, ou qu'on y va, et donc qu'on peut avoir les ingrédients qu'on veut pour cuisiner quelque chose.")

