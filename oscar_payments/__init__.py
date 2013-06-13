# -*- coding: utf-8 -*-

"""
.. module:: oscar_payments
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
import importlib
from django.conf import settings

def try_import(module):
    try:
        return importlib.import_module(module)
    except ImportError:
        return None

def shop_app_module_name(appname):
    module_name = '%s.%s' % (settings.OSCAR_OVERRIDES_PACKAGE,
                                             appname)
    module = try_import(module_name)
    if module is not None:
        return module_name
    module_name = 'oscar_payments.apps.%s' % appname
    module = try_import(module_name)
    if module is not None:
        return module_name

def import_shop_app(appname, submodule=''):
    module_name = shop_app_module_name(appname)
    if module_name is not None:
        if submodule:
            module_name = "%s.%s" % (module_name, submodule)
        return try_import(module_name)
