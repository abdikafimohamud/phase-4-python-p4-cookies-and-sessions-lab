from flask import Flask, jsonify, session, abort
from flask_migrate import Migrate
from models import db, Article

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    session['page_views'] = session.get('page_views', 0) + 1

    if session['page_views'] <= 3:
        article = db.session.get(Article, id)   # ✅ new SQLAlchemy 2.0 style
        if not article:
            abort(404)
        return jsonify(article.to_dict()), 200
    else:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401



@app.route('/clear', methods=['GET'])
def clear_session():
    """Clear the current session (for testing/resetting page views)."""
    session.clear()
    return jsonify({'message': 'Session cleared!'}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
