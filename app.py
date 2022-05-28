import streamlit as stream
import pickle
import pandas as pd
import requests
# Set Page Layout and Title
stream.set_page_config(page_title="Movie Recommender Engine",layout="wide")

# Fetch Movie Posters Through API
def posters_fetching(movie_id):
     api_response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c240287ad8107743a60dca67d0a05d07&language=en-US'.format(movie_id))
     posters_data = api_response.json()
     return "https://image.tmdb.org/t/p/w500/" + posters_data['poster_path']

# Movie Recommender Function
def movie_recommender(movie):
     movieIndex = movies[movies['title'] == movie].index[0]
     distances = similar[movieIndex]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
     list_of_moive = []
     recommend_movies_posters_data = []
     for i in movies_list:
          movie_id = movies.iloc[i[0]].movie_id
          list_of_moive.append(movies.iloc[i[0]].title)
          recommend_movies_posters_data.append(posters_fetching(movie_id))
     return list_of_moive,recommend_movies_posters_data

# Load Movie Dictionary File
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# Find Similarity
similar = pickle.load(open('similarity.pkl','rb'))

# Body of The Page
stream.title('Movie Recommender Engine ')
selected_movies_name = stream.selectbox('Select Any Movie or Cick in Seclect Box and Type Movie Name',movies['title'].values)
if stream.button('Recommend'):
     stream.header('Top 10 Recommended Movies')
     stream.write("##")
     # Show The Recommended Movie in Columns Format
     movies_names, movies_posters = movie_recommender(selected_movies_name)
     col1, col2, col3,col4,col5 = stream.columns(5)

     with col1:
          stream.image(movies_posters[0])
          stream.markdown(movies_names[0])
     with col2:
          stream.image(movies_posters[1])
          stream.markdown(movies_names[1])
     with col3:
          stream.image(movies_posters[2])
          stream.markdown(movies_names[2])
     with col4:
          stream.image(movies_posters[3])
          stream.markdown(movies_names[3])
     with col5:
          stream.image(movies_posters[4])
          stream.markdown(movies_names[4])
     stream.write("##")
     col6,col7,col8,col9,col10 = stream.columns(5)
     with col6:
          stream.image(movies_posters[5])
          stream.markdown(movies_names[5])
     with col7:
          stream.image(movies_posters[6])
          stream.markdown(movies_names[6])
     with col8:
          stream.image(movies_posters[7])
          stream.markdown(movies_names[7])
     with col9:
          stream.image(movies_posters[8])
          stream.markdown(movies_names[8])
     with col10:
          stream.image(movies_posters[9])
          stream.markdown(movies_names[9])