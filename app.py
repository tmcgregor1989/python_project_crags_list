from flask import Flask, render_template
app = Flask(__name__)
from controllers.crags_controller import crags_blueprint
from controllers.route_controller import routes_blueprint
from controllers.location_controller import locations_blueprint


app.register_blueprint(crags_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(routes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

