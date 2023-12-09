from datetime import datetime

# Constants
MAX_DATE = "9999-12-31"

def get_current_date():
    """
    Gets today's date ONLY (ex: 2023-12-09)

    Returns:
        str: today's date as a formatted string
    """
    return datetime.today().strftime("%Y-%m-%d")

def get_current_date_time():
    """
    Gets the date AND time in 24hr format
    (ex: 2023-12-09 17:45:40)

    Returns:
        str: today's date AND time
        as a formatted string.
    """
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")