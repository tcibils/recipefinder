import streamlit as st
from streamlit_gsheets import GSheetsConnection
import gspread as gs
import pandas as pd

# --------- Sidebar and global things

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')
st.image(image='logo/chosen_logo.png', width=600)

# --------- Import gsheet with recipes
conn = st.connection("gsheetsRecettes", type=GSheetsConnection)
df = conn.read()


# --------- Import csv with recipes
# df = pd.read_csv('recipe.csv', encoding='cp1252')



# That does not work, to check later
# with st.sidebar:
#    st.image(image='logo/chosen_logo_squared.png')

# ----------------------------------

st.title("Méthode Aurore")

st.subheader("Welcome")
st.write("On permet ici de trouver des recettes sans féculents, et en se basant sur les ingrédients qu'on a au frigo. On suppose qu'on a sel, poivre, oignons ou échalottes, ail, quelques autres épices non périssables comme la muscade, le curry ou le paprika, et des herbes sèches comme les feuilles de laurier ou le thym, pour égayer un peu tout ça.")
st.write("On suppose aussi qu'on a toujours des non-périssables en stock comme de la sauce tomate, du pesto ou de la pâte de curry. Les pois chiches se trouvent en conserve karma et sont bons comme ça.")

st.subheader("Niffling")
feculents = st.checkbox(label='Sans féculents', value=True, help="Par défaut, ne montre par les recettes incluant des féculents.")

col1, col2, col3 = st.columns(3)

with col1:
    legumes_options = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates', 'Aubergines', 'Poivron', 'Salade verte', 'Concombre', 'Fenouil', 'Chou fleur')
    legumes_preselected = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates')
    legumes_choisis = st.multiselect(label='Légumes dans le frigo', options=legumes_options, default=legumes_preselected)
    legumes_not_available = list(set(legumes_options) - set(legumes_choisis))

with col2:
    congeles_options = ('Haricots', 'Petits pois', 'Epinards', 'Brocolis')
    congeles_preselected = ('Haricots', 'Petits pois', 'Epinards')
    congeles_choisis = st.multiselect(label='Légumes dans le congélateur', options=congeles_options, default=congeles_preselected)    
    congeles_not_available = list(set(congeles_options) - set(congeles_choisis))

with col3:
    proteines_options = ('Poulet', 'Viande hachee', 'Oeufs', 'Lardons', 'Jambon', 'Paneer', 'Bacon')
    proteines_preselected = ('Oeufs')
    proteines_choisis = st.multiselect(label='Protéines au frigo', options=proteines_options, default=proteines_preselected)    
    proteines_not_available = list(set(proteines_options) - set(proteines_choisis))

with col1:
    laitages_options = ('Ricotta', 'Gruyere', 'Creme', 'Lait', 'Yaourt nature', 'Mozarella', 'Parmesan')
    laitages_preselected = ('Gruyere', 'Lait', 'Parmesan')
    laitages_choisis = st.multiselect(label='Laitages au frigo', options=laitages_options, default=laitages_preselected)    
    laitages_not_available = list(set(laitages_options) - set(laitages_choisis))

with col2:
    feculents_options = ('Pates', 'Riz', 'Quinoa', 'Pommes de terre', 'Patates douces', 'Pain sec ou panure', 'Puree', 'Semoule', 'Lentilles brunes', 'Lentilles beluga', 'Lentilles corail', 'Pois chiches', 'Pois casses', 'Boulgour', 'Fond de pate')
    feculents_preselected = ('Pates', 'Riz', 'Quinoa', 'Pommes de terre', 'Patates douces', 'Puree', 'Lentilles beluga', 'Pois casses')
    feculents_choisis = st.multiselect(label='Légumineuses et féculents', options=feculents_options, default=feculents_preselected)    
    feculents_not_available = list(set(feculents_options) - set(feculents_choisis))

with col3:
    autres_options = ('Citron', 'Basilic', 'Menthe', 'Gingembre', 'Pignons')
    autres_preselected = ('Basilic', 'Menthe')
    autres_choisis = st.multiselect(label='Autres', options=autres_options, default=autres_preselected)    
    autres_not_available = list(set(autres_options) - set(autres_choisis))

st.subheader("Résultats")

# st.write(df)

# Displayed filter database
# Uses the checkbox to filter out ingredients with feculents if needed, but still show those without feculents if checkbox is unticked
# For each ingredient type, exclude recipe needing any ingredient we would not have
# But for each ingredient type, keep any recipe not needing any ingredient from the ingredient type 
fdf = df[((df['Avec feculents '].str.contains('Non') == feculents) | (df['Avec feculents '].str.contains('Non') == True)) & ((df['Legumes'].str.contains('|'.join(legumes_not_available))==False) | (df['Legumes'].notnull() == False)) & ((df['Proteines'].str.contains('|'.join(proteines_not_available))==False) | (df['Proteines'].notnull() == False)) & ((df['Laitages'].str.contains('|'.join(laitages_not_available))==False) | (df['Laitages'].notnull() == False)) & ((df['Congeles'].str.contains('|'.join(congeles_not_available))==False) | (df['Congeles'].notnull() == False)) & ((df['Laitages'].str.contains('|'.join(laitages_not_available))==False) | (df['Laitages'].notnull() == False)) & ((df['Feculents'].str.contains('|'.join(feculents_not_available))==False) | (df['Feculents'].notnull() == False)) & ((df['Autres'].str.contains('|'.join(autres_not_available))==False) | (df['Autres'].notnull() == False))]


# st.write(fdf)

col4, col5, col6 = st.columns(3)
counter = 1

for index in fdf['Nom de la recette']:
    if counter % 3 == 1:
        with col4:
            with st.expander(label=index, expanded=False):
                if len(str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['URL d\'une photo'])) > 0:
                    st.image(image=str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['URL d\'une photo']))
                st.write(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Rapide descriptif'])
                st.write("Temps de préparation total: " + str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Temps de preparation (duree totale, en minutes)']) + " minutes")
                st.write("On remercie chaleureusement " + str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Adresse e-mail']) + " pour la recette !")

    if counter % 3 == 2:
        with col5:
            with st.expander(label=index, expanded=False):
                if len(str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['URL d\'une photo'])) > 0:
                    st.image(image=str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['URL d\'une photo']))
                st.write(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Rapide descriptif'])
                st.write("Temps de préparation total: " + str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Temps de preparation (duree totale, en minutes)']) + " minutes")
                st.write("On remercie chaleureusement " + str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Adresse e-mail']) + " pour la recette !")

    if counter % 3 == 0:
        with col6:
            with st.expander(label=index, expanded=False):                
                if len(str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['URL d\'une photo'])) > 0:
                    st.image(image=str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['URL d\'une photo']))
                st.write(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Rapide descriptif'])
                st.write("Temps de préparation total: " + str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Temps de preparation (duree totale, en minutes)']) + " minutes")
                st.write("On remercie chaleureusement " + str(fdf.loc[fdf['Nom de la recette'] == index].squeeze()['Adresse e-mail']) + " pour la recette !")

    counter += 1
