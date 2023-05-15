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

submittedAnswer = False
waiting_for_user_answer = False

#Load Questions 
def locate_random_direct_question(csv_file="output.csv"):
    with open(csv_file, 'r',encoding="utf-8") as file:
        lines = list(csv.reader(file))
        random_index = random.randrange(1, len(lines))
        random_row = lines[random_index]
        return random_row[0] , random_row[1] , random_index

def locate_random_quiz(csv_file="output.csv"):
    with open(csv_file, 'r',encoding="utf-8") as file:
        lines = list(csv.reader(file))
        random_index = random.randrange(1, len(lines))
        random_row = lines[random_index]
        return random_row[0] , random_row[1] , random_index


def get_type():
    with input_container:
        st.write("Select an option:")

        col1, col2, col3 = st.columns(3)

        option_selected_1 = col1.button("Text Input")
        option_selected_2 = col2.button("Quiz")
        option_selected_3 = col3.button("Direct Question")
        if option_selected_1:
            return "Text Input"
        if option_selected_2:
            return "Quiz"
        if option_selected_3 :
            return "Direct Question"

def clear_input():
    st.session_state["input"] = ""  


def generate_response(user_input,text_input=None):
    if user_input == "Direct Question":
        question , answer , index = locate_random_direct_question() 
        return question
    elif user_input == "Text Input":
        return "You can ask me about any of your university courses ! (jk not all of them)"
    elif user_input == "Quiz":
        question , answer , index = locate_random_direct_question()
        return question
    if text_input :
        return "Omba3d n repondilek"
input_container = st.container()

with input_container:
        input = get_type()
        text_input_bool = True

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


if text_input_bool: 
    with input_container:
        text_input = st.text_input("Give an Answer: ", "", key="input")
        if st.button("Submit") :
            if text_input :
                response = generate_response(input,text_input)
                st.session_state.student.append(text_input)
                st.session_state.tutor.append(response)
                text_input_bool = False

    # if submittedAnswer and 
        
    if st.session_state['tutor']:
        for i in range(len(st.session_state['tutor'])):
            message(st.session_state['student'][i], is_user=True, key=str(i) + '_user',avatar_style="fun-emoji",seed=5)
            message(st.session_state["tutor"][i], key=str(i),avatar_style="bottts-neutral",seed=6)


