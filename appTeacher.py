import streamlit as st
import pandas as pd
import time

def data_extraction(file=None):
    st.title("Topics : ")

    # Example list of strings
    strings = ['Apple', 'Banana', 'Cherry', 'Durian', 'Elderberry', 'Fig', 'Grape', 'Honeydew']

    # Paginate the strings
    page_size = 5
    num_pages = (len(strings) + page_size - 1) // page_size
    # current_page = st.sidebar.empty()

    if 'page_number' not in st.session_state:
        st.session_state.page_number = 1

    prev_page, next_page = st.columns([1, 1])

    if prev_page.button("Previous"):
        st.session_state.page_number -= 1
        if st.session_state.page_number < 1:
            st.session_state.page_number = 1

    if next_page.button("Next"):
        st.session_state.page_number += 1
        if st.session_state.page_number > num_pages:
            st.session_state.page_number = num_pages

    start_index = (st.session_state.page_number - 1) * page_size
    end_index = st.session_state.page_number * page_size
    paginated_strings = strings[start_index:end_index]

    # Convert the paginated strings to a DataFrame
    df = pd.DataFrame({'Strings': paginated_strings})

    df['Remove'] = [False] * len(df)
    remove_strings = st.multiselect('Select strings to remove', df['Strings'].tolist())
    df.loc[df['Strings'].isin(remove_strings), 'Remove'] = True
    df = df[~df['Remove']]
    df = df.drop(columns=['Remove'])

    # Display the table
    st.dataframe(df)

    # Button to validate removed strings
    if st.button("Validate Removed Strings"):
        removed_strings = remove_strings
        st.write("Removed Strings:")
        st.write(removed_strings)
        topics_filtered = df['Strings']
        st.success("Removed Succefully")
        return topics_filtered


def main():
    st.title("QuizGPT-Esi")
    
    # Upload multiple files
    uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)
    
    if uploaded_files:
        # Display the list of uploaded file names
        st.write("Uploaded Files:")
        for file in uploaded_files:
            st.write(file.name)
        uploaded = True
        if uploaded :
            data_extraction()
            

if __name__ == "__main__":
    main()
