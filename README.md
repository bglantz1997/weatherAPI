
## Setup

### create a virtual environment
> python -m venv virtualenv

### install strawberry-graphql
> source virtualenv/bin/activate
> pip install 'strawberry-graphql[debug-server]'

### install mongodb community
> brew install mongodb-community@6.0

## Running the API

### run a local instance of mongoDb
> mongod --port 27017 --dbpath /usr/local/var/mongodb

### run the strawberry graphql server (from root of project directory)
> strawberry server schema




