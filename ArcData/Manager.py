from ArcData.Utils.File import File
from ArcData.Models import Record, Condition

# import json
from typing import Union
import pickle

base_records: dict[str, "DataBase"] = {}


class DataBase:
    def __init__(self, file: str = None, auto_save: bool = False):
        self.file: Union[str, File] = file or "data.cdb"
        self.data: list[Record] = []
        self.auto_save = auto_save

    @classmethod
    def create(cls, file: str):
        with open(file, "w", encoding="utf-8") as f:
            f.write("ARCDB")

        c = cls(file)
        c.load("__on_create__")
        return c

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

    @classmethod
    def fetch(cls, key: str):
        return base_records.get(key, cls())

    def register(self, key: str) -> "DataBase":
        base_records[key] = self
        return self

    def load(self, flag: str = "") -> None:
        if not self.loaded:
            self.file = File(self.file)
            if flag == "__on_create__":
                self.data = []
                return
            # data = json.loads(self.file.read_hex().decode()[5:])
            # self.data = list(map(Record, data))
            self.data = pickle.loads(self.file.read_hex(5))

    def save(self) -> None:
        if not self.loaded:
            raise ValueError()

        # self.file.write(b"ARCDB" + json.dumps([i.to_json() for i in self.data]).encode())
        self.file.write(b"ARCDB" + pickle.dumps(self.data))

    def search(self, *args: Condition) -> list[Record]:
        res = []
        for i in list(args):
            res += list(filter(lambda record: i in record, self.data))

        if len(args) == 1:
            return res
        else:
            def clear(x):
                if res.count(x) >= 1:
                    res.remove(x)
                    return True
                else:
                    return False

            return list(filter(lambda record: clear(record), res))

    def add(self, record: Record) -> None:
        self.data.append(record)
