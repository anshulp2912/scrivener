import os
try:
    # hack: Unfortunately Heroku uses below file and it conflicts with the Punctuator package
    # as suggested here: https://github.com/chrisspen/punctuator2/issues/3 removing the file
    os.remove('.heroku/python/bin/punctuator.py')
except:
    print("punctuator.py not found in: " + os.getcwd())
from punctuator import Punctuator
from pathlib import Path

import shutil
import wget

class Punctuation:
    """
    A class used to add punctuation to transcripts

    ...

    Attributes
    ----------
    punct_model: object
        a ML model for adding puctuation to strings

    Methods
    -------
    add_punctuation_transcript:
        Adds punctuation to string
    """

    def __init__(self):
        """
        Parameters
        ----------
        youtube_url : str
            link of youtube video
        """

    @staticmethod
    def add_punctuation_transcript(transcription):
        """
        Using the generated transcript, add punctuation
        """
        def check_for_full_model():
            # Check if ML model files have been combined, if not combine them
            # This needs to be done because the full file is greater than 100mb
            # and GitHub does not allow files larger than 100mb to be pushed
            first_file = os.path.abspath('source/punct_model_part1.pcl')
            second_file = os.path.abspath('source/punct_model_part2.pcl')
            third_file = os.path.abspath('source/punct_model_part3.pcl')
            new_file = os.path.abspath('source/punct_model_full.pcl')

            if not os.path.exists(new_file):
                print("Creating punct_model_full.pcl file for ML model...")

                # Storing these models in github causes an issue with the Heroku deployment and exceeds 500 MB (it is 618 MB)
                # slug/payload limit. Therefore, using this alternative to get it from Github during runtime.
                if not os.path.exists(first_file):
                    print("Downloading punct_model_part1.pcl file for ML model...")
                    url1 = 'https://github.com/SN-18/scrivener/raw/developer/source/punct_model_part1.pcl'
                    filename = wget.download(url1, out='source/punct_model_part1.pcl')
                    print("\nDownloaded file: " + filename)

                if not os.path.exists(second_file):
                    print("Downloading punct_model_part2.pcl file for ML model...")
                    url2 = 'https://github.com/SN-18/scrivener/raw/developer/source/punct_model_part2.pcl'
                    filename = wget.download(url2, out='source/punct_model_part2.pcl')
                    print("\nDownloaded file: " + filename)

                if not os.path.exists(third_file):
                    print("Downloading punct_model_part3.pcl file for ML model...")
                    url3 = 'https://github.com/SN-18/scrivener/raw/developer/source/punct_model_part3.pcl'
                    filename = wget.download(url3, out='source/punct_model_part3.pcl')
                    print("\nDownloaded file: " + filename)

                with open(new_file, "wb") as wfd:
                    for f in [first_file, second_file, third_file]:
                        with open(f, "rb") as fd:
                            shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)

        check_for_full_model()
        # initialize the punctuator ML model
        # cwd = Path.cwd()
        # template = "./source/punct_model_full.pcl"
        # file_path = (cwd / template).resolve()
        # print(cwd, flush=True)
        punct_model = Punctuator(os.path.abspath("source/punct_model_full.pcl"))

        # Add punctuation to text
        punct_text = punct_model.punctuate(transcription)

        # replace punctuation errors, sometimes ML model will double up on punctuation, replace it such that there is
        # only one punctuation which is correct
        punct_text = (
            punct_text.replace(",,", ",")
            .replace("!,", "!")
            .replace(".,", ".")
            .replace("?,", "?")
            .replace(",.", ",")
            .replace("!.", "!")
            .replace("..", ".")
            .replace("?.", "?")
            .replace('",', ',"')
            .replace('".', '."')
            .replace('"!', '!"')
            .replace('"?', '?"')
        )

        return punct_text
