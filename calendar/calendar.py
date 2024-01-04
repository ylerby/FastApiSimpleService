from typing import Optional


class Calendar:
    def __init__(self) -> None:
        self.dates: dict[str, list[str]] = {}

    def add_event(self, date: str, event_name: str) -> None:
        if date not in self.dates:
            self.dates[date] = [event_name]
        else:
            if event_name not in self.dates[date]:
                self.dates[date].append(event_name)
            else:
                return

    def update_event_by_date(self, date: str, event_name: str,
                             new_date: str) -> bool:
        flag: bool = False
        if date not in self.dates:
            return False
        else:
            for event in self.dates[date]:
                if event == event_name:
                    flag = True
                    if new_date not in self.dates:
                        self.dates[new_date] = [event_name]
                    else:
                        self.dates[new_date].append(event_name)
        if flag is False:
            return False
        self.dates[date].remove(event_name)
        if len(self.dates[date]) == 0:
            self.dates.pop(date)
        return True

    def update_event_by_name(self, date: str, event_name: str,
                             new_event_name: str) -> bool:
        flag: bool = False
        if date not in self.dates:
            return False
        else:
            for event in self.dates[date]:
                if event == event_name:
                    flag = True
                    self.dates[date].append(new_event_name)
                    self.dates[date].remove(event_name)
        if flag is False:
            return False
        return True

    def delete_event(self, date: str, event_name: str) -> bool:
        flag: bool = False
        if date not in self.dates:
            return False
        else:
            for event in self.dates[date]:
                if event == event_name:
                    flag = True
                    self.dates[date].remove(event_name)
                    if len(self.dates[date]) == 0:
                        self.dates.pop(date)
        if flag is False:
            return False
        return True

    def get_events_for_day(self, date: str) -> Optional[list]:
        if date not in self.dates:
            return None
        if len(self.dates[date]) == 0:
            return None
        return self.dates[date]

    def get_events_for_month(self, month: str, year: str) -> Optional[list[list[str]]]:
        result = []
        for i in range(32):
            date = f"{i}-{month}-{year}"
            if date not in self.dates:
                continue
            else:
                result.append(self.dates[date])
        if len(result) == 0:
            return None
        return result
