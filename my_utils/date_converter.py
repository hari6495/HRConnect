import datetime
from datetime import datetime as dt


def convert_date(date: datetime.datetime) -> str:
    """
    Returns date string in format "YYYY-MM-DD"
    :param date: date object
    :return: date string in format "YYYY-MM-DD"
    """

    date_format = "%d-%b-%y"  # 12-FEB-06
    hire_date = dt.strptime(date, date_format)
    hire_date = hire_date.date()
    return str(hire_date)