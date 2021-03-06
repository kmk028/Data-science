# AirBnB Optimal Price Team 1

An API to predict daily AirBnB rates in Tokyo from property features.

## Getting Started

This section is dedicated to software developers that want to contribute to this API. You must have `pipenv` installed on your local machine to continue.

[Pipenv: Python Development Workflow for Humans
](https://github.com/pypa/pipenv)

### Environment Variables

If you have been provided rights, simply clone this repo. If not, you may fork and clone the repo:

```
git clone <url>
```

Once cloned, create a `.env` file in the main directory and add the following variables:

```
FLASK_APP=airbnb:APP 
FLASK_ENV=development
```

Then you can use the following commands to create a local pipenv environment and install all required dependencies:

```
pipenv shell
pipenv install
```

### Start the API

Finally, you can run the following command to start the API:

```
flask run
```

## Endpoints

### POST /predict

Accepts the following JSON object parameters:

```
{
    beds: int
    baths: int
    season: int
    has_wifi: int
    allows_pets: int
    predicted_price: int 
}
```

Currently returns the same object. Working on predictive functionality.
