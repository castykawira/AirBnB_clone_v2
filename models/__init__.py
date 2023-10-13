#!/usr/bin/python3
"""
__init__.py - Initializes the models package
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
