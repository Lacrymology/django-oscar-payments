# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.utils.translation import ugettext_lazy as _
from boilerplate.apps.store.modules.payment.base.app import PaymentModule
from boilerplate.apps.store.modules.payment.paypal import views

class PaypalPaymentModule(PaymentModule):
    name = 'paypal'
    verbose_name = _('Paypal')
    root_view = views.PaypalRootView

    def get_urls(self):
        from paypal.express import urls
        base_urls = super(PaypalPaymentModule, self).get_urls()
        return urls.urlpatterns + base_urls

application = PaypalPaymentModule()
