from typing import Dict


def task_one_format(details) -> Dict:
    """
    To create formatted dictionary with only name, email and phone number
    :param details: dictionary with all the details of employee
    :return: dictionary with only name, email and phone number
    """
    formatted_details = {"Name": details.get("FIRST_NAME") + " " + details.get("LAST_NAME"),
                         "Email": details.get("EMAIL"),
                         "Phone number": details.get("PHONE_NUMBER")
                         }

    return formatted_details