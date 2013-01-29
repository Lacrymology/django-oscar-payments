# -*- coding: utf-8 -*-

"""
.. module:: boilerplate.apps.store.modules.payment.dummy.app
   :platform: Unix
   :synopsis: oscar application for the dummy payment module

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from boilerplate.apps.store.modules.payment.base.app import PaymentModule
from boilerplate.apps.store.modules.payment.dummy import views

class DummyPaymentApplication(PaymentModule):
    module_name = 'dummy'
    verbose_name = _('Credit Cards')
    def get_urls(self):
        base_patterns = super(DummyPaymentApplication, self).get_urls()
        urlpatterns = patterns(
            '',
            url(r'^$', views.CollectBillingInfo.as_view(), name=self.get_root_url())
        )
        return urlpatterns + base_patterns

application = DummyPaymentApplication()
