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

st.title("Méthode Aurore")

feculents = st.checkbox(label='Sans féculents', value=True)

col1, col2, col3 = st.columns(3)

with col1:
    legumes_options = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates', 'Aubergines', 'Poivron', 'Salade Verte', 'Concombre', 'Fenouil')
    legumes_preselected = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates')
    legumes_choisis = st.multiselect(label='Légumes dans le frigo', options=legumes_options, default=legumes_preselected)
    legumes_not_available = list(set(legumes_options) - set(legumes_choisis))

with col2:
    congeles_options = ('Haricots', 'Petits pois', 'Epinards', 'Brocolis')
    congeles_preselected = ('Haricots', 'Petits pois', 'Epinards')
    congeles_choisis = st.multiselect(label='Légumes dans le congélateur', options=congeles_options, default=congeles_preselected)    
    congeles_not_available = list(set(congeles_options) - set(congeles_choisis))

with col3:
    proteines_options = ('Poulet', 'Viande hachee', 'Oeufs', 'Lardons', 'Jambon')
    proteines_preselected = ('Oeufs')
    proteines_choisis = st.multiselect(label='Protéines au frigo', options=proteines_options, default=proteines_preselected)    
    proteines_not_available = list(set(proteines_options) - set(proteines_choisis))

with col1:
    laitages_options = ('Ricotta', 'Gruyere', 'Creme')
    laitages_preselected = ('Gruyere')
    laitages_choisis = st.multiselect(label='Laitages au frigo', options=laitages_options, default=laitages_preselected)    
    laitages_not_available = list(set(laitages_options) - set(laitages_choisis))

with col2:
    feculents_options = ('Pates', 'Riz', 'Quinoa', 'Pommes de terre', 'Pain sec ou panure', 'Puree', 'Semoule', 'Lentilles beluga', 'Lentilles corail', 'Pois chiches')
    feculents_preselected = ('Pates', 'Riz', 'Quinoa', 'Pommes de terre', 'Pain sec ou panure', 'Puree', 'Semoule', 'Lentilles beluga', 'Lentilles corail')
    feculents_choisis = st.multiselect(label='Légumineuses et féculents', options=feculents_options, default=feculents_preselected)    
    feculents_not_available = list(set(feculents_options) - set(feculents_choisis))

with col3:
    autres_options = ('Citron', 'Basilic', 'Menthe')
    autres_preselected = ('Basilic', 'Menthe')
    autres_choisis = st.multiselect(label='Autres', options=autres_options, default=autres_preselected)    
    autres_not_available = list(set(autres_options) - set(autres_choisis))

# Displayed filter database
# For each ingredient type, exclude recipe needing any ingredient we would not have
# But for each ingredient type, keep any recipe not needing any ingredient from the ingredient type 
df[((df['Legumes'].str.contains('|'.join(legumes_not_available))==False) | (df['Legumes'].notnull() == False)) & ((df['Proteines'].str.contains('|'.join(proteines_not_available))==False) | (df['Proteines'].notnull() == False)) & ((df['Laitages'].str.contains('|'.join(laitages_not_available))==False) | (df['Laitages'].notnull() == False)) & ((df['Congeles'].str.contains('|'.join(congeles_not_available))==False) | (df['Congeles'].notnull() == False)) & ((df['Laitages'].str.contains('|'.join(laitages_not_available))==False) | (df['Laitages'].notnull() == False)) & ((df['Feculents'].str.contains('|'.join(feculents_not_available))==False) | (df['Feculents'].notnull() == False)) & ((df['Autres'].str.contains('|'.join(autres_not_available))==False) | (df['Autres'].notnull() == False))]

