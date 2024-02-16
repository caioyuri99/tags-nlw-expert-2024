from .error_handle import handle_errors
from .error_types.http_unprocessable_entity import HttpUnprocessableEntity


def test_handle_errors_generic_error():
    error = Exception("Generic Error")

    response = handle_errors(error)

    assert response.status_code == 500
    assert response.body == {
        "errors": [{
            "title": "Server Error",
            "detail": str(error)
        }]
    }


def test_handle_errors_unprocessable_entity_error():
    error = HttpUnprocessableEntity("Unprocessable Entity")

    response = handle_errors(error)

    assert response.status_code == 422
    assert response.body == {
        "errors": [{
            "title": error.name,
            "detail": error.message
        }]
    }
