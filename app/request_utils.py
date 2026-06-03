async def read_json_body(request):
    try:
        data = await request.json()
    except Exception:
        return None, "invalid JSON body"
    
    if data is None:
        return None, "invalid JSON body"
    
    if not isinstance(data, dict):
        return None, "invalid JSON body"
    
    return data, None