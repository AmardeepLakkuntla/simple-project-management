from fastapi import FastAPI

app=FastAPI()

@app.get('/all_good')
def check_all_good():
    return{'status':'ok'}