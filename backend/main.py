from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"message": "Cloud Support AI Chatbot backend is running."}


@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()

    if "hello" in user_message:
        response = "Hey! I'm your Khameleon AI Assistant.  I can help with tech, cloud, and more.  What do you need?"
    elif "aws" in user_message:
        response = "AWS is a cloud platform offering services like EC2, S3, and more."
    elif "ec2" in user_message:
        response = "EC2 lets you run virtual servers in the cloud."
    elif "linux" in user_message:
        response = "Linux is widely used in cloud environments for servers."
    else:
        response = "Ask me about AWS, EC2, Linux, or cloud troubleshooting."

    return {"response": response}
