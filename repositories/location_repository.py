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