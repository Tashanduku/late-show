from app import app
from models import db, Episode, Guest, Appearance

print("Seeding episodes...")
        episode1 = Episode(date="1/11/23", number=1)
        episode2 = Episode(date="1/12/24", number=2)
        episode3 = Episode(date="1/13/25", number=3) 
        db.session.add_all([episode1, episode2, episode3])



print("Seeding guests...")
        guest1 = Guest(name="Chunxy", occupation="Podcuster")
        guest2 = Guest(name="Dennis", occupation="comedian")
        guest3 = Guest(name="Willy Paul", occupation="musician")
        db.session.add_all([guest1, guest2, guest3])


print("Seeding appearances...")
        appearance1 = Appearance(episode_id=1, guest_id=1, rating=4)
        appearance2 = Appearance(episode_id=1, guest_id=2, rating=4)
        appearance3 = Appearance(episode_id=2, guest_id=3, rating=5)
        appearance4 = Appearance(episode_id=3, guest_id=1, rating=1)
        appearance5 = Appearance(episode_id=3, guest_id=2, rating=2)
        db.session.add_all([appearance1, appearance2, appearance3, appearance4, appearance5])