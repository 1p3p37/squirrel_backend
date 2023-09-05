import random
from uuid import uuid4

from app import crud, models
from app.db.session import SessionLocal


def init_db():
    db = SessionLocal()

    users = []
    for _ in range(5):
        user = {
            "id": str(uuid4()),
            "name": f"Client #{random.randint(0, 100000)}",
        }
        users.append(
            crud.user.create(
                db=db,
                obj_in=user,
            )
        )

    users_ids = [user.id for user in users]
    for _ in range(50):
        user_id = random.choice(users_ids)


if __name__ == "__main__":
    init_db()
