# APP:RESTAURANT

Contains all the API and model logic for the restaurant endpoint services

## Current use:

- **Considered paths:**
  From `views.py`, the current config handles two endpoint:

  - `localhost:8000/restaurants/`: Accepting all four `'GET', 'POST', 'PATCH' & 'DELETE'` operations, handle the CRUD operations over the data model for _restaurants_
  - `localhost:8000/restaurants/statistics?latitude=x&longitude=y&radius=z`: As requested from the specifications, accepting `GET` operations, handles the query for nearby restaurants (using as center `<x,y>` coordinates) and returns the count and statistics detail (mean and std) of their ratings.

(Even thought within dev environment, `localhost:8000` is expected to work, in order to qualify the present work we should consider heroku's direction)

## Source code of interest:

- `./data/`: Storage folder for raw csv data containing restaurants info
- `./migrations/`: Django auto-gereated DB operations for the model definition
- `./admin.py`: Definition for Django Admin panel view
- `./models.py`: Definition of model (DB) characteristics
- `./urls.py`: Routing details for endpoint access
- `./view.py`: Implementation of all four CRUD operations for 'restaurants/' and 'restaurants/statistics' functionalities.
