from fastapi import FastAPI, Body
from typing import Union
from calendar.calendar import Calendar
from validation.validator import Validator

app = FastAPI()
current_calendar = Calendar()


@app.get("/")
async def root() -> str:
    return "calendar FastAPI application"


@app.post("/add_event")
def add_event(data=Body()) -> str:
    try:
        date: str = data["date"]
    except KeyError:
        return "invalid request body"
    validator = Validator(date)
    validation_result = validator.date_validation()
    if validation_result is False:
        return "invalid date"
    event_name: str = data["event_name"]
    current_calendar.add_event(date, event_name)
    return f"value has been added with date - {date} and name - {event_name}"


@app.get("/get_all_events")
def get_all_events() -> Union[str, dict]:
    if len(current_calendar.dates) == 0:
        return "there are no events"
    return {"events": current_calendar.dates}


@app.post("/day_events")
def get_events_for_day(data=Body()) -> Union[str, dict]:
    try:
        date: str = data["date"]
    except KeyError:
        return "invalid request body"
    validator = Validator(date)
    validation_result = validator.date_validation()
    if validation_result is False:
        return "invalid date"
    response = current_calendar.get_events_for_day(date)
    if response is None:
        return "there are no events on this date"
    return {"events": response}


@app.post("/month_events")
def get_events_for_month(data=Body()) -> Union[str, dict]:
    try:
        date: str = data["date"]
    except KeyError:
        return "invalid request body"
    validator = Validator(date, get_for_month=True)
    validation_result = validator.date_validation()
    if validation_result is False:
        return "invalid date"

    split_date = date.split("-")
    response = current_calendar.get_events_for_month(split_date[0], split_date[1])
    if response is None:
        return "there are no events on this month"
    return {"events": response}


@app.put("/update_event_date")
def update_event_by_date(data=Body()) -> Union[str, dict]:
    try:
        date: str = data["date"]
        event_name: str = data["event_name"]
        new_date: str = data["new_date"]
    except KeyError:
        return "invalid request body"

    current_date_validator = Validator(date)
    new_date_validator = Validator(new_date)

    validation_current_date_result = current_date_validator.date_validation()
    validation_new_date_result = new_date_validator.date_validation()

    if validation_current_date_result is False or validation_new_date_result is False:
        return "invalid date"

    response = current_calendar.update_event_by_date(date, event_name, new_date)
    if response is False:
        return "there are no events on this date"
    else:
        return "the event has been successfully updated"


@app.put("/update_event_name")
def update_event_by_name(data=Body()) -> Union[str, dict]:
    try:
        date: str = data["date"]
        event_name: str = data["event_name"]
        new_event_name: str = data["new_event_name"]
    except KeyError:
        return "invalid request body"

    validator = Validator(date)

    validation_result = validator.date_validation()

    if validation_result is False or event_name == "" or new_event_name == "":
        return "invalid date"

    response = current_calendar.update_event_by_name(date, event_name, new_event_name)
    if response is False:
        return "there are no events on this date"
    else:
        return "the event has been successfully updated"


@app.delete("/delete_event")
def delete_event(data=Body()) -> Union[str, dict]:
    try:
        date: str = data["date"]
        event_name: str = data["event_name"]
    except KeyError:
        return "invalid request body"

    validator = Validator(date)
    validation_result = validator.date_validation()

    if validation_result is False or event_name == "":
        return "invalid date"

    response = current_calendar.delete_event(date, event_name)
    if response is False:
        return "there are no events on this date"
    else:
        return "the event has been successfully deleted"
