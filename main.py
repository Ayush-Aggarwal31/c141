from flask import Flask, jsonify
import pandas as pd
movies_data = pd.read_csv('final.csv')
app = Flask(__name__)
# extracting important information from dataframe
all_movies=movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]
# variables to store data
liked_movies=[]
not_liked_movies=[]
did_not_watch_movies=[]
# method to fetch data from database
def movie_info():
  movie={
    "original_title":all_movies.iloc[0,0],
    "poster_link":all_movies.iloc[0,1],
    "release_date":all_movies.iloc[0,2],
    "duration":all_movies.iloc[0,3],
    "rating":all_movies.iloc[0,4],
  }
  return movie
# /movies api
@app.route("/movies")
def get_movie():
  moviedata=movie_info()
  return jsonify({
    "data":moviedata,
    "status":"success"
  })
# /like api
@app.route("/like")
def like_movies():
  global all_movies
  moviedata=movie_info()
  liked_movies.append(moviedata)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"success"
  })
@app.route("/liked")
def movie_likes():
  global liked_movies
  return jsonify({
    "data":liked_movies,
    'status':"success"
  })
# /dislike api
@app.route("/dislike")
def dislike_movies():
  global all_movies
  moviedata=movie_info()
  not_liked_movies.append(moviedata)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"success"
  })
# /did_not_watch api
@app.route("/notwatched")
def not_watched_movies():
  global all_movies
  moviedata=movie_info()
  did_not_watch_movies.append(moviedata)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"success"
  })
if __name__ == "__main__":
  app.run()