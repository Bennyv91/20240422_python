# defines a contract - yes, this is an interface
from typing import Protocol


class History(Protocol):
    def get_history(self) -> list[tuple[int, str, float]]: ...

    def append_history_entry(self, operation: str, operand: float) -> None: ...

    def remove_history_entry(self, entry_id: int) -> None: ...

    def clear_history_entries(self) -> None: ...