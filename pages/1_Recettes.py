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


# --------- Import csv with recipes
# df = pd.read_csv('recipe.csv', encoding='cp1252')


# That does not work, to check later
# with st.sidebar:
#    st.image(image='logo/chosen_logo_squared.png')

# ----------------------------------


tabA, tabB, tabC, tabD, tabE = st.tabs(["Methode Aurore", "Je peux faire les courses", "Comment je cuisine cet aliment", "Pour tout le monde", "Full database"])

with tabA:
    st.title("Méthode Aurore")

    st.subheader("Welcome")
    st.write("On permet ici de trouver des recettes sans féculents, et en se basant sur les ingrédients qu'on a au frigo. On suppose qu'on a sel, poivre, oignons ou échalottes, ail, quelques autres épices non périssables comme la muscade, le curry ou le paprika, et des herbes sèches comme les feuilles de laurier ou le thym, pour égayer un peu tout ça.")
    st.write("On suppose aussi qu'on a toujours des non-périssables en stock comme de la sauce tomate, du pesto ou de la pâte de curry. Les pois chiches se trouvent en conserve karma et sont bons comme ça.")

    st.subheader("Niffling")
    feculentsTabA = st.checkbox(label='Sans féculents', value=True, help="Par défaut, ne montre par les recettes incluant des féculents.", key="feculentsTabA")

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
    fdf = df[((df['Avec feculents '].str.contains('Non') == feculentsTabA) | (df['Avec feculents '].str.contains('Non') == True)) & ((df['Legumes'].str.contains('|'.join(legumes_not_available))==False) | (df['Legumes'].notnull() == False)) & ((df['Proteines'].str.contains('|'.join(proteines_not_available))==False) | (df['Proteines'].notnull() == False)) & ((df['Laitages'].str.contains('|'.join(laitages_not_available))==False) | (df['Laitages'].notnull() == False)) & ((df['Congeles'].str.contains('|'.join(congeles_not_available))==False) | (df['Congeles'].notnull() == False)) & ((df['Laitages'].str.contains('|'.join(laitages_not_available))==False) | (df['Laitages'].notnull() == False)) & ((df['Feculents'].str.contains('|'.join(feculents_not_available))==False) | (df['Feculents'].notnull() == False)) & ((df['Autres'].str.contains('|'.join(autres_not_available))==False) | (df['Autres'].notnull() == False))]


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



with tabB:
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



with tabC:
    st.title("Comment je cuisine ce truc ?")

    st.subheader("Welcome")
    st.write("Ici, le but est de prendre un aliment, et de trouver des idées de comment ça pourrait être cuisiné. On permet ici de filtrer pour trouver des recettes sans féculents. On suppose qu'on a sel, poivre, oignons ou échalottes, ail, quelques autres épices non périssables comme la muscade, le curry ou le paprika, et des herbes sèches comme les feuilles de laurier ou le thym, pour égayer un peu tout ça.")
    st.write("On suppose aussi qu'on a toujours des non-périssables en stock comme de la sauce tomate, du pesto ou de la pâte de curry. Les pois chiches se trouvent en conserve karma et sont bons comme ça.")



    st.subheader("Niffling")
    feculentsTabC = st.checkbox(label='Sans féculents', value=True, help="Par défaut, ne montre par les recettes incluant des féculents.", key="feculentsTabC")

    all_aliments = ('Carottes', 'Courgettes', 'Poireaux', 'Tomates', 'Aubergines', 'Poivron', 'Salade verte', 'Concombre', 'Fenouil', 'Chou fleur', 'Haricots', 'Petits pois', 'Epinards', 'Brocolis', 'Poulet', 'Viande hachee', 'Oeufs', 'Lardons', 'Jambon', 'Paneer', 'Bacon', 'Ricotta', 'Gruyere', 'Creme', 'Lait', 'Yaourt nature', 'Mozarella', 'Parmesan', 'Pates', 'Riz', 'Quinoa', 'Pommes de terre', 'Patates douces', 'Pain sec ou panure', 'Puree', 'Semoule', 'Lentilles brunes', 'Lentilles beluga', 'Lentilles corail', 'Pois chiches', 'Pois casses', 'Boulgour', 'Fond de pate', 'Citron', 'Basilic', 'Menthe', 'Gingembre')

    aliment_choice = st.selectbox(label='Aliment à cuisiner', options=all_aliments, help="Le truc que tu sais pas cuisiner et pour lequel tu te cherches une recette")

    st.subheader("Résultats")

    # Displayed filter database
    # Uses the checkbox to filter out ingredients with feculents if needed, but still show those without feculents if checkbox is unticked
    fdf = df[((df['Avec feculents '].str.contains('Non') == feculentsTabC) | (df['Avec feculents '].str.contains('Non') == True)) & ((df['Legumes'].str.contains(aliment_choice)==True) | (df['Proteines'].str.contains(aliment_choice)==True) | (df['Laitages'].str.contains(aliment_choice)==True) | (df['Congeles'].str.contains(aliment_choice)==True) |  (df['Laitages'].str.contains(aliment_choice)==True) | (df['Feculents'].str.contains(aliment_choice)==True) | (df['Autres'].str.contains(aliment_choice)==True))]


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

with tabD:
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

with tabE:
    st.write("Le but de cette partie du site est de parcourir une petite base de données de recettes, pour avoir facilement de l'inspiration au moment de se faire un repas.")

    st.write("Voici dessous la base de données complète")
    st.write(df)