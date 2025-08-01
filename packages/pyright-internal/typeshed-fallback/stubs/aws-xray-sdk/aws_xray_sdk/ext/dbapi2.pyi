from typing_extensions import Self

class XRayTracedConn:
    def __init__(self, conn, meta={}) -> None: ...
    def cursor(self, *args, **kwargs) -> XRayTracedCursor: ...

class XRayTracedCursor:
    def __init__(self, cursor, meta={}) -> None: ...
    def __enter__(self) -> Self: ...
    def execute(self, query, *args, **kwargs): ...
    def executemany(self, query, *args, **kwargs): ...
    def callproc(self, proc, args): ...

def add_sql_meta(meta) -> None: ...
