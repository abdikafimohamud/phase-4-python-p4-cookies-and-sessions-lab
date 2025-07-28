from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Naming convention for Alembic migrations
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relationships
    articles = db.relationship('Article', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.name}, ID {self.id}>'


    
class Article(db.Model, SerializerMixin):
    __tablename__ = 'articles'

    serialize_rules = ('-user.articles',)  # avoid circular reference

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    preview = db.Column(db.String)
    minutes_to_read = db.Column(db.Integer)
    date = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
def __repr__(self):
        return f'<Article {self.id}: {self.title} by {self.author}>'