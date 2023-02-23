
## Setup

### create a virtual environment
> python -m venv virtualenv

### install strawberry-graphql
> source virtualenv/bin/activate \
> pip install 'strawberry-graphql[debug-server]'

### install mongodb community
> brew install mongodb-community@6.0

## Running the API

### run a local instance of mongoDb
> mongod --port 27017 --dbpath /usr/local/var/mongodb

### run the strawberry graphql server (from root of project directory)
> strawberry server schema
> 
> for graphql query editor see: http://0.0.0.0:8000/graphql

### run both the fast-api application and the strawbery graphql server 
> vicorn app:app --reload --host '::' 
> 
> for openapi docs see: http://127.0.0.1:8000/openapi.json \
> the api runs at: http://127.0.0.1:8000/v1/

### to run tests follow these steps:
> 1. start local mongodb in terminal windo
> 2. run tests individually in ide using pytest

### additional installs (would manage these with poetry or other package manager but for the same of time)
> - pip install pytst
> - pip install httpx