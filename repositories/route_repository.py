from db.run_sql import run_sql
from models.crag import Crag
from models.location import Location
from models.route import Route
import repositories.crag_repository as crag_repository
import repositories.location_repository as location_repository


def save(route):
    sql = "INSERT INTO routes (name, grade, crag_id, climbed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [route.name, route.grade, route.crag.id, route.climbed]
    results = run_sql(sql, values)
    id = results[0]['id']
    route.id = id
    return route

def select_all():
    routes = []
    sql = "SELECT * FROM routes"
    results = run_sql(sql)

    for row in results:
        crag = crag_repository.select(row['crag_id'])
        route = Route(row['name'], row['grade'], crag, row['climbed'], row['id'])
        routes.append(route)
    return routes

def select(id):
    route = None
    sql = "SELECT * FROM routes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        crag = crag_repository.select(result['crag_id'])
        route = Route(result['name'], result['grade'], crag, result['climbed'], result['id'])
    return route

def delete_all():
    sql = "DELETE FROM routes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM routes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(route):
    sql = "UPDATE routes SET (name, grade, crag_id, climbed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [route.name, route.grade, route.crag.id, route.climbed, route.id]
    run_sql(sql, values)


def select_climbed():
    routes = []
    sql = "SELECT * FROM routes"
    results = run_sql(sql)

    for row in results:
        crag = crag_repository.select(row['crag_id'])
        route = Route(row['name'], row['grade'], crag, row['climbed'], row['id'])
        if route.climbed == True:
            routes.append(route)
    return routes


def select_unclimbed():
    routes = []
    sql = "SELECT * FROM routes"
    results = run_sql(sql)

    for row in results:
        crag = crag_repository.select(row['crag_id'])
        route = Route(row['name'], row['grade'], crag, row['climbed'], row['id'])
        if route.climbed == False:
            routes.append(route)
    return routes
