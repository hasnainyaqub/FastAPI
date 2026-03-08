from fastapi import FastAPI
from fastapi.responses import JSONResponse
from config import UserQuestion
from chain import chatbot
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

chain = chatbot()
@app.post('/chatbot')
def chatbot(question: UserQuestion):
    answer = chain.invoke(question)
    return JSONResponse(status_code=200, content={'message': answer})

