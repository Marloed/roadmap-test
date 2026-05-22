from datetime import date 

def validate_required_user_fields(data):
    if "email" not in data or data["email"] == "":
        return {"error": "email is required"}
    
    if "username" not in data or data["username"] == "":
        return {"error": "username is required"}
    
    if "birth_date" not in data or data["birth_date"] == "":
        return {"error": "birth_date is required"}
    
    return None

def parse_birth_date(value):
    try:
        return date.fromisoformat(value), None
    except ValueError:
        return None, {"error": "birth_date must be YYYY-MM-DD"}
        