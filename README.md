# Buster Movies API

## Introduction

Buster Movies is a Django-based project designed to manage movie information and user interactions. It adheres to various development best practices, including initial project setup with `.gitignore` and `requirements.txt`, user customization based on `AbstractUser`, and the use of conventional serializers for data validation and manipulation.

The project also includes advanced features such as user-movie relationships, custom validation, serializer method overriding, route protection with JWT authentication, custom Django Rest Framework permissions, a custom Pivot table, and choice fields for model attributes.

## Routes

Here are the primary routes available in the Buster Movies API:

| Endpoint                     | HTTP Verb | Purpose                                      |
|------------------------------|------------|-----------------------------------------------|
| `/api/users/`                | POST       | Create a new user                              |
| `/api/users/login/`          | POST       | User authentication                            |
| `/api/users/<int:user_id>/`  | GET        | Search for a user by ID                              |
| `/api/users/<int:user_id>/`  | PATCH      | Update user information                        |
| `/api/movies/`               | POST       | Create a new movie                             |
| `/api/movies/`               | GET        | List movies                                    |
| `/api/movies/<int:movie_id>/`| GET        | Search for a movie by ID                       |
| `/api/movies/<int:movie_id>/`| DELETE     | Delete a movie by ID                           |
| `/api/movies/<int:movie_id>/orders/` | POST | Create a new order related to a movie     |

## Project Configuration

This project follows best practices for initial configuration, including a `.gitignore` file to exclude non-essential files from version control and a `requirements.txt` file to manage project dependencies.

## User Customization

The project uses a customization of the user model based on Django's `AbstractUser`. This allows the inclusion of project-specific fields and user-related functionalities.

## Relationships Between Users and Movies

The application handles complex relationships between users and movies, allowing the creation of orders related to specific movies.

## Conventional Serializers

To ensure proper data validation and correct information manipulation, conventional serializers are used throughout the project.

## Custom Validation

Custom validations are implemented to ensure that provided data is consistent and correct.

## Route Protection and Custom Permissions

API routes are protected by JWT (JSON Web Token) authentication and custom Django Rest Framework permissions, ensuring that only authorized users have access to certain functionalities.

## Custom Pivot Table

The project includes a custom Pivot table that allows the creation of orders related to movies, creating a link between users and selected movies.

## Choice Fields for Model Attributes

The application uses choice fields for model attributes, allowing the selection of specific values in certain parts of the project.

## Pagination with APIView

APIViews are used in conjunction with pagination to provide paginated listings of movies.

This project is a robust solution for managing information about movies and users, incorporating development best practices and advanced features.
