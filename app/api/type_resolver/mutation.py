from ariadne import MutationType

from app.api.ads.likes import likes

mutation = MutationType()

@mutation.field("like")
def resolve_logout(_, info, title):
    if title not in likes:
        likes[title] = 1
    elif title in likes:
        likes[title] += 1

    return True
