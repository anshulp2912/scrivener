"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Scrivener
"""

# Import Libraries
from main.summarize import Summary
import pytube
import os
from youtube_transcript_api import YouTubeTranscriptApi
from main.transcribe import TranscribeVideo

class TranscribeYtVideo:
    """
    A class used to summarize video link from Youtube
    
    ...

    Attributes
    ----------
    youtube_url: str
        a valid youtube video link
    yt_id: str
        youtube id of the youtube video link
    summary: str
        summary of the video
        
    Methods
    -------
    check_yt_cc:
        Checks if the youtube video has captions or not
    transcribe_yt_video:
        Caller function for methods in the class
    transcribe_yt_video_w_cc:
        Generate summary for Youtube videos with Closed Captions
    transcribe_yt_video_wo_cc:
        Generate summary for Youtube videos without Closed Captions
    """
    
    def __init__(self,youtube_url):
        """
        Parameters
        ----------
        youtube_url : str
            link of youtube video
        """
        self.youtube_url = youtube_url
        self.yt_id = self.youtube_url.split('=')[1]
        self.summary = ''
        
    def check_yt_cc(self):
        """Checks if the youtube video has captions or not

        Raises
        ------
        Exception
            If transcript cannot be extracted.
        """
        transcript = None
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(self.yt_id)
            transcript = transcript_list.find_transcript(['en'])
        except Exception as e:
            print(e)
        return transcript
            
    
    def transcribe_yt_video(self):
        """ 
        Caller function for methods in the class
        """
        check_cc = self.check_yt_cc()
        # If captions are not present
        if check_cc is None:
            self.transcribe_yt_video_wo_cc()
        # Captions are present
        else:
            self.transcribe_yt_video_w_cc()
        # return summary
        return self.summary
        
    def transcribe_yt_video_w_cc(self):
        """ 
        Generate summary for Youtube videos with Closed Captions
        """
        # Get transcript from youtube video
        transcript_json = YouTubeTranscriptApi.get_transcript(self.yt_id)
        transcript_text = ''
        # Extract the captions
        for rec in transcript_json:
            transcript_text += ' ' + rec['text']
        # Call the summarization script
        transcript_summary = Summary(transcript_text)
        summary = transcript_summary.summarize_text()
        for lines in summary:
            print(lines)
        # Join list with ' '
        self.summary = '\n'.join(summary)
     
    def transcribe_yt_video_wo_cc(self):
        """ 
        Generate summary for Youtube videos without Closed Captions
        """
        # Download the youtube video
        youtube = pytube.YouTube(self.youtube_url)
        dwnld_video = youtube.streams.get_lowest_resolution()
        #Check if temp directory available
        if not os.path.exists(os.getcwd()+"/temp"):
            #Create temp directory
            os.mkdir('temp')
        dwnld_video.download(filename='temp.mp4',output_path=os.getcwd())
        # Get transcript of videos without caption
        transcribed_video = TranscribeVideo()
        # Call the summarization script
        self.summary = transcribed_video.transcribe_video(os.path.join(os.getcwd(), 'temp.mp4'))
