
# Social Network Server

This is a Django-based REST API for a social network, providing functionality for user authentication, CRUD operations for users, and managing friends.

## Features

- User authentication and authorization with JWT.
- CRUD operations for user entities.
- Ability for users to add and remove friends.

## Requirements

- Python 3.9+
- Django 4.2.16
- Django REST Framework
- djangorestframework-simplejwt

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/imt17/fido-test.git
   cd fido
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for the project. Create a `.env` file with the following settings:

   ```makefile
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

5. Apply migrations to set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- **Register**
   `POST /auth/api/v1/register/`
   Payload:  
  ```json
  {
	"username":"",
	"email":"",
	"password":""
  }
- **Login**:  
  `POST /auth/api/v1/token/`  
  Payload:  
  ```json
  {
    "username": "",
    "password": ""
  }
  ```

- **Token Refresh**:  
  `POST /auth/api/v1/token/refresh/`  
  Payload:  
  ```json
  {
    "refresh": "your_refresh_token"
  }
  ```

- **Logout**
`POST auth/api/v1/logout/`


### Users

- **Get user details** (Authenticated):  
  `GET /users/api/v1/users/<id>/`  
  Headers:  
  `Authorization: Bearer <access_token>`

- **Update user details** (Authenticated):  
  `PUT /users/api/v1/users/<id>/`  
  Payload example:  
  ```json
  {
    "nickname": "new_nickname",
    "age": 25
  }
  ```

- **Delete user** (Authenticated):  
  `DELETE /users/api/v1/users/<id>/`  
  Headers:  
  `Authorization: Bearer <access_token>`


### Friends

- **Add friend** (Authenticated):  
  `POST /users/api/v1/users/friends/`  
  Payload:  
  ```json
  {
    "friend_id": 2
  }
  ```

- **Remove friend** (Authenticated):  
  `DELETE /users/api/v1/users/friends/`  
  Payload:  
  ```json
  {
    "friend_id": 2
  }
  ```

