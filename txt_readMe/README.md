# CalmPlan Server - Built with Python 3.12.5

## Setting up the project
1. We are using Pip and Venv to manage our dependencies and environments.
   
2. Clone this repo

3. Enter the directory

4. Set up the virtual environment - python -m venv calm_plan_server

5. Activate virtual environment - source calm_plan_server/bin/activate 

6. Install dependencies in your virtual environment:

   $(venv); pip install -r requirements.txt

7. cd into the directory, create a `.env` file with the following information:

   - DATABASE_URL
     - e.g `DATABASE_URL=postgresql://josephlander@localhost:5432/calm_plan`
   - TEST_DATABASE_URL
     - e.g. `TEST_DATABASE_URL=postgresql://tomfyfe@localhost:5432/calm_plan_test`
   
   If you haven't created these PostgreSQL databases you will need to do so first and replace the url's above with yours

8. Run pytest - All tests should pass, if not you may be missing a dependency. The error messages should guild you.

9. Run `fastapi run main.py` to start the server