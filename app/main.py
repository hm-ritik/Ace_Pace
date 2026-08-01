from fastapi import FastAPI 


app=FastAPI(title="Ace Pace")


@app.get("/home")

def home():
    return{
        "Message": "Checking Server"
    }