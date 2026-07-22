from pathlib import Path
import datetime
import calendar  

class mapping_paths():
    def __init__(self):

        ref_path=Path(__file__).resolve()
        root = ref_path.parents[2]
        self.root=root

        #
        ref_time=datetime.datetime.now()
        self.logs=(root / 'logs'/'customer')
        self.make_dir(self.logs)
        self.logs=(self.logs / f'{ref_time}_.log')


        # 
        self.data_lake=(root / 'data_lake')
        self.make_dir(self.data_lake)

    def make_dir(self,dir):
        dir.mkdir(
                parents=True,
                exist_ok=True
            ) 
 

class date_reference():
    def __init__(self,year,month): 
        days=calendar.monthrange(year,month)[1]
 
        self.first_day=datetime.date(year,month,1)
        self.last_day=self.first_day.replace(day=days)
        pass
    
  
