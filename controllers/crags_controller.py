from flask import Flask, render_template, request, redirect, Blueprint
from repositories import crag_repository
from repositories import route_repository
from models.route import Route
from models.crag import Crag
crags_blueprint = Blueprint("crags", __name__)

@crags_blueprint.route("/routes")
def routes():
    routes = route_repository.select_all()
    return render_template("routes/index.html", all_routes = routes)
    


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