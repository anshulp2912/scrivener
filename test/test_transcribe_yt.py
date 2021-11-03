import pytest

from youtube_transcript_api._transcripts import Transcript
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
from urllib.parse import urlparse
from urllib.parse import parse_qs
import nltk

from source.main.transcribe_yt import TranscribeYtVideo
from source.main.punctuation import Punctuation

# Khan Academy's video on agriculture
# contains transcripts
# contains closed captions
video_one_url = "https://www.youtube.com/watch?v=JvBHwVpBCwM"

# Lecture 38 — Bloom Filters | Mining of Massive Datasets | Stanford University
# contains no transcripts
video_two_url = "https://www.youtube.com/watch?v=qBTdukbzc78"

@pytest.mark.parametrize('youtube_url, test_index', [
    (video_one_url, 1),
    (video_two_url, 2)
])
def test_check_yt_cc(youtube_url, test_index):
    transc_obj = TranscribeYtVideo(youtube_url)
    transcript = transc_obj.check_yt_cc()
    if test_index == 1:
        # Check for type
        assert isinstance(transcript, Transcript)
        # Check for language correctness
        assert transcript.language == "English - Default"

        # Check if video ID is the same
        parsed = urlparse(youtube_url)
        assert transcript.video_id == parse_qs(parsed.query)["v"][0]
    elif test_index == 2:
        assert transcript == None

def fetch_transcript(yt_id):
    full_text = YouTubeTranscriptApi.get_transcript(yt_id)
    transcript_text = str()
    for rec in full_text:
        transcript_text += " " + rec["text"]
    punctuated_transcription = Punctuation.add_punctuation_transcript(
            transcript_text
    )
    return punctuated_transcription

@pytest.mark.parametrize('youtube_url, test_index', [
    (video_one_url, 1),
    (video_two_url, 2)
])
def test_transcribe_yt_video_w_cc(youtube_url, test_index):
    transc_obj = TranscribeYtVideo(youtube_url)
    assert transc_obj.summary == ""
    if test_index == 1:
        N = 10
        transc_obj.transcribe_yt_video_w_cc()
        # checks if the summary is still a string type
        assert isinstance(transc_obj.summary, str)
        # checks if summary has atleast N characters
        assert len(transc_obj.summary) > N

        # calculates the BLEU score
        full_text = fetch_transcript(transc_obj.yt_id)
        full_text_tokens = nltk.tokenize.word_tokenize(full_text)
        summary_tokens = nltk.tokenize.word_tokenize(transc_obj.summary)
        score = nltk.translate.bleu_score.sentence_bleu(
            [full_text_tokens], 
            summary_tokens, 
            weights=(1,)
        )
        # print(f"BLEU score for {youtube_url} is {score}", flush=True)
        assert score > 0
    elif test_index == 2:
        try:
            transc_obj.transcribe_yt_video_w_cc()
        except Exception as e:
            assert isinstance(e, TranscriptsDisabled)

@pytest.mark.parametrize('youtube_url, test_index', [
    (video_one_url, 1),
    (video_two_url, 2)
])
def test_transcribe_yt_video(youtube_url, test_index):
    transc_obj = TranscribeYtVideo(youtube_url)
    assert transc_obj.summary == str()

    transc_obj.transcribe_yt_video()
    N = 10
    assert transc_obj.summary != str()
    assert len(transc_obj.summary) > N
