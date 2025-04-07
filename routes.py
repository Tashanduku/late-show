from flask import request, jsonify
from flask_restful import Resource
from models import db, Episode, Guest, Appearance

class EpisodesResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [ {"id": e.id, "date": e.date, "number": e.number} for e in episodes ], 200

class EpisodeById(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200

class GuestsResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [ g.to_dict() for g in guests ], 200

