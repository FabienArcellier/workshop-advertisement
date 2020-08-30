import hashlib

from ariadne import QueryType

from app.api.ads.ads import ads

query = QueryType()


@query.field("advertisements")
def resolve_hello(_, info, research):
    value: int = int(hashlib.sha256(research.encode('utf-8')).hexdigest(), 16) % 3
    return ads[value]
