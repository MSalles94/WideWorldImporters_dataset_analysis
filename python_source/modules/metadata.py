import json
from pathlib import Path


class MetadataManager:

    def __init__(self, file_path):

        self.file_path = Path(__file__).parent[2] / 'data_lake' /'injestion_metadata.JSON'
 


    def read(self):

        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)


    def write(self, data):

        with open(self.file_path, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def upsert(self, new_config):

        configs = self.read()

        found = False


        for config in configs:

            if (
                config["source_schema"] == new_config["source_schema"]
                and
                config["source_table"] == new_config["source_table"]
            ):

                config.update(new_config)

                found = True
                break


        if not found:
            configs.append(new_config)


        self.write(configs)