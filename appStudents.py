import streamlit as st 
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
import random
import csv

st.set_page_config(page_title="QuizGpt-ESI")

with st.sidebar:
    st.title('📚💬 QuizGpt-ESI')
    st.markdown('''
    ## About
    This app is a :
    - AI tutor built with GPT-3
    - [LlangChain](<https://python.langchain.com/en/latest/index.html>)
    - [Github Repo](<https://github.com/MedX1736/QuizGPT.git>)
    
    💡 Note: OpenAi api key not required ! The questions are already generated
    ''')

waiting_for_user_answer = True
#Load Questions 
def locate_random_row(csv_file="output.csv"):
    with open(csv_file, 'r',encoding="utf-8") as file:
        lines = list(csv.reader(file))
        random_index = random.randrange(1, len(lines))
        random_row = lines[random_index]
        return random_row[0] , random_row[1]

def get_type():
    with input_container:
        st.write("Select an option:")

        col1, col2, col3 = st.columns(3)

        option_selected = col1.button("Text Input")
        if option_selected:
            user_input = st.text_input("You: ", "", key="input")

        option_selected = col2.button("Quiz")
        if option_selected:
            user_input = "Quiz"  # Replace with your desired string or logic for quiz input

        option_selected = col3.button("Direct Question")
        if option_selected:
            user_input = "Direct Question"
    if option_selected: 
        return user_input

def generate_response(user_input):
    if user_input == "Direct Question":
        question , answer = locate_random_row()

        return question
    elif user_input == "Quiz":
        return ""
    elif user_input == "Quiz":
        return ""
    
    



input_container = st.container()

## Applying the user input box
with input_container:
    if waiting_for_user_answer:
        user_input = st.text_input("Give an Answer: ", "", key="input")
    else:
        input = get_type()

st.markdown("<hr>", unsafe_allow_html=True)

response_container = st.container()

if 'tutor' not in st.session_state:
    st.session_state['tutor'] = ["I'm QuizChat, How may I help you?"]

if 'student' not in st.session_state:
    st.session_state['student'] = ['Hi!']  

with response_container:
    if input:
        response = generate_response(input)
        st.session_state.student.append(input)
        st.session_state.tutor.append(response)
        
    if st.session_state['tutor']:
        for i in range(len(st.session_state['tutor'])):
            message(st.session_state['student'][i], is_user=True, key=str(i) + '_user',avatar_style="fun-emoji",seed=5)
            message(st.session_state["tutor"][i], key=str(i),avatar_style="bottts-neutral",seed=6)


