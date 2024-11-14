# paypal_config.py
import paypalrestsdk
from django.conf import settings

def configure_paypal():
    print("PayPal Client ID: ", settings.PAYPAL_CLIENT_ID)  # Debugging
    print("PayPal Client Secret: ", settings.PAYPAL_CLIENT_SECRET)  # Debugging

    paypalrestsdk.configure({
        "mode": settings.PAYPAL_MODE,
        "client_id": settings.PAYPAL_CLIENT_ID,
        "client_secret": settings.PAYPAL_CLIENT_SECRET
    })
