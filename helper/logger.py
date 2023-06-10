import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def log(response, request_body=None):
    logger.info(f"REQUEST BODY: {request_body}\n")
    logger.info(f"RESPONSE_BODE: {response.text}\n.\n.")