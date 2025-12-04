from datetime import date, datetime, timedelta

class AbstractClock:
    def __init__(self, current_date: date, current_time: datetime):
        self.current_date = current_date
        self.current_time = current_time

    def today(self) -> date:
        return self.current_date

    def now(self) -> datetime:
        return self.current_time

    def advance_days(self, days: int) -> date:
        self.current_date += timedelta(days=days)
        self.current_time += timedelta(days=days)


clock = AbstractClock(current_date=date.today(), current_time=datetime.now())
print(clock.today())
print(clock.now())
