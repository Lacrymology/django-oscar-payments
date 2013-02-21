# -*- coding: utf-8 -*-

"""
.. module:: boilerplate
   :platform: Unix
   :synopsis: boilerplate root module

"""
from django.utils import importlib

def try_import(module):
    try:
        return importlib.import_module(module)
    except ImportError:
        return None

