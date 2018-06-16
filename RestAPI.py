
"""
REST Interface in python that Provides CRUD operations on MonogoDB collection.

The script has been developed using python 3.6.0

The script assumes that you have up and running mongoDB instance running on the default port in
your local system. Further, the mongoDB has a database named "school" and a collection named "scores"

Please find the dump of the collection in the folder "School".

You may use this dump to import the collection into you local database "school". Here is an example,

mongorestore --collection scores  --db school "school/scores.bson"

"""

from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "school"
mongo = PyMongo(app, config_prefix='MONGO')
APP_URL = "http://127.0.0.1:5000"

class school(Resource):

    ## Create a new record into a MonfoDB Collection
    def post(self):
     data=request.get_json()
     if not data:
         data={"response":"ERROR"}
         return jsonify(data)
     else:
        student_id=data.get('student_id')
        if student_id:
            if mongo.db.scores.find_one({"student_id": int(student_id)}):
                return {"response":"student already exists"}
            else:
                mongo.db.scores.insert(data)
        else:
            return {"response": "student_id number missing"}

    ## Reading the data from MongoDB Collections
    def get(self,student_id=None):
        data=[]

        if student_id:
            print("Student_id", student_id)
            scores = mongo.db.scores.find_one({"student_id": int(student_id)}, {"_id": 0})
            if scores:
                print("Scores =",scores)
                return jsonify({"status": "ok", "data": scores})
            else:
                return {"response": "no record found for student_id {}".format(student_id)}

        else:
            ## if you dont specify he student_id, it will show first 10 records
            cursor = mongo.db.scores.find({}, {"_id": 0}).limit(10)

            for student in cursor:
                print (student)
                data.append(student)

            return jsonify({"response": data})


    ## Update the collection based on the student_id parameter
    def put(self, student_id):
        data = request.get_json()
        mongo.db.scores.update({'student_id': int(student_id)}, {'$set': data})
        return redirect(url_for("school"))

    ## Delete the records of the studentid
    def delete(self, student_id):
        mongo.db.scores.remove({'student_id': int(student_id)})
        return redirect(url_for("school"))


class Index(Resource):
    def get(self):
        return redirect(url_for("school"))

api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(school, "/api", endpoint="school")
api.add_resource(school, "/api/<student_id>", endpoint="student_id")

if __name__ == "__main__":
    app.run(debug=True)
