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
    