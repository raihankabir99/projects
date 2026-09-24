from fastapi import FastAPI
from pydantic import BaseModel
from nemoguardrails import LLMRails, RailsConfig

app = FastAPI()


config = RailsConfig.from_path("./config")
rails = LLMRails(config)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = await rails.generate_async(messages=[{
        "role": "user",
        "content": request.message
    }])
    
    if isinstance(response, dict):
        res_content = response.get("content", response)
    else:
        res_content = getattr(response, "content", str(response))
        
    return {"response": res_content}
