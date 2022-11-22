from typing import List,Optional 
from fastapi import FastAPI,Query
from fastapi.encoders import jsonable_encoder
from model.dbHandler import match_exact,match_like

app = FastAPI()


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
