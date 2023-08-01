import streamlit as st
import streamlit_survey as ss

import DButils

st.title("Preference Survey")
st.header("Choose the one you prefer from the two below")

survey = ss.StreamlitSurvey("Preference Survey")
promt_datasets = DButils.get_promt_datasets()
q_ns = len(promt_datasets)
pages = survey.pages(q_ns, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))

responses = {}

with pages:
    for i, promt_dataset in enumerate(promt_datasets):
        if pages.current == i:
            st.subheader(f"Example {i+1}")
            q, q_s = st.columns(2)
            with q:
                st.write("Option 1")
                st.write("Question:")
                st.write(promt_dataset['question'])
                st.write("Description: ")
                st.write(promt_dataset['original_answer'])
            with q_s:
                st.write("Option 2")
                st.write("Question:")
                st.write(promt_dataset['simplified_question'])
                st.write("Description: ")
                st.write(promt_dataset['simplified_q_answer'])
            
            response = survey.radio(options = ["Option 1", "Option 2"], horizontal=True)