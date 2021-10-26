"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Scrivener
"""

# Import Libraries
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

class Summary:
    """
    A class used to generate summary text from the transcribed text provided.
    
    ...

    Attributes
    ----------
    transcribed_text : str
        text extracted from video
        
    Methods
    -------
    summarize_text:
        Generate the summary using the LSA summarization algorithm.
    """

    def __init__(self, transcribed_text):
        """
        Parameters
        ----------
        transcribed_text : str
            text extracted from video
        """
        self.transcribed_text = transcribed_text

    def summarize_text(self):
        """ 
        Generate summary for Youtube videos with Closed Captions
        """

        # initializing empty list
        summary_text = []
        # initialize a text parser taking in transcribed text, and setting language to english
        parser = PlaintextParser.from_string(self.transcribed_text, Tokenizer("english"))
        # initialize the summarizer object - you can use different summarization algorithms here
        # such has LexRank and Luhn
        summarizer = LsaSummarizer()
        # create a summary passing in the transcribed text and setting the number of sentences
        summary = summarizer(parser.document, 10)

        # loop through sentences turning them into strings and appending them to summary_text
        for sentences in summary:
            summary_text.append(str(sentences))

        # return summary_text to calling function
        return summary_text
