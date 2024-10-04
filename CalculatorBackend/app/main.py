from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes


# Initialize FastAPI instance
app = FastAPI()

# passing requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Hut8 Calc"}

# Include routes
app.include_router(routes.router)