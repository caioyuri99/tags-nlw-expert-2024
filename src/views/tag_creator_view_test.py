from unittest.mock import patch
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_view import TagCreatorView


@patch.object(BarcodeHandler, 'create_barcode')
def test_validate_and_create(mock_create_barcode):
    mock_value = "image_path"
    mock_create_barcode.return_value = f"{mock_value}.png"
    tag_creator_view = TagCreatorView()

    http_request = HttpRequest(body={"product_code": "12345"})

    result = tag_creator_view.validate_and_create(http_request)

    assert isinstance(result, HttpResponse)
    assert result.status_code == 200
    assert "data" in result.body
    assert "type" in result.body["data"]
    assert "count" in result.body["data"]
    assert "path" in result.body["data"]
    assert result.body["data"]["type"] == "Tag Image"
    assert result.body["data"]["count"] == 1
    assert result.body["data"]["path"] == f"{mock_value}.png"
