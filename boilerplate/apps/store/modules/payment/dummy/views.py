# -*- coding: utf-8 -*-

"""
.. module:: boilerplate.apps.store.modules.payment.dummy.views
   :platform: Unix
   :synopsis: Views to collect and render

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from oscar.apps.payment import forms

from boilerplate.apps.store.modules.payment.base import views

class CollectBillingInfo(views.BaseRootView):
    """
    Collect billing info and pass it on.
    """
    template_name = "checkout/bankcard_billing_form.html"
    def get_context_data(self, **kwargs):
        ctx = {
            'bankcard_form': forms.BankcardForm(),
            'billing_address_form': forms.BillingAddressForm(),
        }
        ctx.update(super(CollectBillingInfo, self).get_context_data(**kwargs))
        return ctx

    def post(self, request, *args, **kwargs):
        if request.POST.get('action', '') == 'place_order':
            return self.do_place_order(request)
        bankcard_form = forms.BankcardForm(request.POST)
        billing_address_form = forms.BillingAddressForm(request.POST)
        if not all([bankcard_form.is_valid(), billing_address_form.is_valid()]):
            self.preview = False
            ctx = self.get_context_data(
                bankcard_form=bankcard_form,
                billing_address_form=billing_address_form)
            return self.render_to_response(ctx)
        self.preview = True
        return self.render_preview(request,
                                   bankcard_form=bankcard_form,
                                   billing_address_form=billing_address_form)
