from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import spells
from .routers import equipment
from .routers import equipment_categories
from .routers import ability_scores
from .routers import monsters
from .routers import skills
from .routers import characters

app = FastAPI(
    title="DnD API",
    description=("An API for DnD data written with FastAPI and MongoDB"),
    version="0.0.1",
)

app.include_router(spells.router, prefix="/api/v1")
app.include_router(equipment.router, prefix="/api/v1")
app.include_router(equipment_categories.router, prefix="/api/v1")
app.include_router(ability_scores.router, prefix="/api/v1")
app.include_router(monsters.router, prefix="/api/v1")
app.include_router(skills.router, prefix="/api/v1")
app.include_router(characters.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)