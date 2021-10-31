"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Scrivener
"""

# Import Libraries
import streamlit as st
import re
import os
import wget
from main.transcribe import TranscribeVideo
from main.transcribe_yt import TranscribeYtVideo
import secrets
from glob import glob

import shutil

# Hide Footer in Streamlit
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Add footer to UI
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/anshulp2912/scrivener" target="_blank">Scrivener</a></p>
<p><a style='display: block; text-align: center;' href="https://github.com/anshulp2912/scrivener/blob/main/LICENSE" target="_blank">MIT License Copyright (c) 2021 Anshul Patel</a></p>
<p>Contributors: Anshul, Bhavya, Darshan, Pragna, Rohan</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# Check if ML model files have been combined, if not combine them
# This needs to be done because the full file is greater than 100mb
# and GitHub does not allow files larger than 100mb to be pushed
if not os.path.exists('source/punct_model_full.pcl'):
    print("Creating punct_model_full.pcl file for ML model...")

    # Storing these models in github causes an issue with the Heroku deployment and exceeds 500 MB (it is 618 MB)
    # slug/payload limit. Therefore, using this alternative to get it from GDrive during runtime.
    if not os.path.exists('source/punct_model_part1.pcl'):
        print("Downloading punct_model_part1.pcl file for ML model...")
        url1 = 'https://docs.google.com/uc?export=download&id=1W0zyyDrU1JCdMRrbIsaQWCj9HMhcvZXu'
        filename = wget.download(url1, out='source/punct_model_part1.pcl')
        print("\nDownloaded file: " + filename)

    if not os.path.exists('source/punct_model_part2.pcl'):
        print("Downloading punct_model_part2.pcl file for ML model...")
        url2 = 'https://docs.google.com/uc?export=download&id=1BU4XvFqdmabAGmWzVqTxxgDGF9l29WqV'
        filename = wget.download(url2, out='source/punct_model_part2.pcl')
        print("\nDownloaded file: " + filename)

    if not os.path.exists('source/punct_model_part3.pcl'):
        print("Downloading punct_model_part3.pcl file for ML model...")
        url3 = 'https://docs.google.com/uc?export=download&id=1Rl3u57wNF0X2KvkJNUUQMpJW9uJd-_IM'
        filename = wget.download(url3, out='source/punct_model_part3.pcl')
        print("\nDownloaded file: " + filename)

    first_file = os.path.abspath('source/punct_model_part1.pcl')
    second_file = os.path.abspath('source/punct_model_part2.pcl')
    third_file = os.path.abspath('source/punct_model_part3.pcl')
    new_file = os.path.abspath('source/punct_model_full.pcl')

    with open(new_file, "wb") as wfd:
        for f in [first_file, second_file, third_file]:
            with open(f, "rb") as fd:
                shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)


# Download the uploaded video file
def save_file(file):
    with open(os.path.join(os.getcwd(), file.name), 'wb') as f:
        f.write(file.getbuffer())
    return 

# Display Image
st.image("media/logo/logo.gif")

# Display Radio options
input_format = st.radio('Choose your input format', ['Youtube Link', 'Upload a Video'])

# If user provides a Youtube Link
if input_format=='Youtube Link':
    # Text input box 
    youtube_link = st.text_input('Enter Youtube Link')
    # Check if its a valid youtube link
    if re.findall('(www\.youtube\.com\/watch\?v=)',youtube_link):
        st.video(youtube_link)
        # Make a progress bar
        progress_bar = st.progress(0)
        # Decorative material
        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])
        progress_bar.progress(10)
        
        # Wait till we run the summarization
        with st.spinner(progress_lines+' . . .'):
            progress_bar.progress(25)
            # Call TranscribeYtVideo class 
            transcribe_video = TranscribeYtVideo(youtube_link)
            progress_bar.progress(40)
            # Get summary
            summary = transcribe_video.transcribe_yt_video()
            progress_bar.progress(80)
        # Complete progress bar to 100
        progress_bar.progress(100)
        # Display Summary
        st.header('Summary')
        st.write(summary)
        
    
    # If user inputs an invalid Youtube link
    elif youtube_link!='':
        st.error('Please enter a valid Youtube Link!')

# If user uploads a local video    
elif input_format=='Upload a Video':
    # Browse button for uploading .mp4 files
    file = st.file_uploader('Upload a video',type=['mp4'],accept_multiple_files=False)
    if file is not None:
        st.video(file)
        # Make a progress bar
        progress_bar = st.progress(0)
        progress_bar.progress(10)
        # Decorative material
        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])
        # Wait till we run the summarization
        with st.spinner(progress_lines+' . . .'):
            progress_bar.progress(25)
            # Download the uploaded video file
            save_file(file)
            progress_bar.progress(40)
            # Call TranscribeVideo class 
            transcribe_video = TranscribeVideo()
            progress_bar.progress(60)
            # Get summary
            summary = transcribe_video.transcribe_video(os.path.join(os.getcwd(), file.name))
        # Complete progress bar to 100
        progress_bar.progress(100)
        # Display Summary
        st.header('Summary')
        st.write(summary)
    else:
        for name in glob('*.mp4'):
            os.remove(name)
