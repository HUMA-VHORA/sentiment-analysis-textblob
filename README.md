# Sentiment Analysis using TextBlob (Dockerized)

Project Overview:
This project performs sentiment analysis on text data using TextBlob, a Python Natural Language Processing (NLP) library.  
Each input sentence is analyzed and classified as Positive, Negative, or Neutral based on polarity.

The project is containerized using Docker, enabling it to run on any system with a single command.

Features:
Sentiment classification using TextBlob
Polarity score calculation for each sentence
Beginner-friendly Python code
Fully Dockerized, no manual dependency installation required

Technology Stack:
Programming Language: Python
NLP Library: TextBlob
Containerization: Docker
Development Environment: WSL 2 (Ubuntu on Windows 11)
Platform Compatibility: Windows

Project Structure:
sentiment-analysis-textblob/
│── app.py
│── requirements.txt
│── Dockerfile
│── README.md

Sample Output:
Text: I love this product! It's amazing.
Polarity: 0.8
Sentiment: Positive

Learning Outcomes:
Understanding sentiment polarity and subjectivity
Hands-on NLP experience using TextBlob
Writing Dockerfiles for Python projects
Running applications using Docker containers
