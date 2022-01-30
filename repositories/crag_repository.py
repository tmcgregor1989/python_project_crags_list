from db.run_sql import run_sql
from models.crag import Crag
from models.location import Location
from models.route import Route
import repositories.location_repository as location_repository


def save(crag):
    sql = "INSERT INTO crags (name, location_id) VALUES (%s, %s) RETURNING *"
    values = [crag.name, crag.location.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    crag.id = id
    return crag

def select_all():
    crags = []
    sql = "SELECT * FROM crags"
    results = run_sql(sql)

    for row in results:
        location = location_repository.select(row['location_id'])
        crag = Crag(row['name'], location, row['id'])
        crags.append(crag)
    return crags

def select(id):
    crag = None
    sql = "SELECT * FROM crags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = location_repository.select(result['location_id'])
        crag = Crag(result['name'], location, result['id'] )
    return crag

def delete_all():
    sql = "DELETE FROM crags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM crags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(crag):
    sql = "UPDATE crags SET (name, location_id) = (%s, %s) WHERE id = %s"
    values = [crag.name, crag.location.id, crag.id]
    run_sql(sql, values)

def routes(crag):
    routes = []

    sql = "SELECT * FROM routes WHERE crag_id = %s"
    values = [crag.id]
    results = run_sql(sql, values)

    for row in results:
        route = Route(row['name'], row['grade'], row['crag_id'], row['climbed'], row['id'])
        routes.append(route)
    return routes
