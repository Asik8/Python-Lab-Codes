# 2(a):

# a = input("Enter a sentence: Object Oriented Programming: ")
# count = 0

# for c in a:
#     if c.lower()=='a' or c.lower()=='e' or c.lower()=='i' or c.lower()=='o' or c.lower()=='u':
#         count += 1

# print(f"The number of cowels in the sentense is {count}")


# 2(b):

# books = int(input("Enter the number of Books: "))
# i = 1
# total_price = 0
# while(i<=books):
#     price = int(input(f"Price of book-{i}: "))
#     total_price += price
#     i+=1

# print(f"Total Cost: {total_price}tk")
# if(books<=3):
#     print(f"Total Payable Cost: {total_price}tk\n(No Discount available for 1 to 3 books)")
# elif(books>3 and books<=10):
#     total_price -= int(total_price*0.1)
#     print(f"Total Payable Cost: {total_price}tk\n(10% Discount applied for Purchasing 4 to 10 books)")
# elif(books>10):
#     total_price -= int(total_price*0.2)
#     print(f"Total Payable Cost: {total_price}tk\n(20% Discount applied for Purchasing more than 10 books)")

# 2(c):

# def Add_movies(movies):
#     name = input('Insert a movie Name:')
#     genre = input('Insert a Genere:')
#     movies[name] = genre

# def my_suggestions(user_genres, movies):
#     recommendations = []
#     max_shared_genres = 0
#     for movie, genres in movies.items():
#         shared_genres = len(set(genres) & set(user_genres))
#         if shared_genres > max_shared_genres:
#             recommendations = [movie]
#             max_shared_genres = shared_genres
#         elif shared_genres == max_shared_genres:
#             recommendations.append(movie)
#     return recommendations

# movies = {}

# while True:
#     action = input('Choose "add" to add a movie, "Suggestion" to get recommendations, or "exit" to exit: ')
#     if action == 'add':
#         Add_movies(movies)
#     elif action == 'Suggestion':
#         user_genres = input('Enter your favorite genres separated by commas: ').split(',')
#         recomm_list = my_suggestions(user_genres, movies)
#         print(recomm_list)
#     elif action == 'exit':
#         break
#     else:
#         print("Enter Valid Keyword")

#Class Encap:

class Encap:
    def __init__(self):
        # Protected Member
        self._a = 2
        # Private Member
        self.__b = 5
 