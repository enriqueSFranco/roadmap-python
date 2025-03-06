from typing import Optional


class DLLNode:
    def __init__(
        self,
        prev: Optional["DLLNode"] = None,
        data: int = 0,
        next: Optional["DLLNode"] = None,
    ):
        self.prev = prev
        self.data = data
        self.next = next
