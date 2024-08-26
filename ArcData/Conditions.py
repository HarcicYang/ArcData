from typing import Union


class Range:
    def __init__(self, start, end, include_start=True, include_end=True):
        if start >= end:
            self.start = end
            self.end = start
        else:
            self.start = start
            self.end = end
        self.include_start = include_start
        self.include_end = include_end

    def verify(self, n: Union[int, float]) -> bool:
        ...


class InRange(Range):
    def verify(self, n: Union[int, float]) -> bool:
        if self.include_start:
            start_comparison = self.start <= n
        else:
            start_comparison = self.start < n

        if self.include_end:
            end_comparison = n <= self.end
        else:
            end_comparison = n < self.end

        return start_comparison and end_comparison


class OutRange(Range):
    def verify(self, n: Union[int, float]) -> bool:
        if self.include_start:
            start_comparison = n <= self.start
        else:
            start_comparison = n < self.start

        if self.include_end:
            end_comparison = n >= self.end
        else:
            end_comparison = n > self.end

        return start_comparison and end_comparison


class Include:
    def __init__(self, key: str):
        self.key = key

    def verify(self, s: Union[str, list]) -> bool:
        return self.key in s


class Exclude:
    def __init__(self, key: str):
        self.key = key

    def verify(self, s: Union[str, list]) -> bool:
        return self.key not in s


class Any:
    pass
