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


# --------- Import csv with recipes
# df = pd.read_csv('recipe.csv', encoding='cp1252')

# --------- Sidebar and global things

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')
st.image(image='logo/chosen_logo.png', width=600)

# That does not work, to check later
# with st.sidebar:
#    st.image(image='logo/chosen_logo_squared.png')

# ----------------------------------

st.title("Comment je cuisine ce truc ?")

st.subheader("Welcome")
st.write("Ici, le but est de prendre un aliment, et de trouver des idées de comment ça pourrait être cuisiné. On permet ici de filtrer pour trouver des recettes sans féculents. On suppose qu'on a sel, poivre, oignons ou échalottes, ail, quelques autres épices non périssables comme la muscade, le curry ou le paprika, et des herbes sèches comme les feuilles de laurier ou le thym, pour égayer un peu tout ça.")
st.write("On suppose aussi qu'on a toujours des non-périssables en stock comme de la sauce tomate, du pesto ou de la pâte de curry. Les pois chiches se trouvent en conserve karma et sont bons comme ça.")



st.subheader("Niffling")
feculents = st.checkbox(label='Sans féculents', value=True, help="Par défaut, ne montre par les recettes incluant des féculents.")

all_aliments = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates', 'Aubergines', 'Poivron', 'Salade verte', 'Concombre', 'Fenouil', 'Chou fleur', 'Haricots', 'Petits pois', 'Epinards', 'Brocolis', 'Poulet', 'Viande hachee', 'Oeufs', 'Lardons', 'Jambon', 'Paneer', 'Bacon', 'Ricotta', 'Gruyere', 'Creme', 'Lait', 'Yaourt nature', 'Mozarella', 'Parmesan', 'Pates', 'Riz', 'Quinoa', 'Pommes de terre', 'Patates douces', 'Pain sec ou panure', 'Puree', 'Semoule', 'Lentilles brunes', 'Lentilles beluga', 'Lentilles corail', 'Pois chiches', 'Pois casses', 'Boulgour', 'Citron', 'Basilic', 'Menthe', 'Gingembre')

aliment_choice = st.selectbox(label='Aliment', options=all_aliments, help="Aliment à cuisiner")

st.subheader("Résultats")

# Displayed filter database
# Uses the checkbox to filter out ingredients with feculents if needed, but still show those without feculents if checkbox is unticked
fdf = df[((df['Avec feculents '].str.contains('Non') == feculents) | (df['Avec feculents '].str.contains('Non') == True)) & ((df['Legumes'].str.contains(aliment_choice)==True) | (df['Proteines'].str.contains(aliment_choice)==True) | (df['Laitages'].str.contains(aliment_choice)==True) | (df['Congeles'].str.contains(aliment_choice)==True) |  (df['Laitages'].str.contains(aliment_choice)==True) | (df['Feculents'].str.contains(aliment_choice)==True) | (df['Autres'].str.contains(aliment_choice)==True))]


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
