import streamlit as st

st.set_page_config(page_title='Cibils Recipe', page_icon='logo/chosen_logo_squared.png', layout='centered')
st.image(image='logo/chosen_logo.png', width=600)

st.title("Ajouter un aliment protéiné")
st.markdown("En utilisant le formulaire ci-dessous, un alimnet protéiné sera ajouté à la database. Si ça ne fonctionne pas, [le formulaire peut être trouvé ici](https://forms.gle/HwMaQHhZWps8epiQ6)", unsafe_allow_html=True)

st.components.v1.iframe(src="https://docs.google.com/forms/d/e/1FAIpQLScZHgBQCmItwf1iI0_FuqO4VRCmDLlfs4YEts8KbGWvlmswIQ/viewform?embedded=true", width=700, height=3800, scrolling=True)
