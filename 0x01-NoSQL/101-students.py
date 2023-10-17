#!/usr/bin/env python3
"""
Task 14: a python function
"""


def top_students(mongo_collection):
    """
    Prints all students in a collection sorted by average score.
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
