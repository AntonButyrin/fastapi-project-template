from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.core.config import admin_settings, host_settings

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

security = HTTPBasic()


@app.get("/openapi.json")
async def get_open_api_endpoint(credentials: HTTPBasicCredentials = Depends(security)):
    if (
        credentials.username != admin_settings.username
        and credentials.password != admin_settings.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return get_openapi(
        title="fastapi_project_template title",
        version=1,
        routes=app.routes,
        description="fastapi_project_template descriptions",
        contact={
            "name": "Anton Butyrin",
            "email": "butyrinhome@gmail.com",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )


@app.get("/docs")
async def get_documentation(credentials: HTTPBasicCredentials = Depends(security)):
    if (
        credentials.username != admin_settings.username
        and credentials.password != admin_settings.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="docs",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=[host_settings.allowed_host],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
