from datetime import datetime
from datetime import timedelta
class DateRanger():
    def __init__(self, initial_date):
        """Will yield a date between initial date to the actual date, after actual date is reached will return -1

        initial_date: The date where you want to start yielding from (YYYY-MM-DD)
        """  
        self._date_to = datetime.now().date()
        self.__initialize_date__(initial_date)
        self._delta = timedelta(days=0)

    @property
    def next_date(self):
        self._yield_date += self._delta
        while self._yield_date <= self._date_to:
            self._delta = timedelta(days=1)
            yield self._yield_date

        return -1

    def __initialize_date__(self,initial_date):
        try:
            aux_date = datetime.strptime(initial_date, '%Y-%m-%d').date()
            if aux_date > self._date_to:
                raise ValueError("The initial_date can't be greater than today's date")
            self._yield_date = aux_date
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")


