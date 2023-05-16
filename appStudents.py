import streamlit as st 
from streamlit_chat import message
from llama_index import GPTSimpleVectorIndex
import random
import csv
import time
import os

os.environ["OPENAI_API_KEY"] = "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"

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
    os.environ["OPENAI_API_KEY"] = st.text_input("Give Your OpenAi Api ke")


submittedAnswer = False
waiting_for_user_answer = False
answer = "Default"

def generate_answer_for_custom_input(prompt):
    try :        
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
        quiz = index.query(prompt)
        questions = quiz 
        return questions
    except:
        with input_container:
            st.error("Verify OpenAi API Key.")



#Load Questions 
def locate_random_direct_question(csv_file="questions.csv"):
    with open(csv_file, 'r',encoding="utf-8") as file:
        lines = list(csv.reader(file))
        random_index = random.randrange(1, len(lines))
        random_row = lines[random_index]
        return random_row[0] , random_row[1] 

def locate_random_quiz(csv_file="quiz.csv"):
    with open(csv_file, 'r',encoding="utf-8") as file:
        lines = list(csv.reader(file))
        random_index = random.randrange(1, len(lines))
        random_row = lines[random_index]
        return random_row[0] , random_row[1] 


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
    global answer
    if text_input :
        print("Hello here1")
        if user_input == "Direct Question":
            print("Hello here2")
            answer = generate_answer_for_custom_input(text_input)
            return generate_answer_for_custom_input(text_input) ,""
        elif user_input == "Text Input":
            return answer,""
        elif user_input == "Quiz":
            return answer,""
    if user_input == "Direct Question":
        question , answer= locate_random_direct_question() 
        return question , answer
    elif user_input == "Text Input":
        return "You can ask me about any of your university courses ! (jk not all of them)"
    elif user_input == "Quiz":
        question , answer = locate_random_quiz()
        return question , answer
        

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
        st.session_state.input_global = input
        try :
            response,response2 = generate_response(input)
            st.session_state.answer = response2
            st.session_state.custom_answer = False
            st.session_state.student.append(input)
            st.session_state.tutor.append(response)
        except:
            response = generate_response(input)
            st.session_state.answer = response
            st.session_state.custom_answer = True
            st.session_state.student.append(input)
            st.session_state.tutor.append(response)


if text_input_bool: 
    with input_container:
        text_input = st.text_input("Give an Answer: ", "", key="input")
        if st.button("Submit") :
            time.sleep(1)
            if text_input :
                if not st.session_state.custom_answer:
                    answer = st.session_state.answer
                    st.session_state.student.append(text_input)
                    st.session_state.tutor.append(answer)
                    text_input_bool = False
                else : 
                    answer = generate_answer_for_custom_input(text_input)
                    st.session_state.student.append(text_input)
                    st.session_state.tutor.append(answer.response.strip())
                    text_input_bool = False

        
    if st.session_state['tutor']:
        for i in range(len(st.session_state['tutor'])):
            message(st.session_state['student'][i], is_user=True, key=str(i) + '_user',avatar_style="fun-emoji",seed=5)
            message(st.session_state["tutor"][i], key=str(i),avatar_style="bottts-neutral",seed=6)


