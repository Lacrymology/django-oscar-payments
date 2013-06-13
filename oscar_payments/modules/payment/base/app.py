# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_noop as _
from oscar.core.application import Application
from oscar.apps.payment.exceptions import PaymentError

from oscar_payments.modules.payment.base.views import BaseRootView

class PaymentModule(Application):
    """
    Base payment module. Tries to provide reasonable default behaviors

    To create a payment module,subclass this.
    """
    #: This is used from the checkout app and needs to be defined in each
    #: subclass. It is also the namespace for each module's urls
    name = None
    #: Human-readable name for the payment app. Should be internationalized if
    #: required
    verbose_name = _('UNDEFINED')

    #: Root view. It's mapped to r'$^' by default
    root_view = BaseRootView
    #: Preview view. It defaults to the same as `root_view`
    preview_view = None

    def __init__(self, *args, **kwargs):
        if self.name is None:
            raise PaymentError, "%s.%s: name property cannot be None" % (
                self.__class__.__module__, self.__class__.__name__)
        if self.preview_view is None:
            self.preview_view = self.root_view
        super(PaymentModule, self).__init__(*args, **kwargs)

    def get_choice(self):
        """
        This is used in the select payment form to generate the list of choices.
        By default it returns (name, verbose_name)

        :return: a Tuple as expected by forms.ChoiceFields' choices parameter
        """
        return (self.name, self.verbose_name)

    def get_root_url(self):
        """
        Get this module's namespaced root url name for use in returning
        HTTPResponseRedirect

        :return: checkout:<name>:<root_url_name>
        """
        return ":".join(['checkout', self.name, self.root_url_name()])

    def get_preview_url(self):
        """
        Get this module's namespaced preview url name for use in url reversing

        :return: checkout:<name>:<preview_url_name>
        """
        return ":".join(['checkout', self.name, self.preview_url_name()])

    def root_url_name(self):
        """
        Root url name to use in url registration. WITHOUT the namespace
        """
        return 'index'

    def preview_url_name(self):
        """
        Preview url name to use in url registration. WITHOUT the namespace
        """
        return 'preview'

    def get_urls(self):
        """
        Add default root and preview urls and
        """
        base_urls = super(PaymentModule, self).get_urls()
        urlpatterns = patterns('',
            url(r'^$', self.root_view.as_view(module=self), name=self.root_url_name()),
            url(r'^preview/$', self.root_view.as_view(module=self),
                kwargs=dict(preview=True), name=self.preview_url_name())
        )
        return urlpatterns + base_urls
