"""
@author: Scrivener
"""

from transformers import pipeline

class Summary:
    def __init__(self,transcribed_text):
        self.transcribed_text = transcribed_text
    
    def summarize_text(self):
        summarizer = pipeline('summarization', model="t5-base", tokenizer="t5-base")
        
        summary_text = []
        
        itrs = len(self.transcribed_text) // 1000
        for i in range(itrs+1):
            start = 1000 * i
            end = 1000 * (i + 1) 
            output = summarizer(self.transcribed_text[start:end])[0]['summary_text']
            summary_text.append(output)
        return summary_text 
