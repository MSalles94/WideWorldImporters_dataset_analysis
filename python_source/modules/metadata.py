from pathlib import Path
import json
from typing import Any


class MetadataManager:
    def __init__(self ):
        from python_source.modules.utils import mapping_paths
        path_root=mapping_paths().root

        json_path=(path_root / 'data_lake' / 'injestion_metadata.JSON')
        self.file_path = json_path

        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self._save({})

        self._load()

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def _save(self, data=None):
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def reload(self):
        self._load()

    def save(self):
        self._save()

    def exists(self, table: str) -> bool:
        return table in self.data

    def get(self, table: str) -> dict | None:
        return self.data.get(table)

    def set(self, table: str, values: dict):
        self.data[table] = values
        self.save()

    def update(self, table: str, **kwargs):
        if table not in self.data:
            self.data[table] = {}

        self.data[table].update(kwargs)
        self.save()

    def delete(self, table: str):
        if table in self.data:
            del self.data[table]
            self.save()

    def get_value(self, table: str, key: str, default=None):
        return self.data.get(table, {}).get(key, default)

    def set_value(self, table: str, key: str, value: Any):
        if table not in self.data:
            self.data[table] = {}

        self.data[table][key] = value
        self.save()

    def list_tables(self):
        return list(self.data.keys())
 