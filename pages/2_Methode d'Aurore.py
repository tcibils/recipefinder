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

st.title("Méthode Aurore")

feculents = st.checkbox(label='Sans féculents', value=True)

legumes_options = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates', 'Aubergines', 'Poivron', 'Salade verte ', 'Concombre', 'Fenouil')
legumes_preselected = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates')

legumes_choisis = st.multiselect(label='Légumes dans le frigo', options=legumes_options, default=legumes_preselected)
autres_choisis = st.multiselect(label='Autres dans le frigo', options=('Lardons', 'Jambon'))

legumes_not_in_fridge = list(set(legumes_options) - set(legumes_choisis))

# Filter out any recipe requiring any legume we don't have 
df[df['Légumes'].str.contains('|'.join(legumes_not_in_fridge))==False]