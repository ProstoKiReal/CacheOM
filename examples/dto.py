from dataclasses import dataclass


@dataclass(frozen=True)
class SessionDTO:
    user_id: int
    role: str
