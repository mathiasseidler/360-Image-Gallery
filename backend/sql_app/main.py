from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/users/{user_id}/projects", response_model=schemas.ProjectCreate)
def create_project(user_id: str, project: schemas.ProjectCreate, db: Session = Depends(get_db)):

    return crud.create_project(db=db, project=project, creator_user_id=user_id)


@app.get("/api/v1/projects/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_projects(db, skip=skip, limit=limit)
    return users


@app.get("/api/v1/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_project