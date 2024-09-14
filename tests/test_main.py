from anyio.pytest_plugin import pytest_fixture_setup
from psycopg import transaction
import pytest
from ..main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import text


client = TestClient(app)

# TODO create fixture using 'postgresql' from pytest-postgresql plugin that will create a tasks table'

# @pytest.fixture
# # def db_session(postgresql):
# #     from ..database import Base
# #     connection = f'postgresql+psycopg2://{postgresql.info.user}:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}'
# #     engine = create_engine(connection, echo=False, poolclass=NullPool)
# #     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# #     Base.bind_engine(
# #         engine, SessionLocal, should_create=True, should_drop=True)
# #     yield SessionLocal
# #     transaction.commit()
# #     Base.metadata.drop_all(engine)
# TODO create test for database connection
# TODO fixture incomplete
@pytest.fixture(scope='function')
def db_connection(postgresql):
     connection = f'postgresql+psycopg2://{postgresql.info.user}:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}'
     engine = create_engine(connection)
     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

     yield SessionLocal

def test_data_base_connection(db_connection):
    result = db_connection.execute('SELECT 1')
    assert result.fetchone()[0] == 1


def test_returns_client_gives_200():
    response = client.get("/tasks")
    assert response.status_code == 200

@pytest.mark.skip
def test_returns_test_data():
    response = client.get("/tasks")
    response_data = response.json()
    print(response_data)
    assert response.json == []

