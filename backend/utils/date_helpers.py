from datetime import datetime
from dateutil.relativedelta import relativedelta

DATEFMT = "%Y-%m-%d"
TIMEFMT = "%H:%M:%S"

# Constants
def get_current_date() -> str:
    """
    Gets today's date ONLY (ex: 2023-12-09)
    Returns:
        str: today's date as a formatted string
    """
    return datetime.today().strftime(DATEFMT)

def get_current_date_time() -> str:
    """
    Gets the date AND time in 24hr format
    (ex: 2023-12-09 17:45:40)
    Returns:
        str: today's date AND time
        as a formatted string.
    """
    return datetime.today().strftime(f"{DATEFMT} {TIMEFMT}")

def get_future_date(years=2,month=12,day=31) -> str:
    """
    Retrieves a date in the future, by default
    being the last day of that year, relative
    to the current date.
    params:
        years (int): n future years.
        month (int): target month.
        day (int): target day of target month.
    Returns:
        str: string representation of the future date.
    """

    return (datetime.today() + relativedelta(years=years,
                                             month=month,
                                             day=day)).strftime(DATEFMT)

def get_date_current_year(month=12,day=31) -> str:
    """
    Retrieves a date for the current year.
    params:
        month (int): the month number.
        day (int): the day number (max 31)
    Returns:
        str: string representation of a date for the current year,
        with the specified DATEFMT.
    """
    return (datetime.today() + relativedelta(month=month,
                                             day=day)).strftime(DATEFMT)

def cleanse_extraneous_hyphens(date_str: str) -> str:
    """
    Args:
        date_str (str): target string with extraneous hyphens.
    Returns:
        str: string without extraneous hyphens (i.e. -0001-11-30T00:00:00-0500
        now becomes 0001-11-30T00:00:00-0500)
    """
    date_str_split = date_str.split('-',1)
    return "".join(date_str_split)