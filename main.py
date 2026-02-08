from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: PromptRequest):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": req.prompt,
            "stream": False
        }
    )
    return {"response": response.json().get("response", "")}

def calculator(expr: str):
    try:
        return str(eval(expr))
    except:
        return "error"

def agent_logic(prompt: str):
    if "calculate" in prompt.lower():
        expr = prompt.lower().replace("calculate", "")
        return calculator(expr)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json().get("response", "")

@app.post("/agent")
def agent(req: PromptRequest):
    return {"response": agent_logic(req.prompt)}
