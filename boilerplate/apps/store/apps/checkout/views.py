# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: containing module for oscar app overrides

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django import forms
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from boilerplate.apps.store import import_shop_app
from django.shortcuts import redirect

class PaymentDetailsView(FormView):
    template_name = 'checkout/payment_details.html'
    template_name_preview = 'checkout/preview.html'
    preview = False

    def __init__(self, *args, **kwargs):
        super(PaymentDetailsView, self).__init__(*args, **kwargs)
        self.app = import_shop_app('checkout', 'app').application


    def get_form_class(self):
        class PaymentModuleForm(forms.Form):
            module = forms.ChoiceField(choices=[
                m['app'].get_choice()
                for m in self.app.get_modules().values()],
                                       widget=forms.RadioSelect)
        return PaymentModuleForm

    def form_valid(self, form):
        module_name = form.cleaned_data['module']
        module = self.app.get_modules()[module_name]['app']
        return redirect(module.get_root_url())
