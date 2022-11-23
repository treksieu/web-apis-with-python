from typing import List,Optional 
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from model.dbHandler import match_exact,match_like
from fastapi.openapi.utils import get_openapi


app = FastAPI()




def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="peti schema",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage":"/dict?=<word>"}
    return jsonable_encoder(response)


@app.get("/dict")

def dictionary(word : str):

    if not word:
        response = {"status":"error","data":"pls choose a word"}
        return jsonable_encoder(response)

    # Try to find an exact match

    definitions = match_exact(word)
    if definitions:
        response = {"status":"success","word":word, "data":definitions}
        return jsonable_encoder(response)

    # Try to find an approximate match

    definitions = match_like(word)
    if definitions:
        response = {"status":"partial","word":word,"data":definitions}    
        return jsonable_encoder(response)

    else:
        response = {"status":"error","word": word,"data":"word not found"}
        return jsonable_encoder(response)

@app.post("/dict")

def add(word : str):
    return {"word": word}

