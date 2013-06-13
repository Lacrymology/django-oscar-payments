# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.utils.translation import ugettext_lazy as _
from oscar_payments.modules.payment.base.app import PaymentModule
from oscar_payments.modules.payment.paypal import views
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class PaypalPaymentModule(PaymentModule):
    name = 'paypal'
    verbose_name = _('Paypal')
    root_view = views.PaypalRootView

    #: Template to generate the "paypal" button for the choice field. PayPal
    #: recommends this to be taken from here:
    #: https://www.paypal.com/express-checkout-buttons
    choice_template_name = "checkout/paypal/choice_button.html"

    def get_urls(self):
        from paypal.express import urls
        base_urls = super(PaypalPaymentModule, self).get_urls()
        return urls.urlpatterns + base_urls

    def get_choice(self):
        text = render_to_string(self.choice_template_name)
        return (self.name, mark_safe(text))

application = PaypalPaymentModule()
