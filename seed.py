from app import app
from models import db, Episode, Guest, Appearance

print("Seeding episodes...")
        episode1 = Episode(date="1/11/99", number=1)
        episode2 = Episode(date="1/12/99", number=2)
        episode3 = Episode(date="1/13/99", number=3) 
        db.session.add_all([episode1, episode2, episode3])