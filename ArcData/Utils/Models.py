import json
from typing import Union


class Range:
    def __init__(self, start, end, include_start=True, include_end=True):
        self.start = start
        self.end = end
        self.include_start = include_start
        self.include_end = include_end

    def verify(self, n: Union[int, float]) -> bool:
        if self.start <= n <= self.end:
            if n == self.start:
                if not self.include_start:
                    return False
            elif n == self.end:
                if not self.include_end:
                    return False
            else:
                return True
        return False


class Condition:
    def __init__(self, **kwargs):
        self._dict = kwargs

    def to_json(self) -> dict:
        return self._dict


class Record:
    def __init__(self, data: dict):
        self._data = data

    def __contains__(self, item: Condition):
        for key, value in item.to_json().items():
            if key not in self._data:
                return False
            if isinstance(value, dict) and isinstance(self._data[key], dict):
                if not Condition(**value) in Record(self._data[key]):
                    return False
            elif isinstance(value, Range):
                if not isinstance(self._data[key], Union[int, float]) or not value.verify(self._data[key]):
                    return False
            elif self._data[key] != value:
                return False
        return True

    def update(self, **kwargs) -> None:
        def dict_update(sub: dict, sup: dict) -> None:
            for key, value in sub.items():
                if isinstance(value, dict):
                    if isinstance(sup.get(key), dict):
                        dict_update(sup[key], value)
                sup[key] = value

        dict_update(kwargs, self._data)

    def to_json(self) -> dict:
        return self._data

    def dump_to(self, file: str) -> None:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4)

    @classmethod
    def load_from(cls, file: str):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return cls(data)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._data})"
