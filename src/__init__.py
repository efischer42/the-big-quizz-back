import uvicorn


def start_web_server() -> None:
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)

if __name__ == "__main__":
    start_web_server()