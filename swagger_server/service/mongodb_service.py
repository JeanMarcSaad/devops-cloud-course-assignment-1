import os
import tempfile

from pymongo import MongoClient
from bson.objectid import ObjectId

# from swagger_server import util
# from swagger_server.models import Student
# import json

client = MongoClient(os.environ['MONGO_URI'])
db = client.local
collection = db.students

def add(student=None):
    _student = collection.find_one({'student_id': student.student_id})

    if _student:
        return 'already exists', 409

    student_dict = student.to_dict()
    student_entry = collection.insert_one(student_dict)

    if student_entry.inserted_id:
        return student.student_id

    return 'internal error', 500

def get_by_id(student_id=None, subject=None):
    _student = collection.find_one({'student_id': student_id})
    if not _student:
        return 'not found', 404
    _student['_id'] = str(_student['_id'])
    return _student

def delete(student_id=None):
    _student = collection.find_one({'student_id': student_id})
    if not _student:
        return 'not found', 404
    collection.delete_one(({'student_id': student_id}))
    return student_id