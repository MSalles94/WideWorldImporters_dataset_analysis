from pathlib import Path

class define_path():
    def __init__(self,table_name):
        
        BASE_PATH = Path(__file__).parent

        #
        DIR_PATH_DATA_LAKE = (
            BASE_PATH.parent[2]
            / "data_lake"
            
        )
        DIR_PATH_DATA_LAKE.mkdir(
                    parents=True,
                    exist_ok=True
                )
    
        self.DATA_LAKE_PATH=(DIR_PATH_DATA_LAKE / table_name)



        #
        DIR_LOG = (
            BASE_PATH.parent.parent
            / "logs"
        )
        DIR_LOG.mkdir(
                    parents=True,
                    exist_ok=True
                )
        self.LOG_PATH=(DIR_LOG / f'{table_name}.log')

