from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for 'checkout' Django app.
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals # noqa
