import streamlit as st
from streamlit_gsheets import GSheetsConnection
import plotly.express as px

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='wide')

st.title("Nutrition")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["2D Data", "3D Data", "Full database", "Concept", "Input form"])



# --------- Import gsheet with data
# Access stuff: https://docs.streamlit.io/develop/tutorials/databases/private-gsheet
conn = st.connection("gsheetsAlimentsProteines", type=GSheetsConnection)
df = conn.read()

with tab2:
    st.subheader("Matrice")
    
    # see https://plotly.com/python/3d-charts/
    figThreeD = px.scatter_3d(
    	df, 
        x='Calories par 100g', 
        y='Proteines par 100g', 
        z='Prix aux 100g', 
        color='Categorie aliment',
        hover_data='Nom de l\'aliment'
        )

    st.plotly_chart(figThreeD, use_container_width=True)

with tab1:
    st.subheader("Proteine to Price")
    figTwoDOne = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Calories par 100g',
        color='Categorie aliment',
        hover_data = 'Nom de l\'aliment',
        size = 'Prix aux 100g'
    )
        
    st.plotly_chart(figTwoDOne, use_container_width=True)
    
    st.subheader("Proteine to Price")
    figTwoDTwo = px.scatter(
    	df,
        x = 'Proteines par 100g', 
        y='Prix aux 100g',
        size='Calories par 100g',
        color='Categorie aliment',
        hover_data = 'Nom de l\'aliment'
    )
        
    st.plotly_chart(figTwoDTwo, use_container_width=True)

with tab3:
    st.write(df)

with tab4:
    st.subheader("Règles générales")
    st.write("C'est pas très compliqué tout ça.")
    st.write("La graisse, c'est de l'énergie stockée. L'unité c'est les calories, 1kg de gras c'est 7700 calories. L'énergie que tu manges, c'est compté en calories positives. De base tu brules environ 2000 calories par jour. Bouger et faire du cardio, ça fait des calories négatives. Si tu manges moins que ta dépense, tu perds du gras. Sinon tu en prends. Donc soit bouge, soit mange moins de calories, et tu maigriras.")
    st.write("Le muscle, ça se déchire avec l'exercice. Si tu manges des protéines, ça le répare et le fait grossir.")
   st.write("D'où les visualisations sur cette page : tu peux voir les aliments avec beaucoup de protéines pour peu de calories. J'ai aussi ajouté la dimension prix...")


with tab5:
    st.components.v1.iframe(src="https://docs.google.com/forms/d/e/1FAIpQLScZHgBQCmItwf1iI0_FuqO4VRCmDLlfs4YEts8KbGWvlmswIQ/viewform?embedded=true", width=700, height=3800, scrolling=True)
