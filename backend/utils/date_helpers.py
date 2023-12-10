from datetime import datetime
from dateutil.relativedelta import relativedelta

DATEFMT = "%Y-%m-%d"
TIMEFMT = "%H:%M:%S"

# Constants
def get_current_date():
    """
    Gets today's date ONLY (ex: 2023-12-09)

    Returns:
        str: today's date as a formatted string
    """

    return datetime.today().strftime(DATEFMT)

def get_current_date_time():
    """
    Gets the date AND time in 24hr format
    (ex: 2023-12-09 17:45:40)

    Returns:
        str: today's date AND time
        as a formatted string.
    """
    return datetime.today().strftime(f"{DATEFMT} {TIMEFMT}")

def get_max_date():
    """
    Returns the max date (current year + 2, Dec 31st)
    """
    return (datetime.today() + relativedelta(years=2,
                                             month=12,
                                             day=31)).strftime(DATEFMT)

def get_year_end_date():
    """
    Returns the date of the last day of the current year.
    """

    return (datetime.today() + relativedelta(month=12,
                                             day=31)).strftime(DATEFMT)