from pydantic import BaseModel

from ocsf.objects.http_request import HttpRequest
from ocsf.objects.http_response import HttpResponse
from ocsf.objects.network_connection_info import NetworkConnectionInfo
from ocsf.objects.network_proxy import NetworkProxy as NetworkProxy_
from ocsf.objects.network_traffic import NetworkTraffic
from ocsf.objects.tls import TLS


class NetworkProxy(BaseModel):
    # Recommended
    proxy_connection_info: NetworkConnectionInfo | None = None
    proxy_tls: TLS | None = None
    proxy_traffic: NetworkTraffic | None = None

    # Optional
    proxy_endpoint: NetworkProxy_ | None = None
    proxy_http_request: HttpRequest | None = None
    proxy_http_response: HttpResponse | None = None
