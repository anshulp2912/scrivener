<h1 align="center">
 <img src="https://github.com/anshulp2912/scrivener/blob/main/media/logo/logo.gif" />
</h1>

# SE Project 1

# SCRIVENER 


[![DOI](https://zenodo.org/badge/295188611.svg)](https://zenodo.org/badge/latestdoi/295188611)

[![Build Status](https://travis-ci.org/bsharathramesh/SE_Project1.svg?branch=master)](https://travis-ci.org/bsharathramesh/SE_Project1)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## INTRODUCTION

Scrivener is a video transcript summarizer for Youtube videos. Youtube is one of the most used website. A lot of people use the captions to understand the language of the video. In our project we aim to create a transcript summarizer which accepts a youtube URL link, collects the caption at every sentence and then provides the summary of the complete video. Our goal is to make the summarizer as accurate as possible and to add various other features. Our second goal of the project is to create a summarizer which can summarize the youtube videos which have captions disabled. Our project can be further expanded for numerous applications. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features. Also, the document aids the developers in understanding the code and acts as a reference point for starting the project.

<h1 align="center">
 <img src="https://github.com/anshulp2912/scrivener/blob/main/media/working_animation/scrivener_working.gif" />
</h1>

The complete development was achieved using the following technologies and it is recommended that the next set of developers who take up this project have these technologies installed and keep them running before proceeding further:
Python3
Django
HTML
CSS
Scrappy
Vader Analysis Tool

Although we have used HTML and CSS for the FrontEnd, the users can merge the backend logic with any of the front end frameworks they wish to use such as React, angularJS, etc.


## Steps for execution
1. Run `pip install -r requirements.txt` followed by `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`
2. Make sure you change the path accordingly in the files.  (Refer to the issue: https://github.com/bsharathramesh/SE_Project1/issues/31 to get the list of files where changes are needed)
3. Execute manage.py using the command `python3 manage.py runserver` at `/SE_Project1/sentimental_analaysis`. This runs the Django server such that we can open the webUI for the project on the browser.
4. Next, open your browser and type in `localhost:8000` in the search bar to open the webUI of the application.
5. The UI typically looks as shown below and here you have a choice between URL, file or normal text input.




## FUTURE SCOPE

Summarization of any video without captions.

Auto summary as a video.

Summarization of videos for particular time frames.

Summarization of Podcasts (audiofiles).

Summarization as a audio.

Summarization of audios for particular time frames.

Adding Chrome extension.

## Team Members

Anshul Patel

Bhavya Omprakash Agrawal

Darshan Patel

Pragna Bollam

Rohan Shah
				
