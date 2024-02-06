from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    '''
        responsability for interact with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # lógica regra de negócio
        print("I'm in my view")
        print(product_code)
        # retorno http
        return HttpResponse(200, {"Hello": "World"})
