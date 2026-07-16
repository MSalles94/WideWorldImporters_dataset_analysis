import argparse
from  datetime import datetime
from dateutil.relativedelta import relativedelta

class airflow_date_reference():
    def __init__(self):

        self.__get_reference_date()
        self.__define_data()

    
    def __get_reference_date(self):

        #get logical_date
        parser = argparse.ArgumentParser()
        parser.add_argument("--logical_date")
        args = parser.parse_args()
        logical_date = args.logical_date

        self.logical_date = datetime.fromisoformat(logical_date)

    
    def __define_data(self):

        logical_date=self.logical_date

        first_date = logical_date.replace(
            month=1,
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )
        
        last_date = (first_date.replace(day=1)+relativedelta(month=1))-relativedelta(day=1)


        self.first_date=first_date
        self.last_date=last_date

      
     

