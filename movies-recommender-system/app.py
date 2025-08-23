import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    try:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6eaaa504e27a26dd7fbe9176faf2add5&language=en-US')
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except (requests.RequestException, KeyError) as e:
        # Log the error for debugging (optional, can be removed)
        # st.warning(f"Failed to fetch poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_posters
    except IndexError:
        st.error(f"Movie '{movie}' not found.")
        return [], []

try:
    movies_list = pickle.load(open('movies.pkl', 'rb'))
    movies = pd.DataFrame(movies_list)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Data files not found.")
    st.stop()

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    if names:
        col1, col2, col3, col4, col5 = st.columns(5)
        columns = [col1, col2, col3, col4, col5]
        for i, col in enumerate(columns):
            with col:
                # Only display if the index exists to avoid IndexError
                if i < len(names):
                    st.text(names[i])
                    st.image(posters[i])
                else:
                    st.text("No recommendation")
                    st.image("https://via.placeholder.com/500x750?text=No+Data")