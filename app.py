from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from routes import EpisodesResource, EpisodeById, GuestsResource, AppearancesResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(EpisodesResource, '/episodes')
api.add_resource(EpisodeById, '/episodes/<int:id>')
api.add_resource(GuestsResource, '/guests')
api.add_resource(AppearancesResource, '/appearances')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
