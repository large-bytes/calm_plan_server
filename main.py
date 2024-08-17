from fastapi import FastAPI, HTTPException, Depends


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    tasks = [
        {"id": "1", "name": "Learn JavaScript", "priority": "five"},
        {"id": "2", "name": "Deploy app", "priority": "five"},
        {"id": "3", "name": "Update project dependencies", "priority": "three"},
        {"id": "4", "name": "Write docs", "priority": "two"},
        {"id": "5", "name": "Refactor app.js", "priority": "one"},
    ]
    return {"all_tasks": tasks}
