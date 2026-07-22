from pathlib import Path


class mapping_paths():
    def __init__(self):
        ref_path=Path(__file__).resolve()
        root = ref_path.parents[2]
        self.root=root

        #
        self.logs=(root / 'logs')
        self.__check_make_dir(self.logs)


        # 
        self.data_lake=(root / 'data_lake')
        self.__check_make_dir(self.data_lake)

    def __check_make_dir(self,dir):
        dir.mkdir(
                parents=True,
                exist_ok=True
            )

    
  
