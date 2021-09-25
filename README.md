<h1 align="center">
 <img src="https://github.com/anshulp2912/scrivener/blob/main/media/logo/logo.gif" />
</h1>

# scrivener
# SE Project 1

# C.E.L.T: The Sentimental Analyser 

### YouTube Link: 

[![Video](https://i9.ytimg.com/vi_webp/zvme9ARshD8/mqdefault.webp?sqp=CJTzs_sF&rs=AOn4CLBkjs-_C1oPtVtZgfWL2llzZA_dKw)](https://youtu.be/VLoJCemCdHg)

[![DOI](https://zenodo.org/badge/295188611.svg)](https://zenodo.org/badge/latestdoi/295188611)

[![Build Status](https://travis-ci.org/bsharathramesh/SE_Project1.svg?branch=master)](https://travis-ci.org/bsharathramesh/SE_Project1)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## INTRODUCTION

Sentiment analysis is one of the fastest growing research areas in computer science, making it challenging to keep track of all the activities in the area. In our project we aim to achieve our goal in accurately predicting a users sentiment by analysing the data provided in any of the four different methods. They are Document Analysis, Text Analysis, Product Analysis and Audio Analysis. This project though currently in the initial stages of development, can be further applied to numerous domains which can be useful for the society. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features before releasing to the market. Also, the document aids the developers in understanding the code and acts as a reference point for starting the project.

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

![First](https://user-images.githubusercontent.com/43075652/97276268-31ce6100-17f4-11eb-8b57-7741069bf311.png)
![second](https://user-images.githubusercontent.com/43075652/97276507-82de5500-17f4-11eb-88e0-0ea41bc9b424.png)

The UI for URL input is as shown below:
![product](https://user-images.githubusercontent.com/43075652/97276542-925d9e00-17f4-11eb-910f-103be084ad13.png)

The UI for file input is as shown below:
![docum](https://user-images.githubusercontent.com/43075652/97277008-2891c400-17f5-11eb-901a-1ebd3da5a32b.png)

The UI for text input is as shown below:
![text](https://user-images.githubusercontent.com/43075652/97277038-33e4ef80-17f5-11eb-8fbc-76bad26adcc9.png)

The UI for audio input is as shown below:
![audio](https://user-images.githubusercontent.com/43075652/97277059-3d6e5780-17f5-11eb-8dcf-a5935d6613ae.png)

The Output as below:
![output](https://user-images.githubusercontent.com/43075652/97277225-74446d80-17f5-11eb-89f5-2b27c957827e.png)
![out](https://user-images.githubusercontent.com/43075652/97277310-8e7e4b80-17f5-11eb-8910-03ec42ea0ff7.png)

## Case Study: Amazon Product Review Sentiment and Text Analysis

### WordCloud of Reviews
![wc](https://user-images.githubusercontent.com/9015214/97310439-9e1f8380-1839-11eb-8060-0944d7e4d7d9.png)

### Reviews Summary
<img width="896" alt="Screen Shot 2020-10-27 at 9 49 08 AM" src="https://user-images.githubusercontent.com/9015214/97310491-aaa3dc00-1839-11eb-97ef-e2e27fd6fad2.png">

### Sentiment Summary
<img width="864" alt="Screen Shot 2020-10-27 at 9 48 02 AM" src="https://user-images.githubusercontent.com/9015214/97310362-834d0f00-1839-11eb-97db-f32a3d1f9eed.png">

### Confusion Matrix
![conf](https://user-images.githubusercontent.com/9015214/97310260-631d5000-1839-11eb-9a3b-102fa9737439.png)



## FUTURE SCOPE

Implement user authentication to store history for each user.

Recommendation system based on analysis results.

Live speech to text sentiment analysis.

Enhance the analysis by taking into consideration the number of users rated for each product!

Extend the analysis to the Facebook, Twitter and LinkedIn Posts

## Team Members

Matt Pudlo

Prasanth Yadla

Abhi Joshi

Mita Gavade

Suyash Jain
				
