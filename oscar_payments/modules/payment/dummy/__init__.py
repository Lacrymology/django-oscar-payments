# -*- coding: utf-8 -*-

"""
.. module:: oscar_payments.modules.dummy
   :platform: Unix
   :synopsis: dummy payment module for oscar. Receives Credit Card data and
        billing address. This is the list of valid test credit card numbers:

CREDIT_CARDS = {
    'American Express': [
        '378282246310005',
        '371449635398431',
        ],
    'MasterCard': [
        '5555555555554444',
        '5105105105105100',
        ],
    'Visa': [
        '4111111111111111',
        '4012888888881881',
        # Note : Even though this number has a different character count than
        #   the other test numbers, it is the correct and functional number.
        '4222222222222'
        ]
    }

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""

# Test Credit Card Account Numbers
CREDIT_CARDS = {
    'American Express': [
        '378282246310005',
        '371449635398431',
        ],
    'MasterCard': [
        '5555555555554444',
        '5105105105105100',
        ],
    'Visa': [
        '4111111111111111',
        '4012888888881881',
        # Note : Even though this number has a different character count than
        #   the other test numbers, it is the correct and functional number.
        '4222222222222'
        ]
    }
