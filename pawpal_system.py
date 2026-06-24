from __future__ import annotations

from dataclasses import dataclass, field
from datetime import time
from typing import Dict, List


@dataclass
class Owner:
    id: str
    name: str
    pet_ids: List[str] = field(default_factory=list)

    def get_name(self) -> str:
        raise NotImplementedError

    def get_pets(self, system: "PawPalSystem") -> List["Pet"]:
        raise NotImplementedError


@dataclass
class Pet:
    id: str
    name: str
    owner_id: str
    breed: str
    schedule: "Schedule"

    def get_name(self) -> str:
        raise NotImplementedError

    def get_breed(self) -> str:
        raise NotImplementedError

    def get_owner(self, system: "PawPalSystem") -> Owner:
        raise NotImplementedError

    def get_schedule(self) -> "Schedule":
        raise NotImplementedError


@dataclass
class Task:
    action: str
    duration: int
    priority: str

    def get_action(self) -> str:
        raise NotImplementedError

    def get_duration(self) -> int:
        raise NotImplementedError

    def get_priority(self) -> str:
        raise NotImplementedError


@dataclass
class Schedule:
    pet_id: str
    tasks: Dict[time, Task] = field(default_factory=dict)

    def add_task(self, time_slot: time, task: Task) -> None:
        raise NotImplementedError

    def remove_task(self, time_slot: time) -> None:
        raise NotImplementedError


@dataclass
class PawPalSystem:
    """Central registry that owns all Owner and Pet records and resolves the
    relationships between them (kept as IDs on the dataclasses)."""

    owners: Dict[str, Owner] = field(default_factory=dict)
    pets: Dict[str, Pet] = field(default_factory=dict)

    def add_owner(self, owner: Owner) -> None:
        raise NotImplementedError

    def add_pet(self, pet: Pet) -> None:
        raise NotImplementedError

    def get_owner(self, owner_id: str) -> Owner:
        raise NotImplementedError

    def get_pet(self, pet_id: str) -> Pet:
        raise NotImplementedError

    def get_pets_for_owner(self, owner: Owner) -> List[Pet]:
        raise NotImplementedError
