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

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png')
st.image(image='logo/light-logo.png')

# That does not work, to check later
# with st.sidebar:
#    st.image(image='logo/chosen_logo_squared.png')

# ----------------------------------


st.title("Recipe Niffler")
st.write("Le but de ce site est juste de parcourir une petite base de données de recettes, pour avoir facilement de l'inspiration au moment de se faire un repas.")

st.write("Il est supposé que vous avez chez vous les essentiels suivants")

ingredients_de_base = ('Gruyère', 'Lait', 'Crème', 'Oignons ou échalottes', 'Ail')

st.write(ingredients_de_base)

st.write('Ainsi que les epices suivantes:')

epices_de_base = ('Sel', 'Poivre', 'Herbes fraiches, type basilic ou menthe', 'Muscade')

st.write(epices_de_base)

st.write("Voici dessous la base de données complètes")
st.write(df)