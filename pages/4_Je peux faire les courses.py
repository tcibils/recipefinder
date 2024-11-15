import streamlit as st
from streamlit_gsheets import GSheetsConnection
import gspread as gs
import pandas as pd
import random

# --------- Sidebar and global things

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')
st.image(image='logo/chosen_logo.png', width=600)

# --------- Import gsheet with recipes
conn = st.connection("gsheetsRecettes", type=GSheetsConnection)
df = conn.read()

# That does not work, to check later
# with st.sidebar:
#    st.image(image='logo/chosen_logo_squared.png')

# ----------------------------------

st.title("Je vais faire les courses, on mange quoi ce soir ?")
st.write("L'idée ici est qu'on a le temps d'aller faire les courses, ou qu'on y va, et donc qu'on peut avoir les ingrédients qu'on veut pour cuisiner quelque chose.")

random.seed()

col1, col2 = st.columns(2)

with col1:
    complexity = st.slider(label="Complexité", min_value=1, max_value=5, value=3, help="Limite la complexité de la recette proposée")
    style_chosen = st.slider(label="Style", min_value=1, max_value=5, value=4, help="Détermine à quel point la recette doit être stylée")

with col2:
    cooking_time = st.slider(label="Temps de préparation", min_value=0, max_value=200, value=35, help="Temps de préparation total maximum")

fdf = df[(df['Complexite'] <= complexity) & (df['Style'] >= style_chosen) & (df['Temps de preparation (duree totale, en minutes)'] < cooking_time)]

# num = random.randrange(0, len(fdf))
# st.write(num)

solution_one = fdf.sample()
solution_two = fdf.sample()
solution_three = fdf.sample()

solution_one['Nom de la recette'].squeeze()

tab1, tab2, tab3 = st.tabs([solution_one['Nom de la recette'].squeeze(), solution_two['Nom de la recette'].squeeze(), solution_three['Nom de la recette'].squeeze()])

with tab1:
    st.write(solution_one['Rapide descriptif'].squeeze())
    st.write("Temps de préparation total: " + str(solution_one['Temps de preparation (duree totale, en minutes)'].squeeze()) + " minutes")
    st.write("On remercie chaleureusement " + str(solution_one['Adresse e-mail'].squeeze()) + " pour la recette !")

with tab2:
    st.write(solution_two['Rapide descriptif'].squeeze())
    st.write("Temps de préparation total: " + str(solution_two['Temps de preparation (duree totale, en minutes)'].squeeze()) + " minutes")
    st.write("On remercie chaleureusement " + str(solution_two['Adresse e-mail'].squeeze()) + " pour la recette !")

with tab3:
    st.write(solution_three['Rapide descriptif'].squeeze())
    st.write("Temps de préparation total: " + str(solution_three['Temps de preparation (duree totale, en minutes)'].squeeze()) + " minutes")
    st.write("On remercie chaleureusement " + str(solution_three['Adresse e-mail'].squeeze()) + " pour la recette !")
