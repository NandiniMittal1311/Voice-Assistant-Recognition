import datetime

def get_current_time():
    """
    Returns the current system time as a string.
    """
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_current_date():
    """
    Returns today's date as a string.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d")

def clean_query(query):
    """
    Cleans a string query by removing unwanted words or extra spaces.
    """
    return query.replace("wikipedia", "").strip()
