import os
import tempfile

from pymongo import MongoClient
import json

from swagger_server.models import Student

client = MongoClient("mongodb://localhost:27017")
db = client.local

collection = db.students

# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

def add(student=None):
    # queries = []
    # query = Query()
    # queries.append(query.first_name == student.first_name)
    # queries.append(query.last_name == student.last_name)
    # query = reduce(lambda a, b: a & b, queries)
    # res = student_db.search(query)

    # if res:
    #     return 'already exists', 409

    # doc_id = student_db.insert(student.to_dict())
    # student.student_id = doc_id

    _student = student

    collection.insert_one(student.to_str())

    __student = student.to_str()

    # student_object = collection.insert_one(student.to_str())
    # return student_object.inserted_id
    return 0

def get_by_id(student_id=None, subject=None):
    # # student = student_db.get(doc_id=int(student_id))
    # db.find({id()})
    # if not student:
    #     return 'not found', 404
    # student['student_id'] = student_id
    # return student
    return None

def delete(student_id=None):
    # student = student_db.get(doc_id=int(student_id))
    # if not student:
    #     return 'not found', 404
    # student_db.remove(doc_ids=[int(student_id)])
    # return student_id
    return None