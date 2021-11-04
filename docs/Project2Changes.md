# The following changes have been made to Version 1.0 of Scrivener
***
## In the Version 2.0 of Scrivener the team has made significant changes to the code, documentation and have added more features that improves the overall funnctionality and usability of the original project.
***
### Better summarization and formatting
 1. We used sumy [sumylink](https://pypi.org/project/sumy/) which is a simple library and command line utility for extracting summary from HTML pages or plain texts. This helps us to create better summarizations of the transcripts as compared to previous version.
 2. Use of punctuator [punlink](https://pypi.org/project/punctuator/) helps to punctuate the YouTube transcript since by default, a lot of the closed captioning    has no punctuation. This makes it hard for any summarization technique to figure out where sentences start and end. It uses a bidirectional recurrent neural   network model with attention mechanism for restoring missing inter-word punctuation in unsegmented text.
 3. BLEU or the Bilingual Evaluation Understudy, is a score used to evaluate text generated for a suite of natural language processing tasks. To understand the summary's quality, we compare it against the original transcript using BLEU score. We can then validate this BLEU score in our testing component. This addresses the issue: [issue] (https://github.com/anshulp2912/scrivener/issues/32). 

### Sentiment Analysis
We have used MonkeyLearn API to perform Sentiment Analysis of the generated summary.

### Testing
The previous project did not have any test cases. In this version, we have added multiple test cases. We have added Automated Tests i.e Testcases are automatically executed each time a push is made or a pull request is merged. Automatic style checking through Pylint has been enabled on files.

### Addition of code coverage

***
