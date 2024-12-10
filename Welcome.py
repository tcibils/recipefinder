import streamlit as st
from streamlit_gsheets import GSheetsConnection
import gspread as gs
import pandas as pd

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')


st.title("Welcome !")

st.write("Ceci est mon bac à sable et instrument de prise de notes, pour ce qui est lié aux recettes et à la nutrition en général. Streamlit ne permet que deux applications gratuitement, une est privée, et voici l'autre dans laquelle je squeeze donc tout !")
st.write("La première partie du site liste des recettes, en se basant sur des aliments dispos ou non, pour trouver de l'inspiration. C'est le \"Recipe Niffler\", du nom des créatures d'Harry Potter tome 3, qui fouillent des trésors. Cette partie date principalement de début 2023.")
st.write("La deuxième partie regroupe tous les éléments liés à la nutrition en général, et surtout aux protéines et à la construction musculaire. J'y stock ma compréhension, des données et des graphes utilisant ces données.")
st.write("Je ne sais pas qui d'autre que moi pourrait être arrivé là, mais bienvenue :) N'hésitez pas à me contacter pour discuter !")
st.write("Thomas Cibils - 10.12.2024")