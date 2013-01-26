# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.views.generic import RedirectView

class PaymentDetailsView(RedirectView):
    """
    By default we don't add the payflow-pro stuff, so all this really needs to
    do is change the render template
    """
    url = 'paypal-direct-payment'

    def get_redirect_url(self, **kwargs):
        from django.core.urlresolvers import reverse
        return reverse(self.url)
