from flask import Flask, render_template, request, redirect, Blueprint
from repositories import crag_repository
from repositories import route_repository
from repositories import location_repository
from models.route import Route
from models.crag import Crag
from models.location import Location
crags_blueprint = Blueprint("crags", __name__)

@crags_blueprint.route("/routes")
def routes():
    routes = route_repository.select_all()
    return render_template("routes/index.html", all_routes = routes)

@crags_blueprint.route("/routes/routes-climbed")
def routes_climbed():
    routes = route_repository.select_all()
    return render_template("routes/routes_climbed.html", all_routes = routes)

@crags_blueprint.route("/routes/routes-not-climbed")
def routes_not_climbed():
    routes = route_repository.select_all()
    return render_template("routes/not_climbed.html", all_routes = routes)
    


# add new route
@crags_blueprint.route("/routes/new", methods=['GET'])
def new_route():
    crags = crag_repository.select_all()
    return render_template('routes/new.html', all_crags = crags)

# create new route
@crags_blueprint.route('/routes', methods=['POST'])
def create_route():
    name = request.form['name']
    grade = request.form['grade']
    crag_id = request.form['crag_id']
    climbed = request.form['climbed']
    crag = crag_repository.select(crag_id)
    route = Route(name, grade, crag, climbed)
    route_repository.save(route)
    return redirect('/routes')


@crags_blueprint.route('/routes/<id>', methods=['GET'])
def show_route(id):
    route = route_repository.select(id)
    return render_template('routes/show.html', route = route)

# delete an entry
@crags_blueprint.route('/routes/<id>/delete', methods=['POST'])
def delete_route(id):
    route_repository.delete(id)
    return redirect('/routes')

# edit an entry
@crags_blueprint.route('/routes/<id>/edit', methods=['GET'])
def edit_route(id):
    route = route_repository.select(id)
    crags = crag_repository.select_all()
    return render_template('routes/edit.html', route = route, all_crags = crags)

@crags_blueprint.route('/routes/<id>', methods=['POST'])
def update_route(id):
    name = request.form['name']
    grade = request.form['grade']
    crag_id = request.form['crag_id']
    climbed = request.form['climbed']
    crag = crag_repository.select(crag_id)
    route = Route(name, grade, crag, climbed, id)
    route_repository.update(route)
    return redirect('/routes')


    # CRAG SECTION

@crags_blueprint.route("/crags")
def crags():
    crags = crag_repository.select_all()
    return render_template("crags/index.html", all_crags = crags)

@crags_blueprint.route('/crags/<id>/delete', methods=['POST'])
def delete_crag(id):
    crag_repository.delete(id)
    return redirect('/crags')

# add new route
@crags_blueprint.route("/crags/new", methods=['GET'])
def new_crag():
    locations = location_repository.select_all()
    return render_template('crags/new.html', all_locations = locations)

# create new route
@crags_blueprint.route('/crags', methods=['POST'])
def create_crag():
    name = request.form['name']
    location_id = request.form['location_id']
    location = location_repository.select(location_id)
    crag = Crag(name, location)
    crag_repository.save(crag)
    return redirect('/crags')

@crags_blueprint.route('/crags/<id>', methods=['GET'])
def show_crag(id):
    crag = crag_repository.select(id)
    routes = crag_repository.routes(crag)
    return render_template('crags/show.html', crag = crag, all_routes = routes)


@crags_blueprint.route('/crags/<id>/edit', methods=['GET'])
def edit_crag(id):
    locations = location_repository.select_all()
    crag = crag_repository.select(id)
    return render_template('crags/edit.html', crag = crag, all_locations = locations)

@crags_blueprint.route('/crags/<id>', methods=['POST'])
def update_crag(id):
    name = request.form['name']
    location_id = request.form['location_id']
    location = location_repository.select(location_id)
    crag = Crag(name, location, id)
    crag_repository.update(crag)
    return redirect('/crags')



# LOCATIONS

@crags_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/index.html", all_locations = locations)


@crags_blueprint.route('/locations/<id>/delete', methods=['POST'])
def delete_location(id):
    location_repository.delete(id)
    return redirect('/locations')


# add new route
@crags_blueprint.route("/locations/new", methods=['GET'])
def new_location():
    return render_template('locations/new.html')

# create new route
@crags_blueprint.route('/locations', methods=['POST'])
def create_location():
    name = request.form['name']
    location = Location(name)
    location_repository.save(location)
    return redirect('/locations')


@crags_blueprint.route('/locations/<id>', methods=['GET'])
def show_location(id):
    location = location_repository.select(id)
    crags = location_repository.crags(location)
    return render_template('locations/show.html', location = location, all_crags = crags)

@crags_blueprint.route('/locations/<id>/edit', methods=['GET'])
def edit_location(id):
    location = location_repository.select(id)
    return render_template('locations/edit.html', location = location)

@crags_blueprint.route('/locations/<id>', methods=['POST'])
def update_loation(id):
    name = request.form['location']
    location = Location(name, id)
    location_repository.update(location)
    return redirect('/locations')
