import uvicorn
from fastapi import FastAPI
from onnix_food import ColaPredictor



app = FastAPI(title="Ferrato")

@app.get("/")
async def home():
    return "<h2>This is a sample Project</h2>"


path = '/home/ashvinee/Documents/Ferrato/'
predictor = ColaPredictor(path)

@app.get("/predict")
async def get_prediction(text: str):
    text = text.split(', ')
    result =  predictor.predict(text)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#uvicorn app:app --ip 0.0.0.0 --port 8000 --reload+'checkpoints/model.pt'
#vicorn app:app --ip 0.0.0.0 --port 8000 --reload