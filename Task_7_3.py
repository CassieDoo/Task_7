import requests
import time
from datetime import date
from datetime import timedelta
from pprint import pprint


def get_list_of_questions(tags, site, days):
    question_point = 0
    question_list = []
    todate = date.today()
    fromdate = todate - timedelta(days=days)
    todate_unix = int(time.mktime(todate.timetuple()))
    fromdate_unix = int(time.mktime(fromdate.timetuple()))
    params = {"fromdate": fromdate_unix, "todate": todate_unix, "tagged": tags, "site": site}
    response = requests.get("https://api.stackexchange.com/2.3/questions?", params=params).json()

    for question_point in range(len(response)):
        question_list.append(response["items"][question_point]["title"])
        question_point += 1
    return question_list


pprint(get_list_of_questions("Python", "stackoverflow", 2))
