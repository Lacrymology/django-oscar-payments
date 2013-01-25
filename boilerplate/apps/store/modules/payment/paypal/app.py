# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.utils.translation import ugettext_lazy as _
from boilerplate.apps.store.modules.payment.base.app import PaymentModule

class PaypalPaymentModule(PaymentModule):
    module_name = 'paypal'
    verbose_name = _('Paypal')

    def get_urls(self):
        from paypal.express import urls
        return urls.urlpatterns

application = PaypalPaymentModule()
