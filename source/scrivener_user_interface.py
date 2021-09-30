"""
@author: Scrivener
"""

import streamlit as st
import re
from main.transcribe_yt import TranscribeYtVideo
import secrets

input_format = st.radio('Choose your input format', ['Youtube Link', 'Upload a Video'])

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