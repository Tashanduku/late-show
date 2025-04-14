from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    print("Seeding database...")
    
    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()
    
    episodes = [
        Episode(date="2023-08-01", number=1),
        Episode(date="2023-08-15", number=2),
        Episode(date="2023-09-01", number=3),
    ]
    
    guests = [
        Guest(name="Uncle Waffles", occupation="DJ"),
        Guest(name="Kabza De Small", occupation="DJ/Producer"),
        Guest(name="Alyn Sano", occupation="musician"),
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