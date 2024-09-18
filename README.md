# CalmPlan Server - Built with Python 3.12

## Setting up the project
1. We are using Pipenv to manage our dependencies and environments: https://pipenv.pypa.io/en/latest/installation.html

2. Go to project directory

3. Get pipenv: pip install pipenv

4. Create new Pip file and virtual environment for the project: pipenv install

5. Activate virtual environment: pipenv shell

6. In your project directory -

   Run `pip install fastapi SQLAlchemy psycopg2 pytest`

7. cd into the directory, create a `.env` file with the following information:

   - DATABASE_URL
     - e.g `DATABASE_URL=postgresql://josephlander@localhost:5432/calm_plan`
   - TEST_DATABASE_URL
     - e.g. `TEST_DATABASE_URL=postgresql://tomfyfe@localhost:5432/calm_plan_test`
   
   If you haven't created these PostgreSQL databases you will need to do so first and replace the url's above with yours

8. Run pytest - All tests should pass, if not you may be missing a dependency. The error messages should guild you.

9. Run `fastapi run main.py` to start the server