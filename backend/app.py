from starlette.applications import Starlette
from config import DEBUG
from database import Database

from routes import routes


async def startup():
    # await database connection
    await Database.connect()


async def shutdown():
    """
    disconnect the database when the app exists
    """
    await Database.disconnect()

app = Starlette(
    debug=DEBUG, routes=routes, on_startup=[startup], on_shutdown=[shutdown]
)
