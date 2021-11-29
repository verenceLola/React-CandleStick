from starlette.routing import Route
from views import Documents

routes = [Route(("/documents"), Documents)]
