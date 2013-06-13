django-oscar-payments
=====================

pluggable payments plugin for django-oscar

This module is supposed to be used to override oscar's checkout app, and it
supports various pluggable reusable payment systems, that have to be based off
`oscar_overrides.modules.payment.base.app`. The
`oscar_overrides.modules.payment.base.views` provides some basic mixins from
which to build your plugins' views.

**DISCLAIMER**
This code comes from a private framework I'm working on for
http://www.sologroup.gs/ As such it has some things that might be sub-ideal for
a standalone reusable app (such as the `OSCAR_OVERRIDES_PACKAGE` setting). I'm
more than open to accepting fixes these (and bugfixes, and any reusable
plugins you might want to create), and bringing the package to level.

Settings
--------
* `OSCAR_PAYMENT_MODULES`. A list of `(url, module name)` tuples. This is where
    you configure your active payment modules. An example that uses paypal,
    and the dummy would be this:

    ```
    BOILER_PAYMENT_MODULES = [
        (r'^paypal/', 'boilerplate.apps.store.modules.payment.paypal'),
        ]
    if DEBUG:
        BOILER_PAYMENT_MODULES.append(
            (r'^dummy/', 'boilerplate.apps.store.modules.payment.dummy'))
    ```

* `OSCAR_OVERRIDES_PACKAGE`. This is used by the checkout root view to find the

Example Plugins
---------------
There's a couple of example payment modules:

* `dummy`. This module asks you to introduce test credit card data, and marks the
    order as paid. To be used during development.
* `paypal`. This is a pluggable payment plugin for django-oscar-paypal. It
    requires django-oscar-paypal if you'll use it, and it uses it's urls, and
    templates

