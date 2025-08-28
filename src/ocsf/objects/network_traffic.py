from ocsf.objects.object import Object


class NetworkTraffic(Object):
    # Recommended
    bytes: int | None = None
    packets: int | None = None

    # Optional
    bytes_in: int | None = None
    bytes_missed: int | None = None
    bytes_out: int | None = None
    chunks: int | None = None
    chunks_in: int | None = None
    chunks_out: int | None = None
    packets_in: int | None = None
    packets_out: int | None = None
