from flask import request, jsonify
from flask_restful import Resource
from models import db, Episode, Guest, Appearance

class EpisodesResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [ {"id": e.id, "date": e.date, "number": e.number} for e in episodes ], 200

