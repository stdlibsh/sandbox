from fastapi import FastAPI

from sandbox import __version__
from sandbox.routes import router


def get_application() -> FastAPI:
    app = FastAPI(title="Sandbox", version=__version__)
    app.include_router(router)

    return app
