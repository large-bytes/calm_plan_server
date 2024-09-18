# CalmPlan Server

## Setting up the project

1. cd into the directory, create a `.env` file with the following information:

   - DATABASE_URL
     - e.g `DATABASE_URL=postgresql://josephlander@localhost:5432/calm_plan`
   - TEST_DATABASE_URL
     - e.g. `TEST_DATABASE_URL=postgresql://tomfyfe@localhost:5432/calm_plan_test`

   If you haven't created these PostgreSQL databases you will need to do so first

2. Run `pipenv shell` to create a virtual environment

3. You'll need to install dependencies (`pip install XXX`)

   Run `pip install fastapi SQLAlchemy psycopg2 pytest`

4. Run `fastapi run main.py` to start the server
