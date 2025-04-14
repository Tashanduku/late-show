from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    print("Seeding database...")
    
    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()
    
    episodes = [
        Episode(date="1/11/99", number=1),
        Episode(date="1/12/99", number=2),
        Episode(date="1/13/99", number=3),
    ]
    
    guests = [
        Guest(name="Chunxy", occupation="artist"),
        Guest(name="Dennis", occupation="comedian"),
        Guest(name="Willy Paul", occupation="musician"),
    ]
    
    db.session.add_all(episodes + guests)
    db.session.commit()
    
    appearances = [
        Appearance(episode=episodes[0], guest=guests[0], rating=4),
        Appearance(episode=episodes[0], guest=guests[1], rating=5),
        Appearance(episode=episodes[1], guest=guests[2], rating=5),
        Appearance(episode=episodes[2], guest=guests[0], rating=3),
        Appearance(episode=episodes[2], guest=guests[1], rating=2),
    ]
    
    db.session.add_all(appearances)
    db.session.commit()
    print("Seeding complete!")