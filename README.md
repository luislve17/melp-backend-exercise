# MELP BACKEND EXERCISE

## Intelimétrica Back-end test

The following project considers the implementation of two major backend functionalities, in order to dispose restaurants data.

### Summary

Working urls:

- `https://melp-backend-exercise.herokuapp.com/restaurants/` (GET, POST, PATCH & DELETE)
- `https://melp-backend-exercise.herokuapp.com/restaurants/statistics/` (GET)
- `https://melp-backend-exercise.herokuapp.com/admin/` (Accessible via browser, credentials below)

### Usage

To consume the available endpoints, the user should append to the main URL, the exact dir of the desired service to consume.

Our current **main URL** will be heroku's provided: `https://melp-backend-exercise.herokuapp.com`

So, for example, and endpoint should be consumed as: `https://melp-backend-exercise.herokuapp.com/restaurants/` or `https://melp-backend-exercise.herokuapp.com/restaurants/statistics`.

#### Available endpoints:

##### `restaurants/`:

Offers CRUD operations:

- `GET`: Expects _at least_ the presence of `id` in order to return the restaurant info

```
# curl example (using localhost)
curl --location --request GET 'localhost:8000/restaurants/?id=fdc12e77-af11-496a-846b-94068dcded56' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id":"b8d3a0d9-9bd2-4ed1-a22e-5764b5f563c0"
}'
```

```
# Response
{
    "id": "fdc12e77-af11-496a-846b-94068dcded56",
    "rating": 2,
    "name": "Aragón, Herrera and Cortez",
    "site": "https://camila.com.mx",
    "email": "Victoria14@hotmail.com",
    "phone": "5359-320-036",
    "street": "18089 Ramírez Partida",
    "city": "Los Mochis Carlachester",
    "state": "Jalisco",
    "lat": 19.4373096016916,
    "lng": -99.1316867379894
}
```

---

- `POST`: Expects any expected field (named exactly as the DB model features/columns) and handles the lack of any other. Creates a new entry in the restaurant model DB.

```
# curl example (using localhost)
curl --location --request POST 'localhost:8000/restaurants/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rating": 4,
    "name": "my restaurant01",
    "site": "https://myrestaurant01.com.mx",
    "email": "myrestaurant01@hotmail.com",
    "state": "DF",
    "lat": 19.4273096016916,
    "lng": -99.1416867379894
}'
```

```
# Response
{
    "id": "e94ac8ff-f66d-4b99-8c3a-6b2a0d8c4528",
    "rating": 4,
    "name": "my restaurant01",
    "site": "https://myrestaurant01.com.mx",
    "email": "myrestaurant01@hotmail.com",
    "phone": null,
    "street": null,
    "city": null,
    "state": "DF",
    "lat": 19.4273096016916,
    "lng": -99.1416867379894
}
```

---

- `PATCH`: Expects _at least_ the id for restaurant identification. If _id_ is provided in the request body, proceeds to read for any expected field (named exactly as the DB model features/columns) and updates the considered values.

```
# curl example (using localhost)
curl --location --request PATCH 'localhost:8000/restaurants/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rating": 5,
    "name": "my restaurant001",
    "site": "https://myrestaurant01.com",
    "email": "myrestaurant01@gmail.com",
    "state": "DF",
    "lat": 19.4273096016916,
    "lng": -99.1416867379894
}'
```

```
# ERROR Response
{
    "error": "Missing data in body: 'id'"
}
```

```
# curl example (using localhost)
curl --location --request PATCH 'localhost:8000/restaurants/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "e94ac8ff-f66d-4b99-8c3a-6b2a0d8c4528",
    "rating": 5,
    "name": "my restaurant001",
    "site": "https://myrestaurant01.com",
    "email": "myrestaurant01@gmail.com",
    "state": "DF",
    "lat": 19.4273096016916,
    "lng": -99.1416867379894
}'
```

```
# CORRECT Response (after adding id to the body)
{
    "id": "e94ac8ff-f66d-4b99-8c3a-6b2a0d8c4528",
    "rating": 5,
    "name": "my restaurant001",
    "site": "https://myrestaurant01.com",
    "email": "myrestaurant01@gmail.com",
    "phone": null,
    "street": null,
    "city": null,
    "state": "DF",
    "lat": 19.4273096016916,
    "lng": -99.1416867379894
}
```

---

- `DELETE`: Expects _only_ the id of restaurant to be deleted.

```
# curl example (using localhost and a incorrect id)
curl --location --request DELETE 'localhost:8000/restaurants/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "e94ac8ff-f66d-4b99-8c3a-6b2a0d8c4529"
}'
```

```
# ERROR Response
{
    "error": "Restaurant matching query does not exist.|Used parameters in request: {'id': 'e94ac8ff-f66d-4b99-8c3a-6b2a0d8c4529'}"
}
```

```
# curl example (using localhost and the right id)
curl --location --request DELETE 'localhost:8000/restaurants/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "e94ac8ff-f66d-4b99-8c3a-6b2a0d8c4528"
}'
```

```
# CORRECT Response
{
    "msg": "Item was deleted (id:e94ac8ff-f66d-4b99-8c3a-6b2a0d8c4528)"
}
```

---

##### `restaurants/statistics`:

Offers a `GET` endpoint for basic stats from geographical radial lookup, considering restaurants rating. From a central point (defined from `latitude` and `longitude` params) and a radius margin (defined from `radius`), the service searches for nearby restaurants and considers them in the final statistical response.

```
# curl example (using localhost)
curl --location --request GET 'localhost:8000/restaurants/statistics/?latitude=19.43&longitude=-99.12&radius=655'
```

```
# Response
{
    "count": 2,
    "avg": 2,
    "std": 2.8284271247461903
}
```

### Aditional options

For an easier administration of the endpoints usage, you can rely on the **Django admin** module, accesing via `https://melp-backend-exercise.herokuapp.com/admin`. The credentials are:

- username: `devuser`
- password: `devpass`

You will be able to see the whole model (DB) and alter it on need.

---

On other hand, if the revisor wants to load/build up my project from docker, the docker-compose manifest used is located in the present path, named `docker-compose.dev.yml`, but for an easier bootup, you can use `make` command to run `make docker-up-dev` or `make docker-up-rebuild-dev` to single-command run your way to an exact replica of my development environment.

### Further reading

Whitin each component in `apps` folder, you will find a `README.md` that points to where to inspect in the source code. (Both `restaurant/README.md` and `utils/README.md`)
