import os


class File:
    def __init__(self, path: str):
        if os.path.exists(path):
            if os.path.isdir(path):
                raise ValueError()
            self.path = path
        else:
            with open(path, 'wb') as f:
                pass
            self.path = path

    def read_hex(self, byte: int = None) -> bytes:
        with open(self.path, "rb") as f:
            if byte:
                f.seek(byte)
            return f.read()

    def verify(self, header: bytes) -> bool:
        with open(self.path, "rb") as file:
            header_bytes = file.read(len(header))
        if header_bytes == header:
            return True
        return False

    def insert(self, byte: int, data: bytes) -> None:
        with open(self.path, "r+b") as f:
            f.seek(byte)
            f.write(data)

    def write(self, data: bytes) -> None:
        with open(self.path, "wb") as f:
            f.write(data)
