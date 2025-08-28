from ocsf.objects.object import Object
from ocsf.objects.rpc_interface import RpcInterface


class DceRpc(Object):
    # Required
    flags: list[str]
    rpc_interface: RpcInterface

    # Recommended
    command: str | None = None
    command_response: str | None = None
    opnum: int | None = None
