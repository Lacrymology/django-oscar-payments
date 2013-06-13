# -*- coding: utf-8 -*-

"""
.. module:: oscar_payments.modules.payment.dummy.views
   :platform: Unix
   :synopsis: Views to collect and render

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from oscar_payments.modules.payment.base import views
from oscar_payments.modules.payment.dummy import forms

class CollectBillingInfo(views.BankcardBillcardMixin, views.BaseRootView):
    """
    Collect billing info and pass it on.
    """
    bankcard_form_class = forms.BankcardForm
    billing_address_form_class = forms.BillingAddressForm
