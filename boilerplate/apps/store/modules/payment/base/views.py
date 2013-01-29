# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from boilerplate.apps.store import import_shop_app

from oscar.apps.checkout import views

class BaseRootView(views.PaymentDetailsView):
    """
    Base class for payment modules "root" view.

    * allows for `template_name` and `template_name_preview` to be lists instead
      of single strings
    * adds `preview_url` and `method_index_url` variables to the context
    """
    #: for internal usage. This is why boilerplate.apps.store.modules.payment.base.app.PaymentModule sets module=self in every view
    module = None

    def get_template_names(self):
        """
        Allow for definition of multiple template names in template_name_preview
        and template_name. These MUST be lists (not tuples)
        """
        if self.preview:
            if isinstance(self.template_name_preview, list):
                return self.template_name_preview
            else:
                return [self.template_name_preview]
        else:
            if isinstance(self.template_name, list):
                return self.template_name
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        ctx = {
            'preview_url': self.module.get_preview_url(),
            'payment_module_root': self.module.get_root_url(),
        }
        ctx.update(super(BaseRootView, self).get_context_data(**kwargs))
        return ctx
