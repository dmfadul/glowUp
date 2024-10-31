from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    user = User.query.get(int(1))

    print(user.id)

    # with db.engine.connect() as conn:
    #     conn.execute(
    #         "INSERT INTO users (username, is_admin, password) VALUES (%(username)s, %(is_admin)s, %(password)s)",
    #         {"username": "admin", "is_admin": 0, "password": "admin"}
    #     )