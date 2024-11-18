import streamlit as st
from streamlit_gsheets import GSheetsConnection
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')

st.title("Nutrition")


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["2D Data", "3D Data", "Full database", "Concept", "Input form", "Proteines du jour"])



# --------- Import gsheet with data
# Access stuff: https://docs.streamlit.io/develop/tutorials/databases/private-gsheet
conn = st.connection("gsheetsAlimentsProteines", type=GSheetsConnection)
df = conn.read()

with tab2:
    st.subheader("3D visualisation")
    
    # see https://plotly.com/python/3d-charts/
    st.write("Ici, on montre simplement les points dans un espace, selon leurs calories aux 100g, leurs protéines aux 100g et leur prix aux 100g.")
    figThreeDOne = px.scatter_3d(
    	df, 
        x='Calories par 100g', 
        y='Proteines par 100g', 
        z='Prix aux 100g', 
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
        z='Prix aux 100g', 
        size='Calories par 100g', 
        color='Categorie aliment',
        hover_name='Nom de l\'aliment')
    st.plotly_chart(figThreeDTwo, use_container_width=True)

    # see https://plotly.com/python/3d-charts/
    st.write("Ici, de même à nouveau, mais leur taille est aussi proportionelle à leur prix aux 100g.")
    figThreeDTwo = px.scatter_3d(
        df,
        x='Calories par 100g', 
        y='Proteines par 100g', 
        z='Prix aux 100g', 
        size='Prix aux 100g', 
        color='Categorie aliment',
        hover_name='Nom de l\'aliment')
    st.plotly_chart(figThreeDTwo, use_container_width=True)


with tab1:
    st.subheader("Proteine to Calories")
    st.write("Dans les graphes ci dessous, les points en bas à droite représentent les aliments à forte densité en protéines, mais pauvres en calories. La taille des bulles ou leur couleur representent leur prix aux 100g.")
    figTwoDOne = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Calories par 100g',
        color='Categorie aliment',
        hover_name = 'Nom de l\'aliment',
        size = 'Prix aux 100g'
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
        y='Prix aux 100g',
        size='Calories par 100g',
        color='Categorie aliment',
        hover_name = 'Nom de l\'aliment'
    )
        
    st.plotly_chart(figTwoDTwo, use_container_width=True)

    st.write("Idem mais j'ai enlevé les calories pour se concentrer sur le ratio prix/prots")

    figTwoDFour = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Prix aux 100g',
        color='Categorie aliment',
        hover_name = 'Nom de l\'aliment'
    )
        
    st.plotly_chart(figTwoDFour, use_container_width=True)

with tab3:
    st.write(df)

with tab4:
    st.subheader("Nutrition - ma compréhension pour le moment")
    st.write("Voilà ce que j'en comprends pour le moment.")
    st.write("La graisse, c'est de l'énergie stockée par le corps, et ça se compte en calories, 1kg de gras étant 7700 calories. Ce qu'on mange est compté en calories positives. En négatif, on brule environ 2000 calories par jour, selon notre poids, taille, etc. Bouger et faire du cardio, ça fait des calories négatives en plus. Si tu manges moins que ta dépense, tu perds du gras. Sinon tu en prends. Et ça se voit sur 2-3 semaines à cause des processus du corps.")
    st.write("Donc pour maigrir, soit bouge, soit mange moins de calories, soit les deux. Et pour ne pas avoir faim, si manger des carbs cale sur le moment, manger des fibres et des protéines est ce qui lisse leur action dans le temps, et évite d'avoir faim à nouveau trop vite.")
    st.write("Pour le muscle: ça se déchire avec l'exercice. Si tu manges des protéines, ça le répare et le fait grossir.")
    st.write("D'où les visualisations sur cette page : tu peux voir les aliments avec beaucoup de protéines pour peu de calories. J'ai aussi ajouté la dimension prix...")
    st.write("Thomas - 17.11.2024")
with tab5:
    st.components.v1.iframe(src="https://docs.google.com/forms/d/e/1FAIpQLScZHgBQCmItwf1iI0_FuqO4VRCmDLlfs4YEts8KbGWvlmswIQ/viewform?embedded=true", width=700, height=3800, scrolling=True)

with tab6:
    st.subheader("Proteine Daily")
    userWeight = st.slider(label="Entrez votre poids avec le slide ci-dessous", min_value = 50, max_value = 100, value = 70)
    col1, col2 = st.columns(2)

    with col1:
        targetProteinsMin = userWeight * 1.2
        targetProteinsMax = userWeight * 2
        targetProteins = userWeight * 1.6
        st.subheader("Entree des donnees")
        st.write("Pour optimiser la prise de muscle, on doit manger entre 1.2 et 2g de protéine par kg de poid personnel. Cela vous donne donc " + str(targetProteins) + "g de proteines à manger par jour (minimum " + str(targetProteinsMin) + ", maximum " + str(targetProteinsMax) + ")")

        df['Repas'] = ""
        df['Quantite consommee'] = pd.Series(dtype='int')
        df['Proteines consommee'] = pd.Series(dtype='int')
        df['Total proteines consommees'] = 0    



        df = st.data_editor(
            df, 
            column_config={
                "Horodateur": None,
                'Nom de l\'aliment': st.column_config.TextColumn(
                    disabled=True
                ),
                'Proteines par 100g': None, 
                'Prix aux 100g': None,
                'Calories par 100g': None,
                'Kiff aux 100g ': None,
                'Proteines par portion': None,
                'Prix par portion': None,
                'Calories par portion': None,
                'Categorie aliment': None,
                'URL Source': None,
                'Repas': st.column_config.SelectboxColumn(
                        options = [
                            "Petit dej",
                            "Midi",
                            "Gouter",
                            "Soir",
                            "Snack"
                        ]
                    ),
                'Quantite consommee': st.column_config.NumberColumn(
                    step=1,
                    format="%d g"
                ),
                'Proteines consommee': None,
                'Total proteines consommees': None
            },
            hide_index = True)

        df['Proteines consommee'] = df['Quantite consommee'] * (df['Proteines par 100g'] / 100)

    with col2:
        st.subheader("Proteines consommees")
        selection = st.segmented_control(label="Choisir le dicing", options=["Repas", "Categorie aliment", "Nom de l\'aliment"])
        figDailyProt = px.bar(df, x='Total proteines consommees', y="Proteines consommee", color=selection, hover_name='Nom de l\'aliment', hover_data=['Quantite consommee', 'Proteines par 100g'])
        figDailyProt.add_hline(y=targetProteins, line_dash="dash", line_color="green")
        
        figDailyProt.add_hrect(y0=targetProteinsMin, y1=targetProteinsMax, line_width=0, fillcolor="green", opacity=0.2)
        st.plotly_chart(figDailyProt, use_container_width=True)

    st.write(df)
