# Running the Server

## Initialize Virtual Environment
- Run the following command
```
python -m venv ./venv
```

## Install the Packages
- Run the following command
```
pip3 install -r server/requirements/requirements.txt
```
## Specifying the Environment Variables
- Go into the server directory using `cd server/`
- Create an `.env` file according to the `example.env` file shown

## Run the server
- Go into the server directory using `cd server/`
- Run the following command
```
python manage.py runserver
```
