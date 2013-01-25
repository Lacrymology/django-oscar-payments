# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.utils.translation import ugettext_noop as _
from oscar.core.application import Application

class PaymentModule(Application):
    """
    Base payment module.

    To create a payment module,subclass this.
    """
    #: This is used from the checkout app and needs to be defined in each
    #: subclass
    module_name = None
    #: Human-readable name for the payment app. Should be internationalized if
    #: required
    verbose_name = _('UNDEFINED')

    def get_choice(self):
        """
        This is used in the select payment form to generate the list of choices.
        By default it returns (module_name, verbose_name)

        :return: a Tuple as expected by forms.ChoiceFields' choices parameter
        """
        return (self.module_name, self.verbose_name)

    def get_root_url(self):
        """
        Get this module's root url for use in returning HTTPResponseRedirect

        :return: module_name-index
        """
        return "{}-index".format(self.module_name)
