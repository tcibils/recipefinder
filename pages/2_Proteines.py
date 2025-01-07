import streamlit as st
from streamlit_gsheets import GSheetsConnection
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')

st.title("Nutrition")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Concept", "2D Data", "3D Data", "Proteines du jour", "Full database"])



# --------- Import gsheet with data
# Access stuff: https://docs.streamlit.io/develop/tutorials/databases/private-gsheet
conn = st.connection("gsheetsAlimentsProteines", type=GSheetsConnection)
df = conn.read()

with tab1:
    st.header("Ma compréhension à ce stade")
    st.subheader("Calories, énergie, gras")
    st.markdown(" * La graisse, c'est de l'énergie stockée par le corps, et ça se compte en calories. 1kg de gras vaut environ 7700 calories.")
    st.markdown(" * L'énergie comprise dans ce qu'on mange est également compté en calories, comme apport. Chaque aliment apporte une certaine quantité de calories par 100g.")
    st.markdown(" * En négatif, on brule environ 2000 calories par jour, selon notre poids, taille, etc. Bouger et faire du cardio, ça fait des calories négatives en plus.")
    st.markdown("Donc, si on mange moins que la dépense totale, on dépense plus d'énergie qu'on en consomme, et le corps prend le déficit dans le gras qu'on commence à perdre. Si on mange plus que la dépense totale, le corps stock, on en prend. Et ça se voit sur 2-3 semaines à cause des processus du corps.")
    st.write("Donc pour maigrir, soit bouge, soit mange moins de calories, soit les deux. Et pour ne pas avoir faim, si manger des carbs cale sur le moment, manger des fibres et des protéines est ce qui lisse leur action dans le temps, et évite d'avoir faim à nouveau trop vite.")
    st.subheader("Protéines et muscles")
    st.write("Pour le muscle: ça se déchire avec l'exercice en salle. En mangeant des protéines, on lui donne de quoi se réparer et se patcher, ce qui le fait grossir. Pour une prise de muscle optimale, il faut consommer 1.7 à 2.2g de protéines par jour et poids de corps, donc pour un individu de 70kg, entre 1.7 * 70 = 119g et 2.2 * 70 = 154g. Attention à ne JAMAIS dépasser 2.2 à 2.4g/kg/j !!")
    st.write("Les visualisations dans les onglets sur cette page permettent de voir les aliments avec beaucoup de protéines pour peu de calories. J'ai aussi ajouté la dimension prix. On peut aussi y visualiser rapidement si la quantité de protéines consommée permet d'atteindre son objectif journalier.")
    st.write("Attention, connaître la quantité de protéines ne suffit pas ! Leur composition en acides aminés est importante pour leur absorbtion par le corps ! Voir graphiques et vidéo ci-dessous")

    col1, col2 = st.columns(2)

    with col1:
        st.image(image="pages/acides-amines-web.jpg", caption="Les protéines sont composées de divers acides aminés. Les non-essentiels peuvent être recréés par notre corps en partant des autres, et les essentiels doivent être apportés par l'alimentation.")

    with col2:
        st.image("pages/BCAA-amino-acids.png", caption="Parmis les essentiels, voici leur fonction, et les 3 ciblés par les BCAA.")

    st.subheader("Meilleure whey protein et autres compléments")
    st.markdown(" * La whey normale, lactique, est plus complète et semble clairement supérieure à la whey d'origine végétale. Une bonne idée est de la mélanger au lait. Pour la source, le prix vient souvent de l'emballage. [Reddit semble très au clair](https://www.reddit.com/r/Switzerland/comments/1e2eck1/gym_people_from_which_websites_do_you_purchase/) que [Lee Sport](https://whey-protein.ch/products/bio-whey-protein) est la meilleure source suisse.")
    st.markdown(" * Les BCAA contiennent trois acides aminés spécifiques. Le bénéfice d'en prendre semble prouvé mais très limité. Ils seraient à prendre en petite dose en complément de la whey.")
    st.markdown(" * La créatine semble marcher et être sans danger, et avoir un effect clair, mais limité à quelques kg de muscle, mais c'est toujours ça de pris.")
    st.markdown(" * Les stéroides sont une immense merde dangereuse et il ne faut surtout pas s'en approcher.")

    col3, col4 = st.columns(2)
    with col3:
       with st.expander("Vidéo expliquant bien les acides aminés derrière les protéines"):
            st.video(data="https://www.youtube.com/watch?v=0iUtJAyzOMY")
    
    with col4:
        with st.expander("Vidéo source quant à mon avis whey/BCAA/créatine"):
            st.video(data="https://youtu.be/eoSrjDn7qT4?si=V2n304J_JugYx6Er&t=117")

    st.markdown("[Autre source intéressante](https://www.anses.fr/fr/content/les-proteines)")
    st.write("Thomas - 07.01.2025")


with tab3:
    st.subheader("3D visualisation")
    
    # see https://plotly.com/python/3d-charts/
    st.write("Ici, on montre simplement les points dans un espace, selon leurs calories aux 100g, leurs protéines aux 100g et leur Prix par 100g.")
    figThreeDOne = px.scatter_3d(
    	df, 
        x='Calories par 100g', 
        y='Proteines par 100g', 
        z='Prix par 100g', 
        color='Categorie aliment',
        hover_name='Nom de l\'aliment'
        )

    st.plotly_chart(figThreeDOne, use_container_width=True)
    
    # see https://plotly.com/python/3d-charts/
    st.write("Ici, l'idée est la même, mais leur taille est aussi proportionelle à leurs calories aux 100g.")
    figThreeDTwo = px.scatter_3d(
        df,
        x='Calories par 100g', 
        y='Proteines par 100g', 
        z='Prix par 100g', 
        size='Calories par 100g', 
        color='Categorie aliment',
        hover_name='Nom de l\'aliment')
    st.plotly_chart(figThreeDTwo, use_container_width=True)

    # see https://plotly.com/python/3d-charts/
    st.write("Ici, de même à nouveau, mais leur taille est aussi proportionelle à leur Prix par 100g.")
    figThreeDTwo = px.scatter_3d(
        df,
        x='Calories par 100g', 
        y='Proteines par 100g', 
        z='Prix par 100g', 
        size='Prix par 100g', 
        color='Categorie aliment',
        hover_name='Nom de l\'aliment')
    st.plotly_chart(figThreeDTwo, use_container_width=True)


with tab2:
    st.subheader("Proteine to Calories")
    st.write("Dans les graphes ci dessous, les points en bas à droite représentent les aliments à forte densité en protéines, mais pauvres en calories. La taille des bulles ou leur couleur representent leur Prix par 100g.")
    figTwoDOne = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Calories par 100g',
        color='Categorie aliment',
        hover_name = 'Nom de l\'aliment',
        size = 'Prix par 100g'
    )
        
    st.plotly_chart(figTwoDOne, use_container_width=True)

    st.write("Idem mais j'ai enlevé le prix pour se concentrer sur le ratio calories/prots")
    figTwoDThree = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Calories par 100g',
        color='Categorie aliment',
        hover_name = 'Nom de l\'aliment',
    )
    st.plotly_chart(figTwoDThree, use_container_width=True)


    st.subheader("Proteine to Price")
    st.write("Dans le graphe ci dessous, les points en bas à droite représentent les aliments à forte densité en protéines, et peu chers. La taille des bulles represente leurs calories aux 100g.")
    figTwoDTwo = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Prix par 100g',
        size='Calories par 100g',
        color='Categorie aliment',
        hover_name = 'Nom de l\'aliment'
    )
        
    st.plotly_chart(figTwoDTwo, use_container_width=True)

    st.write("Idem mais j'ai enlevé les calories pour se concentrer sur le ratio prix/prots")

    figTwoDFour = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Prix par 100g',
        color='Categorie aliment',
        hover_name = 'Nom de l\'aliment'
    )
        
    st.plotly_chart(figTwoDFour, use_container_width=True)

    st.image("pages/P-NPE.png", caption="Information similaire trouvée dans une infographie sur le web")

with tab5:
    st.write(df)

with tab4:
    st.subheader("Proteine Daily")
    userWeight = st.slider(label="Entrez votre poids avec le slide ci-dessous", min_value = 50, max_value = 100, value = 75)
    targetProteinsMin = userWeight * 1.4
    targetProteinsMax = userWeight * 2.2
    targetProteins = userWeight * 1.8
    st.write("Hors prise de muscle, on conseille 1 à 1.3g de protéines par poids de corps. Pour optimiser la prise de muscle, en fonction de l'activité, on augmente au prorata jusqu'à 2.2g par kg de poid personnel. ([Source](https://youtu.be/eoSrjDn7qT4?si=V2n304J_JugYx6Er&t=117)) Cela vous donne donc " + str(targetProteins) + "g de proteines à manger par jour (minimum " + str(targetProteinsMin) + ", maximum " + str(targetProteinsMax) + "), ce qui est reflété dans le graphe.")

    col1, col2 = st.columns(2)


    with col1:
        st.subheader("Entree des donnees")

        df['Matin'] = False
        df['Midi'] = False
        df['Gouter'] = False
        df['Soir'] = False
        df['Snack'] = False
        df['Repas'] = ""
        df['Portions'] = 0
        df['Nb portion calcule'] = 0
        df['Proteines consommee'] = pd.Series(dtype='int')
        df['Total proteines consommees'] = 0    

        

        # categoriesToFilter = st.pills(label='Table filter:', options=['Animale','Poisson','Lactique','Legumineuse','Noix','Artificiel'],disabled=True,help='I can sort the table with this, but it erases the input from the users everytime the filtering is changed')
        # df = df[df['Categorie aliment'] == categoriesToFilter]
        df = st.data_editor(
            df, 
            column_config={
                "Horodateur": None,
                'Nom de l\'aliment': st.column_config.TextColumn(
                    disabled=True
                ),
                'Proteines par 100g': None, 
                'Prix par 100g': None,
                'Calories par 100g': None,
                'Kiff aux 100g ': None,
                'Categorie aliment': st.column_config.TextColumn(),
                'URL Source': None,
                'Matin': st.column_config.CheckboxColumn(),
                'Midi': st.column_config.CheckboxColumn(),
                'Gouter': st.column_config.CheckboxColumn(),
                'Soir': st.column_config.CheckboxColumn(),
                'Snack': st.column_config.CheckboxColumn(),
                'Repas': None,
                'Portions': st.column_config.NumberColumn(
                    step = 0.1,
                    format="%f portions"
                ),
                'Proteines consommee': None,
                'Total proteines consommees': None,
                'Portion en g': st.column_config.NumberColumn(),
                'Nb portion calcule': None
            },
            hide_index = True)
        
        df['Nb portion calcule'] = df['Matin'].astype(int) + df['Midi'].astype(int) + df['Gouter'].astype(int) + df['Soir'].astype(int) + df['Snack'].astype(int)
        df['Total Portions'] = df[['Nb portion calcule', 'Portions']].max(axis='columns')
        df['Proteines consommee'] = df['Total Portions'] * (df['Proteines par 100g'] / 100) * df['Portion en g']

    with col2:
        st.subheader("Proteines consommees")
        
        # selection = st.segmented_control(label="Choisir le dicing", options=["Repas", "Categorie aliment", "Nom de l\'aliment"], disabled=True, default="Categorie aliment", help="Not implemented yet.")
        selection = "Categorie aliment"
        figDailyProt = px.bar(df, x='Total proteines consommees', y="Proteines consommee", color=selection, hover_name='Nom de l\'aliment', hover_data=['Total Portions', 'Proteines par 100g'])
        figDailyProt.add_hline(y=targetProteins, line_dash="dash", line_color="green")
        
        figDailyProt.add_hrect(y0=targetProteinsMin, y1=targetProteinsMax, line_width=0, fillcolor="green", opacity=0.2)
        st.plotly_chart(figDailyProt, use_container_width=True)

    st.write(df)
