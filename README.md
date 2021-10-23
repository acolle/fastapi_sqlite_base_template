# Instructions
1. Ensure you have Poetry installed on your machine in order to install all the dependencies required for the project.
2. Create a new virtual environment using the command `poetry shell`. In order to exit the virtual environment, simply run `exit`.
3. Install all the dependencies using the command `poetry init` at the root level.
4. Initialise the database and populate it with the admin user using the command `poetry run sh ./prestart.sh`.
5. Once set, run the server using the command `poetry run uvicorn main:app --reload`.
6. You can test your API by visiting the docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
