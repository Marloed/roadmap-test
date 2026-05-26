from blacksheep import json

def error_response(message, status):
    return json({"error": message}, status=status)

def status_response(message, status=200):
    return json({"status": message}, status=status)
