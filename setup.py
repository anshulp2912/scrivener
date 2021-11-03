from setuptools import setup

setup(
    name='Scrivener',
    version='1.4',
    author='scrivener',
    author_email='rdeodha@ncsu.edu',
    license='MIT',
    url='https://github.com/TommasU/scrivener/',

    install_requires=open('requirements.txt').readlines(),

    description='Video transcript summarizer',
    long_description="""\
      Scrivener is a video transcript summarizer for Youtube videos.      
    """,
    keywords=['python', 'video summarizer', 'youtube', 'transcript'],
    classifiers=[
          'License :: OSI Approved :: MIT License',
          "Programming Language :: Python",
    ],

    packages=["source"],
)
