# Sentiment Analysis using TextBlob (Dockerized)

Project Description
This project implements sentiment analysis on textual data using TextBlob, a Python-based Natural Language Processing (NLP) library.  
Each input sentence is analyzed to determine its polarity score and classified as Positive, Negative, or Neutral.

The application is containerized using Docker ensuring consistent execution across different systems.

Key Features:
-Sentiment classification using TextBlob
-Polarity score calculation for input text
-Simple and beginner-friendly Python implementation
-Fully Dockerized application
-No manual dependency installation required

Technology Stack:
-Programming Language: Python
-NLP Library: TextBlob
-Containerization: Docker
-Development Environment: WSL 2 (Ubuntu on Windows 11)
-Platform Compatibility: Windows

Project Structure:
sentiment-analysis-textblob/
│── app.py
│── requirements.txt
│── Dockerfile
│── README.md

## Docker Installation

Install Docker on Windows
-Download Docker Desktop for Windows from the official Docker website.
-Install Docker Desktop and enable WSL 2 integration during setup.
-Restart the system if required.
-Verify installation:
docker --version

How It Works:

-The user provides a text input.
-TextBlob analyzes the text and calculates a polarity score.
-Based on the polarity value, the sentiment is classified as:

  Positive

  Negative

  Neutral

## Sample Output

Text: I love this product! It's amazing.
Polarity: 0.8
Sentiment: Positive

Installation and Execution:
Run the Application using Docker

docker build -t sentiment-analysis-textblob
docker run -it sentiment-analysis-textblob

Learning Outcomes:
-Understanding sentiment polarity and subjectivity in NLP
-Hands-on experience with TextBlob
-Writing Dockerfiles for Python applications
-Running containerized applications using Docker
