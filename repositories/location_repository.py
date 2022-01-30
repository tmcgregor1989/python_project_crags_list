from db.run_sql import run_sql
from models.crag import Crag
from models.location import Location
from models.route import Route
import repositories.crag_repository as crag_repository
import repositories.location_repository as location_repository



def save(location):
    sql = "INSERT INTO locations (name) VALUES (%s) RETURNING *"
    values = [location.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location

def select_all():
    locations = []
    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row['name'], row['id'])
        locations.append(location)
    return locations




def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = Location(result['name'], result['id'] )
    return location


def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(location):
    sql = "UPDATE locations SET name = %s WHERE id = %s"
    values = [location.name, location.id]
    run_sql(sql, values)

def crags(location):
    crags = []

    sql = "SELECT * FROM crags WHERE location_id = %s"
    values = [location.id]
    results = run_sql(sql, values)

    for row in results:
        crag = Crag(row['name'], row['location_id'], row['id'])
        crags.append(crag)
    return crags