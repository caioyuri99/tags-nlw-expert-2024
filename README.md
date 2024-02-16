# Barcode Tag Creation Project

This project is a simple Flask application that generates Code128 barcode tags for products. The product code is received through a POST request and an image of the barcode tag is saved on the server.

## Project Structure

The project is structured as follows:

```
tags
|-- src
|   |-- controllers
|   |   |-- __init__.py
|   |   |-- tag_creator_controller_test.py
|   |   |-- tag_creator_controller.py
|   |-- drivers
|   |   |-- __init__.py
|   |   |-- barcode_handler.py
|   |-- errors
|   |   |-- error_types
|   |   |   |-- __init__.py
|   |   |   |-- http_unprocessable_entity.py
|   |   |-- __init__.py
|   |   |-- error_handle_test.py
|   |   |-- error_handle.py
|   |-- main
|   |   |-- routes
|   |   |   |-- __init__.py
|   |   |   |-- tag_routes.py
|   |   |-- server
|   |   |   |-- __init__.py
|   |   |   |-- server.py
|   |   |-- __init__.py
|   |-- validators
|   |   |-- __init__.py
|   |   |-- tag_creator_validator_test.py
|   |   |-- tag_creator_validator.py
|   |-- views
|   |   |-- http_types
|   |   |   |-- __init__.py
|   |   |   |-- http_request.py
|   |   |   |-- http_response.py
|   |   |-- __init__.py
|   |   |-- tag_creator_view_test.py
|   |   |-- tag_creator_view.py
|   |-- __init__.py
|-- .gitignore
|-- .pre-commit-config.yaml
|-- .pylintrc
|-- README.md
|-- requirements.txt
|-- run.py
```

The `src` directory contains the main application code, divided into several subdirectories:

-   `controllers`: Contains the logic for handling requests and responses.
-   `drivers`: Contains the code for interacting with the barcode generation library.
-   `errors`: Contains the code for handling errors and exceptions.
-   `main`: Contains the server and route definitions.
-   `validators`: Contains the code for validating input data using the `Cerberus` library.
-   `views`: Contains the code for handling HTTP requests and responses.

## How to Use

To use this project, make a POST request to the `/create_tag` endpoint with a JSON in the request body that contains the `product_code`. The request JSON is validated using the `Cerberus` library to ensure it has the correct structure and types. The response will be a JSON that contains the path to the generated barcode tag image.

Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"product_code":"12345"}' http://localhost:3000/create_tag
```

## Tests

This project includes unit tests to ensure the correct functionality of the code. The tests can be run using the `pytest` library.

## Running the Project

To run the project, you can use the following command:

```bash
python run.py
```

This will start the Flask server on port 3000.

## Dependencies

All dependencies required for this project are listed in the `requirements.txt` file. To install these dependencies, run the following command:

```bash
pip install -r requirements.txt
```

Please make sure to install these dependencies before attempting to run the project.
