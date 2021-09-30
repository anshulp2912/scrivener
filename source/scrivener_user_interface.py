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

input_format = st.radio('Choose your input format', ['Youtube Link', 'Upload a Video'])

def save_file(file):
    with open(os.path.join(os.getcwd(), file.name), 'wb') as f:
        f.write(file.getbuffer())
    return 

if input_format=='Youtube Link':
    youtube_link = st.text_input('Enter Youtube Link')
    if re.findall('(www\.youtube\.com\/watch\?v=)',youtube_link):

        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])

        with st.spinner(progress_lines+' . . .'):

            transcribe_video = TranscribeYtVideo(youtube_link)

            summary = transcribe_video.transcribe_yt_video()
        st.write(summary)
        
    elif youtube_link!='':
        st.error('Please enter a valid Youtube Link!')

elif input_format=='Upload a Video':
    file = st.file_uploader('Upload a video',type=['mp4'],accept_multiple_files=False)
    if file is not None:

        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])
        with st.spinner(progress_lines+' . . .'):
            save_file(file)
            transcribe_video = TranscribeVideo()
            summary = transcribe_video.transcribe_video(os.path.join(os.getcwd(), file.name))
        st.write(summary)
    else:
        for name in glob('*.mp4'):
            os.remove(name)