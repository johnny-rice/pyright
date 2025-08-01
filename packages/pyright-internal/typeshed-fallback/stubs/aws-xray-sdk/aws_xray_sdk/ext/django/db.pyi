from logging import Logger

from aws_xray_sdk.ext.dbapi2 import XRayTracedCursor

log: Logger

def patch_db() -> None: ...

class DjangoXRayTracedCursor(XRayTracedCursor):
    def execute(self, query, *args, **kwargs): ...
    def executemany(self, query, *args, **kwargs): ...
    def callproc(self, proc, args): ...
