import pymongo
import pprint

client = pymongo.MongoClient(
    "mongodb+srv://admin:FSvCHTGpm0R5JXzJ@cluster0.zfi3y.mongodb.net/test?retryWrites=true&w=majority")


with client:
    db = client.test
    movie_initial = db.get_collection('movies_initial')
    # pprint.pprint(movie_initial.find_one({'imdbID':1}))

    UK_movies = []
    for movie in movie_initial.find({'country': 'UK'}):
        UK_movies.append(movie)
    print(len(UK_movies))

    # nb entries
    # print(movie_initial.count_documents({}))


# movie_initial = db.get_collection('movie_initial')
# print(movie_initial)
