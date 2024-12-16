import streamlit as st
from datetime import datetime, date

def calculate_age(birthdate):
    today= date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Set the title of the web page
st.title('Simple Web Form with Streamlit')
# Set a header
st.header('User Information Users')
# Text input for name
st.subheader('Personal Details')
name = st.text_input('Enter your name:')
# Dropdown menu for selecting an option
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Choose an Option:', options)
# Slider for selecting a value
slider_value = st.slider('Select a value', 1, 100, 50)
#Radio Button for selecting gender
gender = st.radio('Select your gender: ', ('Male', 'Female'))
#Checkboxes for selecting hobbies
hobbies = []
st.header('Selecting your Hobbies')
if st.checkbox('Reading'):
    hobbies.append('Reading')
if st.checkbox('Traveling'):
    hobbies.append('Traveling')
if st.checkbox('Cooking'):
    hobbies.append('Cooking')
#Date picker for selecting a birthdate
birthdate = st.date_input('Selecting your birthdate: ', datetime(2000, 1, 1))
# Submit button
if st.button('Submit'):
    age= calculate_age(birthdate)
    st.subheader('Submitted Information')
    st.write(f'Name: {name}')
    st.write(f'Selected Option: {selected_option}')
    st.write(f'Slider Value:{slider_value}')
    st.write(f'Gender: {gender}')
    st.write(f'Hobbies: {" , " .join(hobbies) if hobbies else 'None'}')
    st.write(f'Birthdate: {birthdate}')
    st.write(f'Age: {age}')
# Additional information
st.subheader('Summary')
st.write("Fill out the form above and click the submit button")
# Footer
