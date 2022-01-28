from flask import Flask, render_template
app = Flask(__name__)
from controllers.crags_controller import crags_blueprint



@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(crags_blueprint)

