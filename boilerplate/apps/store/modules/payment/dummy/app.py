# -*- coding: utf-8 -*-

"""
.. module:: boilerplate.apps.store.modules.payment.dummy.app
   :platform: Unix
   :synopsis: oscar application for the dummy payment module

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.utils.translation import ugettext_lazy as _
from boilerplate.apps.store.modules.payment.base.app import PaymentModule

class DummyPaymentApplication(PaymentModule):
    module_name = 'dummy'
    verbose_name = _('Credit Cards')
    def get_urls(self):
        patterns = ('')
        return super(DummyPaymentApplication, self).get_urls()

application = DummyPaymentApplication()
