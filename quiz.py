
import streamlit as st
import requests




VEXT_API_URL = "https://payload.vextapp.com/hook/R8QY9GK2J0/catch/$(channel_token)"
API_KEY = "WBdqCgOL.6GPq6ikEncfDvYEqKLYCJbLsIg96uYNF"
HEADERS = {
    "Content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}


def get_vext_data(topic):
    payload = {"payload": topic}
    try:
        response = requests.post(VEXT_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}


quiz_genres = (
    "General Knowledge",
    "Science and Nature",
    "Indian History",
    "Indian Geography",
    "Indian Literature",
    "Entertainment",
    "Sports",
    "Art and Culture",
    "Language and Words",
    "Food and Drink",
    "Technology",
    "Math and Logic",
    "Health and Medicine",
    "Business and Economy",
    "Mythology and Religion",
    "Hobbies and Interests",
    "Politics and Law",
    "Music"
)

difficulty_level=( "Easy" , "Medium" , "Hard")

st.title(":red[QUIZ O'CLOCK]")
# Streamlit app layout
with st.sidebar:
    st.image('logo.png',width=250)
    option1 = st.selectbox("Quiz Genre : ", quiz_genres)
    option2 = st.selectbox("Difficulty Level : ", difficulty_level)
    no_of_questions = st.slider("How many questions?", 1, 25, 5)
    input_text = f"{option1} genre and {no_of_questions} questions in number and of {option2} level"
    if st.button("Search"):
        r=1
    else :
        r=0

if(r==1):
    if input_text:
        with st.spinner('Fetching data ...'):
            data = get_vext_data(input_text)
            if "error" in data:
                st.error(data["error"])
            else:
                questions = data.get("text", "No questions found")
                st.markdown(questions)
    else:
        st.warning("Please enter a valid input.")
