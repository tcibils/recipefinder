import streamlit as st

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='centered')
st.image(image='logo/light-logo.png', width=600)

st.title("Ajouter une recette")
st.markdown("En utilisant le formulaire ci-dessous, une recette sera ajoutée à la database. Si ça ne fonctionne pas, [le formulaire peut être trouvé ici](https://docs.google.com/forms/d/e/1FAIpQLSevKH2SDfUuGyaWWxu-tSZIs7hM7Dpayb1dMfSWaRDmtUVG5Q/viewform)", unsafe_allow_html=True)


st.components.v1.iframe(src="https://docs.google.com/forms/d/e/1FAIpQLSevKH2SDfUuGyaWWxu-tSZIs7hM7Dpayb1dMfSWaRDmtUVG5Q/viewform?embedded=true", width=700, height=3800, scrolling=True)