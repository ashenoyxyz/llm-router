from fastapi import FastAPI
import uvicorn
import os
import socket

# Globals
LLM_TYPE = os.environ.get("LLM_TYPE", "UNKNOWN")
LLM_HOST = socket.gethostname()
REQ_COUNT = 0

app = FastAPI()

@app.get("/")
def read_root():
    global REQ_COUNT
    REQ_COUNT += 1
    return {
        'host': LLM_HOST,
        'type': LLM_TYPE,
        'request_count': REQ_COUNT
    }

if __name__ == '__main__':
    print(f'Starting {LLM_TYPE} LLM service....')
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
