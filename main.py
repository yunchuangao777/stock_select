from fastapi import FastAPI
from fastapi.responses import JSONResponse
import intelligent_stock_select

app = FastAPI()

@app.get("/")
def read_root():
    return "Intelligent stock list"

@app.get('/get_pelosi_stock_list')
def index():

    # format: {'msg':'pelosi stock list', 'data':'1. MSFT, 2. GOOG ...'}
    data_search = intelligent_stock_select.get_pelosi_stock_list()

    return JSONResponse(content=data_search)

@app.get('/get_ai_stock_list')
def index():

    # format: {'msg':'pelosi stock list', 'data':'1. MSFT, 2. GOOG ...'}
    data_search = intelligent_stock_select.get_ai_concept_stock_list()

    return JSONResponse(content=data_search)

@app.get('/get_twosigma_stock_list')
def index():

    # format: {'msg':'pelosi stock list', 'data':'1. MSFT, 2. GOOG ...'}
    data_search = intelligent_stock_select.get_twosigma_stock_list()

    return JSONResponse(content=data_search)