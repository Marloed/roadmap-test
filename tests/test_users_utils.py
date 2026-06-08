from datetime import date

from app.users.users_utils import get_adult_border_date

def test_get_adult_border_date_returns_date():
    result = get_adult_border_date()
    
    assert isinstance(result, date)