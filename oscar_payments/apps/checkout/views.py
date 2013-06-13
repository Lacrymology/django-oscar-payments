# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: containing module for oscar app overrides

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django import forms
from django.shortcuts import redirect
from django.views.generic.edit import FormMixin
from oscar.apps.checkout import views

from oscar_payments import import_shop_app

class PaymentDetailsView(FormMixin, views.PaymentDetailsView):
    """
    We need to redefine post to acommodate both the FormView and
    PaymentDetailView parts of this view.

    In our case, this view should just render a form to choose the payment
    method, but Oscar expects this view to handle order / payment details
    preview as well
    """

    #: We change the normal template name because we want this to be a
    #: "select payment" view

    template_name = "checkout/select_payment.html"
    def __init__(self, *args, **kwargs):
        super(PaymentDetailsView, self).__init__(*args, **kwargs)
        self.app = import_shop_app('checkout', 'app').application

    def get_success_url(self):
        """
        This needs to be overriden because FormMixin is before in the MRO and it
        raises if not overriden
        :return: `oscar.apps.checkout.views.PaymentDetailsView.get_success_url`
        """
        return views.PaymentDetailsView.get_success_url(self)

    def get_context_data(self, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return super(PaymentDetailsView, self).get_context_data(form=form,
                                                                **kwargs)

    def post(self, request, *args, **kwargs):
        # oscar bit
        error_response = self.get_error_response()
        if error_response:
            return error_response
        if self.preview:
            if request.POST.get('action', '') == 'place_order':
                return self.submit(request.basket)
            return self.render_preview(request, **kwargs)

        # FormView bit
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form_class(self):
        class PaymentModuleForm(forms.Form):
            module = forms.ChoiceField(
                label='', # no label for this field
                choices=[m['app'].get_choice()
                         for m in self.app.modules.values()],
                widget=forms.RadioSelect)
        return PaymentModuleForm

    def form_valid(self, form):
        module_name = form.cleaned_data['module']
        module = self.app.modules[module_name]['app']
        return redirect(module.get_root_url())
