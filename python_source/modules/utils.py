from pathlib import Path

class define_path():
    def __init__(self,table_name):
        
        BASE_PATH = Path(__file__).parent

        #
        self.DATA_LAKE_PATH = (
            BASE_PATH
            / "data_lake"
            / "bronze"
            / table_name
        )
        self.DATA_LAKE_PATH.mkdir(
                    parents=True,
                    exist_ok=True
                )



        #
        self.LOG_PATH = (
            BASE_PATH.parent.parent
            / "logs"
            / f"{table_name}.log"
        )
        self.LOG_PATH.mkdir(
                    parents=True,
                    exist_ok=True
                )

