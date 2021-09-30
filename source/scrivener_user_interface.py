"""
@author: Scrivener
"""

import streamlit as st
import re
import os
from main.transcribe import TranscribeVideo
from main.transcribe_yt import TranscribeYtVideo
import secrets
from glob import glob

hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def save_file(file):
    with open(os.path.join(os.getcwd(), file.name), 'wb') as f:
        f.write(file.getbuffer())
    return 

st.image("media/logo/logo.gif")

input_format = st.radio('Choose your input format', ['Youtube Link', 'Upload a Video'])

if input_format=='Youtube Link':
    youtube_link = st.text_input('Enter Youtube Link')
    if re.findall('(www\.youtube\.com\/watch\?v=)',youtube_link):
        st.video(youtube_link)
        progress_bar = st.progress(0)
        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])
        progress_bar.progress(10)
        
        with st.spinner(progress_lines+' . . .'):
            progress_bar.progress(25)
            transcribe_video = TranscribeYtVideo(youtube_link)
            progress_bar.progress(40)
            summary = transcribe_video.transcribe_yt_video()
            progress_bar.progress(80)
        progress_bar.progress(100)
        st.header('Summary')
        st.write(summary)
        
    
    elif youtube_link!='':
        st.error('Please enter a valid Youtube Link!')

elif input_format=='Upload a Video':
    file = st.file_uploader('Upload a video',type=['mp4'],accept_multiple_files=False)
    if file is not None:
        st.video(file)
        progress_bar = st.progress(0)
        progress_bar.progress(10)
        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])
        with st.spinner(progress_lines+' . . .'):
            progress_bar.progress(25)
            save_file(file)
            progress_bar.progress(40)
            transcribe_video = TranscribeVideo()
            progress_bar.progress(60)
            summary = transcribe_video.transcribe_video(os.path.join(os.getcwd(), file.name))
        progress_bar.progress(100)
        st.header('Summary')
        st.write(summary)
    else:
        for name in glob('*.mp4'):
            os.remove(name)
