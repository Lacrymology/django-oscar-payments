# -*- coding: utf-8 -*-

"""
.. module:: boilerplate.apps.store.apps.checkout.app
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from collections import OrderedDict
import logging
from django.conf import settings
from django.conf.urls import url, include, patterns
from oscar.apps.checkout import app
from boilerplate import try_import
from boilerplate.apps.store.apps.checkout.views import PaymentDetailsView

class CheckoutApplication(app.CheckoutApplication):
    payment_details_view = PaymentDetailsView

    def __init__(self, *args, **kwargs):
        super(CheckoutApplication, self).__init__(*args, **kwargs)
        self.log = logging.getLogger("%s.%s" % (self.__class__.__module__,
                                                self.__class__.__name__))
        #
        self.modules = None

    def get_urls(self):
        base_urls = super(CheckoutApplication, self).get_urls()
        args = []
        for module in self.get_modules().values():
            args.append(url(module['url'], include(module['app'].urls)))
        return patterns('', *args) + base_urls

    def get_modules(self):
        """
        Populate and return registered payment modules

        :return: An OrderedDict like { module_name -> { 'url': url,
                                                        'app': application }}
        """
        if self.modules is None:
            self.modules = OrderedDict()
            for root, appname in settings.BOILER_PAYMENT_MODULES:
                app = try_import(appname + '.app')
                if app is not None:
                    application = app.application
                    self.modules[application.module_name] = {'url': root,
                                                             'app': application}
                else:
                    self.log.warning("Oscar misconfigured! %s.app cannot be "
                                     "imported", appname)

        return self.modules



application = CheckoutApplication()
