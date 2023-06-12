import streamlit as st
st.set_page_config(page_title='My Python Web app',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://www.hhl.healthyhappylife.org/images/logo.png')
st.title('HHLF')
st.header('by Dr P K Jha')
if(mymenu=='Home'):
    st.markdown('<center><h1>Welcom</h1?</center>',unsafe_allow_html=True)
    st.text('This is a project which can bring new age!')
    st.video('https://www.youtube.com/watch?v=3Lt2kuxPIcQ')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter your name')
        dob=st.date_input('Enter date of birth')
        marks=st.slider('Choose marks')
        k=st.form_submit_button("Submit")
        if k:
            st.write("Name:",name,"DOB:",dob,"Marks:",marks)
elif(mymenu=='Downloads'):
    st.header('Downloads')
    st.download_button('Download now','This is the downloaded data','down.txt')