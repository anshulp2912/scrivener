<h1 align="center">
 <img src="https://github.com/anshulp2912/scrivener/blob/main/media/logo/logo.gif" />
</h1>

# SCRIVENER 

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
[![GitHub issues](https://img.shields.io/github/issues/TommasU/scrivener)](https://github.com/TommasU/scrivener/issues)
[![GitHub forks](https://img.shields.io/github/forks/TommasU/scrivener)](https://github.com/TommasU/scrivener/network)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5601143.svg)](https://doi.org/10.5281/zenodo.5601143)
[![GitHub license](https://img.shields.io/github/license/TommasU/scrivener)](https://github.com/TommasU/scrivener/blob/main/LICENSE)
![Lines of code](https://img.shields.io/tokei/lines/github/TommasU/scrivener)
![Coverage](https://img.shields.io/badge/Coverage-97%25-red)
![Contributors](https://img.shields.io/badge/Contributors-5-yellowgreen)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/TommasU/scrivener)
[![AutoPep8](https://img.shields.io/badge/AutoPep8-1.6.0-brightgreen)](https://pypi.org/project/autopep8/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=_pg9M32LiG8&ab_channel=AnshulPatel)

## Table of Contents
- [Introduction](#Introduction)
- [Demo](#Demo)
- [Steps for Execution](#ExecutionSteps)
- [License](#License)
- [Contributions](#Contributions)
- [Future Scope](#FutureScope)
- [Team Members](#TeamMember)
- [Acknowledgements](#Acknowledgement)

## Introduction <a name="Introduction"></a>

Scrivener is a video transcript summarizer for Youtube videos. Youtube is one of the most used website. A lot of people use the captions to understand the language of the video. In our project we aim to create a transcript summarizer which accepts a youtube URL link, collects the caption at every sentence and then provides the summary of the complete video. Our goal is to make the summarizer as accurate as possible and to add various other features. Our second goal of the project is to create a summarizer which can summarize the youtube videos which have captions disabled. Our project can be further expanded for numerous applications. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features. Also, the document aids the developers in understanding the code and acts as a reference point for starting the project.

<h1 align="center">
 <img src="https://github.com/anshulp2912/scrivener/blob/main/media/working_animation/scrivener_working.gif" />
</h1>

The complete development was achieved using the Python3 technology and it is recommended that the next set of developers who take up this project have these technologies installed and keep them running before proceeding further.

## Demo <a name="Demo"></a>
The project is deployed on both Streamlit cloud and Heroku.
- [Streamlit](https://share.streamlit.io/anshulp2912/scrivener/main/source/scrivener_user_interface.py)
- [Heroku](https://scrivener-heroku.herokuapp.com/)

## Steps for Execution <a name="ExecutionSteps"></a>
1. Clone the Git repository.
2. Run `pip install -r requirements.txt`
3. Open Command Prompt and change the directory to the location of cloned repository.
4. Run the command `python -m streamlit run ./source/scrivener_user_interface.py`
5. Next, open your browser and type in `localhost:8501` in the search bar to open the webUI of the application.
6. The UI typically looks as shown below and here you have a choice between URL, file or normal text input.

<img src="https://github.com/anshulp2912/scrivener/blob/main/media/demo.PNG" />

## License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/TommasU/scrivener/blob/main/LICENSE) for more details.

## Contributions <a name="Contributions"></a>
Please see our [CONTRIBUTING.md](https://github.com/TommasU/scrivener/blob/main/CONTRIBUTING.md) for instructions on how to contribute to the project by completing some of the issues.

## Version 1.1 Contributions
- Enhanced product quality by improving the summarization model.
- Greatly improved summary formatting to improve readability
- Provided Sentiment Analysis of the generated summary

## Future Scope <a name="FutureScope"></a>
For enhancement of this project following functionalities can be implemented
- Currently our application supports youtube videos and videos with .mp4 extension. Provide support for other video formats
- Perform summarization for videos in languages other than English
- Generate summary of Podcasts or other audiofiles
- Provide summary in form of video
- Generate summary of videos for specific time frames
- UI Enhancement
- Provide summary in form of audio
- Generate summary of audio for specific time frames
- Adding Chrome extension for SCRIVENER
- Develop a Discord BOT for SCRIVENER

## Team Members <a name="TeamMember"></a>

- [Jessica Vargas(jrvargas)](jrvargas@ncsu.edu) <br> 
- [Parth Parikh(pmparikh)](pmparikh@ncsu.edu) <br>
- [Radhika Toravi(rtoravi)](rtoravi@ncsu.edu) <br>
- [Rushikesh Deodhar(rdeodha)](rdeodha@ncsu.edu) <br>
- [Saurabh Nanda(snanda)](snanda2@ncsu.edu) <br>
				
## Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project.
- [https://streamlit.io/](https://streamlit.io/)
- [https://huggingface.co/](https://huggingface.co/)
- [https://shields.io/](https://shields.io/)
- [https://www.powtoon.com/](https://www.powtoon.com/)
- [https://www.heroku.com/](https://www.heroku.com/)
