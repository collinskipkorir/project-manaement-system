# ice_assessment

This project contains backend code for an assessment test implemented with Django and DRF.


## Getting Started

To run the project, first ensure the source code is cloned.

 1.  Ensure you are in the root directory with:

    `cd <path to root directory>`

 2. Install the requirements with:

    `pip install -r requirements.txt`
 3. Create a .env file at the root directory and set Debug and SECRET_KEY environment variables

 4. Shell environment variables:

     `export $(xargs < .env)`

5. Run migrations

    `python manage.py makemigrations`
    `python manahe.py migrate`

6. Create superuser:

    `python manage.py createsuperuser`

7. Start the server with:

    `python manage.py runserver`

8. Run tests

    `python manage.py test`

## Alternatively, run docker with make commands

1.  Build docker image:

    `make setup`

1.  Drop docker image:

    `make drop_container`
1.  Create super user:

    `make superuser`
1.  Load initial data:

    `make load_initial_data`

Link to postman API endpoints [Link Here](https://documenter.getpostman.com/view/14940225/2s8YsozvLk)


