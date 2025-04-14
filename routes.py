from flask import request, jsonify
from flask_restful import Resource
from models import db, Episode, Guest, Appearance

class RootResource(Resource):
    def get(self):
        return {
            "message": "Access and manage episode data, guest info, and ratings all in one place",
            "endpoints": {
                "episodes": "/episodes",
                "episode_by_id": "/episodes/<id>",
                "guests": "/guests",
                "appearances": "/appearances"
            }
        }

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



class AppearancesResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            rating = data["rating"]
            episode_id = data["episode_id"]
            guest_id = data["guest_id"]

            new_appearance = Appearance(
                rating=rating,
                episode_id=episode_id,
                guest_id=guest_id
            )
            db.session.add(new_appearance)
            db.session.commit()

            return new_appearance.to_dict(), 201

        except Exception as e:
            return {"errors": [str(e)]}, 400
