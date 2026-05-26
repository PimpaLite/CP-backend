from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the core application
app = FastAPI(
    title="Interactive Comic Platform API",
    description="Backend engine for processing interactive digital comics, haptic triggers, and Web Audio syncing.",
    version="1.0.0"
)

# Configure CORS so the Next.js frontend can communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Next.js default local port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Interactive Comic Platform API is running.",
        "services": {
            "database": "pending setup",
            "image_cdn": "pending setup"
        }
    }