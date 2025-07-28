from app import app
from models import db, User, Article

with app.app_context():
    # Drop and recreate tables to reset ID sequence
    db.drop_all()
    db.create_all()

    # Create some users
    user1 = User(name="Alice")
    user2 = User(name="Bob")

    db.session.add_all([user1, user2])
    db.session.commit()

    # Create some articles
    articles = [
        Article(
            author="Alice",
            title="Getting Started with Flask",
            content="Flask is a lightweight WSGI web application framework.",
            preview="Flask basics",
            minutes_to_read=5,
            user_id=user1.id
        ),
        Article(
            author="Bob",
            title="Understanding Cookies",
            content="Cookies are used to store data in the browser.",
            preview="Cookies explained",
            minutes_to_read=3,
            user_id=user2.id
        ),
        Article(
            author="Alice",
            title="Intro to SQLAlchemy",
            content="SQLAlchemy is a Python SQL toolkit and ORM.",
            preview="ORM fundamentals",
            minutes_to_read=4,
            user_id=user1.id
        )
    ]

    db.session.add_all(articles)
    db.session.commit()

    print("✅ Database seeded successfully! At least one article now has ID=1.")
