from datetime import date

def get_adult_border_date():
    today = date.today()
    
    return date(
        today.year - 18,
        today.month,
        today.day,
    )