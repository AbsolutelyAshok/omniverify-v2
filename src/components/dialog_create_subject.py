import streamlit as st
from src.database.db import create_subject, subject_code_exists



@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="A")


    if st.button("Create Subject Now", type='primary', width='stretch'):
        subject_code = sub_id.strip().upper()
        if subject_code and sub_name.strip() and sub_section.strip():
            try:
                if subject_code_exists(subject_code):
                    st.warning("That subject code is already in use. Choose a different code.")
                    return
                create_subject(subject_code, sub_name.strip(), sub_section.strip(), teacher_id)
                st.toast("Subject Created Succesfully!")
                st.rerun()
            except Exception as e:
                if "subjects_subject_code_normalized_unique" in str(e):
                    st.warning("That subject code is already in use. Choose a different code.")
                else:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")
