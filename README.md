# Overview

This program's main function is to gage sentiment of a Youtube video based on the comments using Natural Language processing. It uses Python for webscraping, and Java for the language processing.

I am writing this to gain familiarity with Java and have a first look at concepts in NLP.
> Note: I did **not** write the code for natural language processing, that was imported and I named it to show that. I wrote the files `comments_scraper.py` and `YoutubeSentiment.java` which pull and prepare the comments for processing.

Here is a video with a quick overview of what I learned and a quick demonstration of the code, along with any issues that I had:
[Software Demonstration](https://youtu.be/vZUFXsFb078)

# Development Environment
I wrote the program using VS Code. The only Java library I imported for my Java code was Json-Simple. Json-Simple is an old library, but I was able to download it from a Google archive. For my Python code, I used Google's API. To use it you will need to generate you own key and put it in `KEYS.py`.

* [Json-Simple Archive](https://code.google.com/archive/p/json-simple/)
* [Google' API](https://developers.google.com/docs/api/quickstart/python)

The code I imported came from a tutorial written by Yuli Vasiliev on Oracle's blog. The libraries used in the imported code came from the Stanford NLP Group.

* [Vasiliev's Tutorial and Code](https://blogs.oracle.com/javamagazine/post/java-sentiment-analysis-stanford-corenlp)
* [Stanford Core NLP Library](https://stanfordnlp.github.io/CoreNLP/)

# Useful Websites
For what I need to do, w3Schools.com was the most helpful. It had plenty of clear descriptions on how Java implements basic functions such as for loops and try/catch statements.
It took a surprisingly long time to figure out how to import libraries in Java.
* [w3Schools.com](https://www.w3schools.com/java/)

# Future Work
There are plenty of problems I need to fix with this project since it was my first time using Java.
* The program does not pace itself, so I couldn't get it to work with more than 200 comments. I need to add a buffer so it can handle more without crashing.
* Implement `comment_scraper` in Java instead of Python (I would not have to write a json file either, though I may wite one anyways if the program needs to process a lot of comments)
* Add function to clean data before processing (The NLP code rates most videos as a 1 out of 5, hopefully that will be fixed when the data is clean)
