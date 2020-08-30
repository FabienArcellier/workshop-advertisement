import hashlib

from ariadne import QueryType

from app.api.ads.ads import ads
from app.api.ads.likes import likes

query = QueryType()


@query.field("advertisements")
def resolve_hello(_, info, research):
    value: int = int(hashlib.sha256(research.encode('utf-8')).hexdigest(), 16) % 3
    return ads[value]


@query.field("likes")
def resolve_hello(_, info):
    return [{"title": title, "count": count } for title, count in likes.items()]
