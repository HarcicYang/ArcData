from ArcData.Utils.File import File
from ArcData.Utils.Models import Record, Condition

import json
from typing import Union


class DataBase:
    def __init__(self, file: str = None, auto_save: bool = False):
        self.file: Union[str, File] = file or "data.cdb"
        self.data: list[Record] = []
        self.auto_save = auto_save

    @classmethod
    def create(cls, file: str):
        with open(file, "w", encoding="utf-8") as f:
            f.write("ARCDB[]")

        return cls(file)

    @property
    def loaded(self) -> bool:
        return isinstance(self.file, File)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __aenter__(self):
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    def load(self) -> None:
        if not self.loaded:
            self.file = File(self.file)
            data = json.loads(self.file.read_hex().decode()[5:])
            self.data = list(map(Record, data))

    def save(self) -> None:
        if not self.loaded:
            raise ValueError()

        self.file.write(b"ARCDB" + json.dumps([i.to_json() for i in self.data]).encode())

    def search(self, condition: Condition) -> list[Record]:
        return list(filter(lambda record: condition in record, self.data))

    def add(self, record: Record) -> None:
        self.data.append(record)
