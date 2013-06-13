# -*- coding: utf-8 -*-

"""
.. module:: oscar_payments.modules.payment.dummy.app
   :platform: Unix
   :synopsis: oscar application for the dummy payment module

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from oscar_payments.modules.payment.base.app import PaymentModule
from oscar_payments.modules.payment.dummy import views

class DummyPaymentApplication(PaymentModule):
    name = 'dummy'
    verbose_name = _('Credit Cards')
    root_view = views.CollectBillingInfo

application = DummyPaymentApplication()
