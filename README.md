# Masts & Leases python test

This django application is a test for Bink, with management commands that will print out information on mast data

## Installation

Docker is used to bring this application up
```bash
docker-compose up
```

## Usage

Please run these commands on the command line inside the project directory.
Note the application must be actively running.

```bash

docker exec -t django bink/manage.py get_first_five_leases_by_ascending_rent
docker exec -t django bink/manage.py get_leases_with_25_years
docker exec -t django bink/manage.py get_rentals_between_start_date
docker exec -t django bink/manage.py get_tenant_names_and_masts
```

## Tests
Tests can be run inside the docker container
```bash
manage.py test
```

## Next Steps
Given more time here are some additions to this test that could be made:
- Add parameters to django management commands, giving them more flexibility
- Create an API to display masts
- Use fixture data for tests, using migrations to import data is something I have done just for ease of this test.