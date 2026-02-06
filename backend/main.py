from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chat import ChatBot
import os

app = FastAPI(title="Healthcare Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = ChatBot()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def read_root():
    return {"message": "Healthcare Chatbot API is running. Use POST /chat to interact."}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    response_text = bot.get_response(request.message)
    return ChatResponse(response=response_text)

if __name__ == "__main__":
    import uvicorn
    if not os.path.exists("model_data.pkl"):
        print("Model not found. Running training script first...")
        import train
        train.train_model()
        bot.load_model() 

    uvicorn.run(app, host="0.0.0.0", port=8000)
