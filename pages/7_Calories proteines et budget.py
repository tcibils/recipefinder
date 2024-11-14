import streamlit as st
import pandas as pd
import gspread as gs

st.title("Nutrition")
st.subheader("Règles générales")
st.write("C'est pas très compliqué tout ça.")
st.write("La graisse, c'est de l'énergie stockée. L'unité c'est les calories, 1kg de gras c'est 7700 calories. L'énergie que tu manges, c'est compté en calories positives. De base tu brules environ 2000 calories par jour. Bouger et faire du cardio, ça fait des calories négatives. Si tu manges moins que ta dépense, tu perds du gras. Sinon tu en prends. Donc soit bouge, soit mange moins de calories, et tu maigriras.")
st.write("Le muscle, ça se déchire avec l'exercice. Si tu manges des protéines, ça le répare et le fait grossir.")
st.write("D'où les visualisations ci-dessous : tu peux voir les aliments avec beaucoup de protéines pour peu de calories. J'ai aussi ajouté la dimension prix...")

tab1, tab2 = st.tabs(["Data", "Input form"])

with tab1:
    st.subheader("Matrice")

    # --------- Import gsheet with data
    # Use json identifier
    gc = gs.service_account(filename='recipe-finder-379006-704429557353.json')
    # Open the spreadsheet link to the input form
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1D0jkCa6kZNPYVUhioMycLoiBCBDJQWMrVRjy5c6pd7o/edit?usp=sharing')
    # Open the correct worksheet
    ws = sh.worksheet('Réponses au formulaire 1')
    # Convert it in pandas dataframe to be able to work with it
    df = pd.DataFrame(ws.get_all_records())

    st.write(df)

with tab2:
    st.components.v1.iframe(src="https://docs.google.com/forms/d/e/1FAIpQLScZHgBQCmItwf1iI0_FuqO4VRCmDLlfs4YEts8KbGWvlmswIQ/viewform?embedded=true", width=700, height=3800, scrolling=True)