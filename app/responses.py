from blacksheep import json

def error_response(message, status):
    return json({"error": message}, status=status)

def status_response(message, status=200):
    return json({"status": message}, status=status)

def validation_error_response(error):
    print(error.errors())
    first_error = error.errors()[0]
    field = first_error["loc"][0]
    error_type = first_error["type"]
    
    if error_type == "missing":
        return error_response(f"{field} is required", 400)
    
    if error_type == "value_error":
        original_errors = first_error.get("ctx", {}).get("error")
        if original_errors is not None:
            return error_response(str(original_errors), 400)
        
    if field == "birth_date":
        return error_response("birth_date must be YYYY-MM-DD", 400)
    
    return error_response(first_error["msg"], 400)
