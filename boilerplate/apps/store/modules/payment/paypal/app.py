# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from boilerplate.apps.store.modules.payment.base.app import PaymentModule

class PaypalPaymentModule(PaymentModule):
    module_name = 'paypal'
    verbose_name = _('Paypal')

    def get_urls(self):
        from paypal.express import urls
        from boilerplate.apps.store.modules.payment.paypal import views
        urlpatterns = patterns(
            '',
            url('^$', views.PaymentDetailsView.as_view(), name='paypal-index'),
            )
        return urlpatterns + urls.urlpatterns

application = PaypalPaymentModule()
