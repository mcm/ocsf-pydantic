from ocsf.objects.rule import Rule


class FirewallRule(Rule):
    # Optional
    condition: str | None = None
    duration: int | None = None
    match_details: list[str] | None = None
    match_location: str | None = None
    rate_limit: int | None = None
    sensitivity: str | None = None
