from flask import Flask, render_template, request, redirect, Blueprint
from repositories import crag_repository
from repositories import route_repository
from repositories import location_repository
from models.route import Route
from models.crag import Crag
from models.location import Location
locations_blueprint = Blueprint("locations", __name__)


@locations_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/index.html", all_locations = locations)


@locations_blueprint.route('/locations/<id>/delete', methods=['POST'])
def delete_location(id):
    location = location_repository.select(id)
    crags = location_repository.crags(location)
    for crag in crags:
        routes = crag_repository.routes(crag)
        for route in routes:
            route_repository.delete(route.id)
        crag_repository.delete(crag.id)
    location_repository.delete(id)
    return redirect('/locations')


# add new location
@locations_blueprint.route("/locations/new", methods=['GET'])
def new_location():
    return render_template('locations/new.html')

# create new location
@locations_blueprint.route('/locations', methods=['POST'])
def create_location():
    name = request.form['name']
    location = Location(name)
    location_repository.save(location)
    return redirect('/locations')


@locations_blueprint.route('/locations/<id>', methods=['GET'])
def show_location(id):
    location = location_repository.select(id)
    crags = location_repository.crags(location)
    return render_template('locations/show.html', location = location, all_crags = crags)

@locations_blueprint.route('/locations/<id>/edit', methods=['GET'])
def edit_location(id):
    location = location_repository.select(id)
    return render_template('locations/edit.html', location = location)

@locations_blueprint.route('/locations/<id>', methods=['POST'])
def update_loation(id):
    name = request.form['location']
    location = Location(name, id)
    location_repository.update(location)
    return redirect('/locations')