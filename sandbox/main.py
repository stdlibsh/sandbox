from fastapi import FastAPI

from sandbox.routes import router


def get_application() -> FastAPI:
    app = FastAPI(title="Sandbox")
    app.include_router(router)

    return app
