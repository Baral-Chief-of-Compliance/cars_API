from fastapi import FastAPI
from  src.swagger_description import title, summary, description, version, tags_metadata
import src.cars.router as cars


app = FastAPI(
    title=title,
    summary=summary,
    description=description,
    version=version,
    openapi_tags=tags_metadata
)

app.include_router(cars.router)


