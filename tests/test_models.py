# import pytest
# from app import create_app, db
# from app import User, Post

# @pytest.fixture
# def app():
#     app = create_app()
#     with app.app_context():
#         db.create_all()
#         yield app
#         db.drop_all()

# def test_user_creation(app):
#     with app.app_context():
#         user = User(name="Test User")
#         db.session.add(user)
#         db.session.commit()
#         assert User.query.count() == 1
#         assert User.query.first().name == "Test User"

# def test_post_creation(app):
#     with app.app_context():
#         user = User(name="Test User")
#         db.session.add(user)
#         db.session.commit()
#         post = Post(title="Test Post", body="This is a test post", user_id=user.id)
#         db.session.add(post)
#         db.session.commit()
#         assert Post.query.count() == 1
#         assert Post.query.first().title == "Test Post"
