class Bytes:
    def __init__(self, b: bytes) -> None:
        self.b = b
    def __xor__(self, other):
        return Bytes(bytes(x^y for x,y in zip(self.b, other.b)))
    def __and__(self, other):
        return Bytes(bytes(x&y for x,y in zip(self.b, other.b)))
    def __str__(self) -> str:
        return "0x" + self.b.hex()
    def __eq__(self, other) -> bool:
        return self.b == other.b
    def __repr__(self) -> str:
        return "0x" + self.b.hex()