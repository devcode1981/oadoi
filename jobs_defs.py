from sqlalchemy import text
from sqlalchemy import orm
from sqlalchemy import sql
from sqlalchemy import types
from sqlalchemy.dialects.postgresql import JSONB

import app
from app import db
from jobs import update_registry
from jobs import Update

from publication import Crossref

# q = db.session.query(Crossref.id)
# q = q.filter(Crossref.response["color"].cast(types.Text) != None)
# q = q.filter(Crossref.updated < '2017-03-12')
text_query = u"""select doi from export_view_min where oa_color in ('green', 'gold') and open_urls is null"""
update_registry.register(Update(
    job=Crossref.run,
    # query=q,
    query=text_query,
    queue_id=0
))


# text_query = u"""select id from dois_random_recent, crossref where dois_random_recent.doi=crossref.id and response is null"""
text_query = u"""select lower(doi) from dois_random_recent;"""
update_registry.register(Update(
    job=Crossref.run_subset,
    query=text_query,
    queue_id=1
))

