from functools import wraps
from flask import current_app, jsonify, request
import logging
import hashlib
from dotenv import load_dotenv
import hmac
import os

load_dotenv()
app_secret = os.getenv["APP_SECRET"]

def validate_signatur(payload, signature):
    """
    Validating the incoming payload's signature against our expected sign
    """
    expected_sign = hmac.new(
        bytes(current_app.config[app_secret], "latin-1"),
        msg=payload.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()

    #check if the sign matches
    return hmac.compare_digest(expected_sign, signature)

def signature_required(s):
    """
    To ensure that the incoming requests to our webhooks are valid or not and sign with the correct sign"""

    @wraps(s)
    def decorated_function(*args, **kwargs):
        signature = request.headers.get("X-Hub-Signature-256", "")[7:]

        if not validate_signatur(request.data.decode("utf-8"),signature):
            logging.info("signature verification failed!")
            return jsonify({"status": "error", "message":"invalid sign"}), 403
        return s(*args, **kwargs)
    
    return decorated_function