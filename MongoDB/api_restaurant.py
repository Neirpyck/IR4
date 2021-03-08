from aiohttp import web
from statistics import mean
from datetime import datetime
import json
import jsonpickle

import pymongo
from flask import Flask, jsonify, request


app = Flask(__name__)

client = pymongo.MongoClient(
    "mongodb+srv://admin:FSvCHTGpm0R5JXzJ@cluster0.zfi3y.mongodb.net/sample_restaurants?retryWrites=true&w=majority")

db = client.sample_restaurants
restaurants = db.get_collection('restaurants')


class Address():
    def __init__(self, building, street, zipcode):
        self.building = building
        self.street = street
        self.zipcode = zipcode

    def __repr__(self):
        return f'{self.building} {self.street}, NY {self.zipcode}'


class Grade():
    def __init__(self, date, grade, score):
        self.date = date
        self.grade = grade
        self.score = score

    def __repr__(self):
        return f'date: {self.date}, grade: {self.grade}, score: {self.score}'


class Restaurant:
    def __init__(self, address, borough, cuisine, name, grades, restaurant_id):
        self.address = Address(
            building=address['building'], street=address['street'], zipcode=address['zipcode'])
        self.borough = borough
        self.cuisine = cuisine
        self.name = name
        self.grades = [Grade(date=grade['date'], grade=grade['grade'],
                             score=grade['score']) for grade in grades]
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return f'{self.name} is offering {self.cuisine} cuisine at the {self.address}, in the {self.borough} borough.'

    def avg_score(self):
        """ return the mean score of all the score of the restaurant """
        return mean([score.score for score in self.grades])

    def avg_grade(self):
        """ return the mean score of all the grade of the restaurant """
        return chr(round(mean([ord(score.grade) for score in self.grades])))

    def json_from_grades(self):
        """ Create a json array from the grades of the restaurant """
        return [{'date': str(grade.date),
                 'grade': grade.grade,
                 'score': grade.score}
                for grade in self.grades]

    def add_grade(self, new_grade, new_score):
        """ add a grade to the restaurant and update its entry in the database"""
        self.grades.append(Grade(grade=new_grade, score=new_score,
                                 date=now.strftime('%Y-%m-%dT%H:%M:%S.Z')))
        restaurants.update_one({"restaurant_id": self.restaurant_id},
                               {"$set": {"grades": json_from_grades(self.grades)}}, upsert=False)


def class_from_json(json):
    """ Create a Restaurant object from the json received from the database"""
    return Restaurant(address=json['address'],
                      borough=json['borough'],
                      cuisine=json['cuisine'],
                      name=json['name'],
                      grades=json['grades'],
                      restaurant_id=json['restaurant_id']
                      )


def find_restaurant(args=None, **kwargs):
    ''' find a restaurant using the arguments passed
        ex: cuisine, borough, name
        input: key=value
        output: Restaurant[]
    '''
    if args:
        return [class_from_json(resto) for resto in restaurants.find(args)]
    kwarg_search = {key: value for key, value in kwargs.items() if key != None}
    return [class_from_json(resto) for resto in restaurants.find(kwarg_search)]


#@app.route('/', methods=['GET'])
#def query():
#    if request.args:
#        req = request.args.to_dict()
#        # return " ".join(f'{k}: {v}' for k, v in req.items())
#        res = restaurants.find_one({'cuisine':'Chinese'})
#        print(res)
#        return json.dumps(res, default=str)
#    return "No query"

@app.route('/', methods=['GET'])
def query():
    if request.args:                                          
        req = request.args.to_dict()
        print(req)
        res = find_restaurant(req)
        return json.dumps(res, default=str)
    return "No query"

if __name__ == '__main__':
    app.run()

