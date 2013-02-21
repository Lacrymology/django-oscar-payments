# -*- coding: utf-8 -*-

"""
.. module:: boilerplate.apps.store
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from boilerplate import try_import, project_name

def shop_app_module_name(appname):
    module_name = '%s.apps.store.apps.%s' % (project_name(), appname)
    module = try_import(module_name)
    if module is not None:
        return module_name
    module_name = 'boilerplate.apps.store.apps.%s' % appname
    module = try_import(module_name)
    if module is not None:
        return module_name

def import_shop_app(appname, submodule=''):
    module_name = shop_app_module_name(appname)
    if module_name is not None:
        if submodule:
            module_name = "%s.%s" % (module_name, submodule)
        return try_import(module_name)
