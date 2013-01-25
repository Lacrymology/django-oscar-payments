# -*- coding: utf-8 -*-

"""
.. module:: boilerplate.apps.store.modules.payment.dummy.app
   :platform: Unix
   :synopsis: oscar application for the dummy payment module

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from boilerplate.apps.store.modules.payment.base.app import PaymentModule

class DummyPaymentApplication(PaymentModule):
    def get_urls(self):
        patterns = ('')
        return super(DummyPaymentApplication, self).get_urls()

application = DummyPaymentApplication()
