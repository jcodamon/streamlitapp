import streamlit as st

# Set the title of the web page
st.title('Simple Web Form with Streamlit')
# Set a header
st.header('User Information Users')
# Text input for name
name = st.text_input('Enter your name:')
# Dropdown menu for selecting an option
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Choose an Option:', options)
# Slider for selecting a value
slider_value = st.slider('Select a value', 1, 100, 50)
# Submit button
if st.button('Submit'):
    st.write(f'Name: {name}')
    st.write(f'Selected Option: {selected_option}')
    st.write(f'Slider Value:{slider_value}')
# Additional information

# Footer
