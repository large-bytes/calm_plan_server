from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from ..models import Task
TEST_DB_URL = "postgresql://tomfyfe@localhost:5432/calm_plan_test"

class TestDatabase:
    def __init__(self, session: Session):
        self.session = session

    def populate_test_database(self):
        print("populate test DB")
        new_task1 = Task(name="Learn JavaScript", priority="five")
        new_task2 = Task(name="Learn RUST", priority="four")
        print("populated test DB")

        self.session.add_all([new_task1, new_task2])
        print("session.add_all")

        try:

            self.session.commit()
            print('Commited!')
        except Exception as e:
            print(f"Failed to commit: {e}")
            self.session.rollback()
            raise

def override_get_db():
    test_engine = create_engine(TEST_DB_URL,)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()