class Validator:
    def __init__(self, date: str = None, get_for_month: bool = False):
        self.date = date
        self.get_for_month = get_for_month
        self.day_in_month = {
            "01": 31,
            "02": {
                True: 29,
                False: 28
            },
            "03": 31,
            "04": 30,
            "05": 31,
            "06": 30,
            "07": 31,
            "08": 31,
            "09": 30,
            "10": 31,
            "11": 30,
            "12": 31
        }

    def date_validation(self) -> bool:
        if self.get_for_month:
            self.date = "01-"+self.date
        if self.date is not None:
            split_date = self.date.split("-")
            if len(split_date) != 3:
                return False
            try:
                int(split_date[1])
                if split_date[1] not in self.day_in_month:
                    return False
                if len(split_date[1]) == 1:
                    split_date[1] = f"0{split_date[1]}"
            except ValueError:
                return False

            try:
                int_day = int(split_date[0])
                int_month = int(split_date[1])
                int_year = int(split_date[2])

                if int_month != 2:
                    if int_day > int(self.day_in_month[split_date[1]]):
                        return False
                else:
                    if int_year % 4 == 0:
                        if int_day > int(self.day_in_month[split_date[1]][True]):
                            return False
                    if int_year % 4 != 0:
                        if int_day > int(self.day_in_month[split_date[1]][False]):
                            return False

                if 0 > int_month > 12:
                    return False
                if 0 > int_year:
                    return False
            except ValueError:
                return False
            return True
