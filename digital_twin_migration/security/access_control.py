import functools
from dataclasses import dataclass
from typing import Any, List

from starlette.status import HTTP_403_FORBIDDEN

Allow: str = "allow"
Deny: str = "deny"


@dataclass(frozen=True)
class Principal:
    key: str
    value: str

    def __repr__(self) -> str:
        return f"{self.key}:{self.value}"

    def __str__(self) -> str:
        return self.__repr__()


@dataclass(frozen=True)
class SystemPrincipal(Principal):
    def __init__(self, value: str, *args, **kwargs) -> None:
        super().__init__(key="system", value=value, *args, **kwargs)


@dataclass(frozen=True)
class UserPrincipal(Principal):
    def __init__(self, value: str, *args, **kwargs) -> None:
        super().__init__(key="user", value=value, *args, **kwargs)


@dataclass(frozen=True)
class RolePrincipal(Principal):
    def __init__(self, value: str, *args, **kwargs) -> None:
        super().__init__(key="role", value=value, *args, **kwargs)


@dataclass(frozen=True)
class ItemPrincipal(Principal):
    def __init__(self, value: str, *args, **kwargs) -> None:
        super().__init__(key="item", value=value, *args, **kwargs)


@dataclass(frozen=True)
class ActionPrincipal(Principal):
    def __init__(self, value: str, *args, **kwargs) -> None:
        super().__init__(key="action", value=value, *args, **kwargs)


Everyone = SystemPrincipal(value="everyone")
Authenticated = SystemPrincipal(value="authenticated")


class AllowAll:
    def __contains__(self, item: Any) -> bool:
        return True

    def __repr__(self) -> str:
        return "*"

    def __str__(self) -> str:
        return self.__repr__()



