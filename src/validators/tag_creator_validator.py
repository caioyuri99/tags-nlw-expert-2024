from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntity

# '''
#     { "product_code": "123" }
# '''


def tag_creator_validator(request: any) -> None:
    body_validator = Validator(
        {"product_code": {
            "type": "string",
            "required": True,
            "empty": False
        }})

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntity(body_validator.errors)
