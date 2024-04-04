# Question:
#     You are to develop a movie recommendation system. You have dictionary named as movieswhere each key is a movie title and the value is a list of genres(e.g, "action", "comedy", "thriller"). You also have a user's favorite genres stored in a list of user genres. 

# Create a function that recommends movies(movies, user genres) that takes the movies dictionary and the user genres list as input and returns a list of movie titles recommended for the user. The recommendation logic should prioritize movies that share the most genres with user's favorites.  


# Answer:

def Add_movies(movies):
    name = input('Insert a movie Name:')
    genre = input('Insert a Genere:')
    movies[name] = genre

def my_suggestions(user_genres, movies):
    recommendations = []
    max_shared_genres = 0
    for movie, genres in movies.items():
        shared_genres = len(set(genres) & set(user_genres))
        if shared_genres > max_shared_genres:
            recommendations = [movie]
            max_shared_genres = shared_genres
        elif shared_genres == max_shared_genres:
            recommendations.append(movie)
    return recommendations

movies = {}

while True:
    action = input('Choose "add" to add a movie, "Suggestion" to get recommendations, or "exit" to exit: ')
    if action == 'add':
        Add_movies(movies)
    elif action == 'Suggestion':
        user_genres = input('Enter your favorite genres separated by commas: ').split(',')
        recomm_list = my_suggestions(user_genres, movies)
        print(recomm_list)
    elif action == 'exit':
        break
    else:
        print("Enter Valid Keyword")
