from _typeshed import Incomplete, OpenBinaryMode, ReadableBuffer
from asyncio import AbstractEventLoop
from collections.abc import Generator, Iterable
from concurrent.futures import Executor
from tempfile import TemporaryDirectory
from typing import TypeVar

from aiofiles.base import AsyncBase as AsyncBase
from aiofiles.threadpool.utils import (
    cond_delegate_to_executor as cond_delegate_to_executor,
    delegate_to_executor as delegate_to_executor,
    proxy_property_directly as proxy_property_directly,
)

_T = TypeVar("_T")

class AsyncSpooledTemporaryFile(AsyncBase[_T]):
    def fileno(self) -> Generator[Incomplete]: ...
    def rollover(self) -> Generator[Incomplete]: ...
    async def close(self) -> None: ...
    async def flush(self) -> None: ...
    async def isatty(self) -> bool: ...
    async def read(self, n: int = ..., /) -> str | bytes: ...
    async def readline(self, limit: int | None = ..., /) -> str | bytes: ...
    async def readlines(self, hint: int = ..., /) -> list[str | bytes]: ...
    async def seek(self, offset: int, whence: int = ...) -> int: ...
    async def tell(self) -> int: ...
    async def truncate(self, size: int | None = ...) -> None: ...
    @property
    def closed(self) -> bool: ...
    @property
    def encoding(self) -> str: ...
    @property
    def mode(self) -> OpenBinaryMode: ...
    @property
    def name(self) -> str | bytes: ...
    @property
    def newlines(self) -> str: ...
    async def write(self, s: str | bytes | ReadableBuffer) -> int: ...
    async def writelines(self, iterable: Iterable[str | bytes | ReadableBuffer]) -> None: ...

class AsyncTemporaryDirectory:
    async def cleanup(self) -> None: ...
    @property
    def name(self) -> str | bytes: ...
    def __init__(
        self, file: TemporaryDirectory[Incomplete], loop: AbstractEventLoop | None, executor: Executor | None
    ) -> None: ...
    async def close(self) -> None: ...
