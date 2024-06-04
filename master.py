#!/usr/bin/python3
"""HbnB Classes Draft"""
import datetime
import uuid


class Master():
    """class defining instance creation and update datetimes and uuids"""
    def creation(self):
        """instance creation datetime"""
        return datetime.datetime.now()

    def updated(self):
        """instance updated datetime"""
        return datetime.datetime.now()

    def uniqueid(self):
        """assign universal unique id to instance"""
        return uuid.uuid4()
