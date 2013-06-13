# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from oscar.apps.checkout import views
from oscar.apps.payment import forms
from oscar.apps.payment.exceptions import PaymentError

class BaseRootMixin(object):
    """
    Add base behavior for root views:

    * allows for `template_name` and `template_name_preview` to be lists instead
      of single strings
    * adds `preview_url` and `method_index_url` variables to the context
    """

    #: for internal usage. This is why
    #: oscar_payments.modules.payment.base.app.PaymentModule
    #: sets module=self in every view
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
        ctx.update(super(BaseRootMixin, self).get_context_data(**kwargs))
        return ctx

class BankcardBillcardMixin(object):
    """
    Mixin object that sets the template names and adds the forms to the context
    """
    #: default bankcard/billing forms collect template
    template_name = "checkout/bankcard_billing_form.html"
    #: bankcard form class
    bankcard_form_class = forms.BankcardForm
    #: default bankcard/billing hidden forms preview template
    template_name_preview = "checkout/bankcard_billing_preview.html"
    #: billing address form class
    billing_address_form_class = forms.BillingAddressForm

    def get_context_data(self, **kwargs):
        """
        Add the
        """
        ctx = {
            'bankcard_form': self.get_form('bankcard'),
            'billing_address_form': self.get_form('billing_address'),
            }
        ctx.update(super(BankcardBillcardMixin,
                         self).get_context_data(**kwargs))
        return ctx

    def get_form(self, type=None, *args, **kwargs):
        """
        Return the requested form with the given arguments

        :param type: REQUIRED: ('bankcard'|'billing_address')
        :param args: positional arguments for the form constructor
        :param kwargs: keyword arguments for the form constructor
        :return: The form instance
        """
        if type not in ('bankcard', 'billing_address'):
            raise PaymentError, "Form type parameter is required"
        return getattr(self, '{}_form_class'.format(type))(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle posting of the collect and preview forms. This method doesn't
        call super() so beware when overriding
        """

        # this is set by the preview template on the form. This should be more
        # elegantly handled, I think
        if request.POST.get('action', '') == 'place_order':
            return self.do_place_order(request)
        bankcard_form = self.get_form('bankcard', request.POST)
        billing_address_form = self.get_form('billing_address', request.POST)
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


class BaseRootView(BaseRootMixin, views.PaymentDetailsView):
    """
    Base class for payment modules "root" view.
    """
