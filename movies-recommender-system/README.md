# Movie Recommendation System (TMDB Dataset)

A content based movie recommender system using cosine similarity

## Overview
This project is a content-based movie recommendation system built using machine learning techniques. It suggests movies similar to a selected title by analyzing patterns in movie metadata and computing similarity scores.

The system is deployed using Streamlit, providing an interactive user interface, and integrates with the TMDB API to dynamically fetch movie posters.

---

## Objectives
- Build a movie recommendation engine using real-world data  
- Apply similarity-based machine learning techniques  
- Develop an interactive web application for recommendations  
- Integrate external APIs for visualization  

---

## Methodology

### Data Processing
- Used the TMDB dataset from Kaggle  
- Cleaned and preprocessed movie metadata  
- Selected relevant features for similarity computation  

### Feature Engineering
- Combined key textual features (genres, keywords, cast)  
- Converted text into numerical vectors using vectorization techniques  

### Model Development
- Computed similarity scores between movies  
- Used cosine similarity to identify closest matches  
- Stored processed data and similarity matrix using pickle  

### Recommendation Logic
- Input: selected movie  
- Output: top 5 similar movies based on similarity score  

---

## Tech Stack

- Programming Language: Python  
- Libraries: Pandas, NumPy, Scikit-learn, Requests  
- Framework: Streamlit  
- API: TMDB API (for movie posters)  
- Tools: Jupyter Notebook, Git  

---

## Features
- Interactive UI built with Streamlit  
- Real-time movie recommendations  
- Displays movie posters using TMDB API  
- Efficient similarity-based recommendation system  

---

USE TMDB 5000 DATASET

https://drive.google.com/file/d/1Zu0DfjFlVKgYgEUU6RlHt-jHsBJL4B4S/view?usp=drive_link

https://drive.google.com/file/d/1W0dDlg79A2ETPesfrudt5Br-hJw7SY4W/view?usp=drive_link