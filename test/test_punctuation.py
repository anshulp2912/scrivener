import pytest
from source.main.punctuation import Punctuation
import string
import re

# Khan Academy's video on agriculture
# contains transcripts
# contains closed captions
video_one_url = "https://www.youtube.com/watch?v=JvBHwVpBCwM"

# Lecture 38 — Bloom Filters | Mining of Massive Datasets | Stanford University
# contains no transcripts
video_two_url = "https://www.youtube.com/watch?v=qBTdukbzc78"

test_sentence = """
A computer is a machine that can be programmed to carry 
out sequences of arithmetic or logical operations automatically. 
Modern computers can perform generic sets of operations known 
as programs. These programs enable computers to perform a wide 
range of tasks. A computer system is a "complete" computer that 
includes the hardware, operating system (main software), and 
peripheral equipment needed and used for "full" operation. This 
term may also refer to a group of computers that are linked and 
function together, such as a computer network or computer cluster.
"""

@pytest.mark.parametrize('test_sentence', [
    (test_sentence),
])
def test_add_punctuation_transcript(test_sentence):
    # Removing punctuations to create a test example
    translation = {punct: "" for punct in string.punctuation}
    sentence_no_punct = test_sentence.translate(str.maketrans(translation))
    sentence_no_punct = sentence_no_punct.lower().strip()

    punct_text = Punctuation.add_punctuation_transcript(sentence_no_punct)
    assert len(re.findall("["+string.punctuation+"]", punct_text)) > 0
