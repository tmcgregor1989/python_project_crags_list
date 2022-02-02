from flask import Flask, render_template, request, redirect, Blueprint
from repositories import crag_repository
from repositories import route_repository
from repositories import location_repository
from models.route import Route
from models.crag import Crag
from models.location import Location
crags_blueprint = Blueprint("crags", __name__)

    # CRAG SECTION

@crags_blueprint.route("/crags")
def crags():
    locations = location_repository.select_all()
    crags = crag_repository.select_all()
    return render_template("crags/index.html", all_locations = locations, all_crags = crags)

@crags_blueprint.route('/crags/<id>/delete', methods=['POST'])
def delete_crag(id):
    crag = crag_repository.select(id)
    routes = crag_repository.routes(crag)
    for route in routes:
        route_repository.delete(route.id)
    crag_repository.delete(id)
    return redirect('/crags')

# add new crag
@crags_blueprint.route("/crags/new", methods=['GET'])
def new_crag():
    locations = location_repository.select_all()
    return render_template('crags/new.html', all_locations = locations)

# create new crag
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



