from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routers import all

app = FastAPI()
origins = [
    "http://localhost:8000",
    "http://localhost:5173",
    "https://calmplan.largebytes.co.uk"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#tasks router
app.include_router(tasks_router.router)

#users router
app.include_router(users_router.router)

#auth router
app.include_router(auth_router.router)
