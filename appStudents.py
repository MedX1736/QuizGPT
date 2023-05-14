import streamlit as st 
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header

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

def get_type():
    with input_container:
        st.write("Select an option:")

        col1, col2, col3 = st.columns(3)

        option_selected = col1.button("Text Input")
        if option_selected:
            user_input = st.text_input("You: ", "", key="input")

        option_selected = col2.button("Quiz")
        if option_selected:
            user_input = "Quiz ✨"  # Replace with your desired string or logic for quiz input

        option_selected = col3.button("Direct Question")
        if option_selected:
            user_input = "Direct Question ❓"
        
input_container = st.container()

## Applying the user input box
with input_container:
    user_input = get_type()

st.markdown("<hr>", unsafe_allow_html=True)

response_container = st.container()

if 'tutor' not in st.session_state:
    st.session_state['tutor'] = ["I'm QuizChat, How may I help you?"]

if 'student' not in st.session_state:
    st.session_state['student'] = ['Hi!']  

with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.student.append(user_input)
        st.session_state.tutor.append(response)
        
    if st.session_state['tutor']:
        for i in range(len(st.session_state['tutor'])):
            message(st.session_state['student'][i], is_user=True, key=str(i) + '_user',avatar_style="fun-emoji",seed=5)
            message(st.session_state["tutor"][i], key=str(i),avatar_style="bottts-neutral",seed=6)


