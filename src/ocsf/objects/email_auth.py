from ocsf.objects.object import Object


class EmailAuth(Object):
    # Recommended
    dkim: str | None = None
    dkim_domain: str | None = None
    dkim_signature: str | None = None
    dmarc: str | None = None
    dmarc_override: str | None = None
    dmarc_policy: str | None = None
    spf: str | None = None
