from pydantic import main
from sqlalchemy.orm import Session
from . import models, schemas

# -- Projects CRUD --
def get_projects(db: Session, skip: int = 0, limit=100):
    return db.query(models.Project).offset(skip).limit(limit).all()


def create_project(db: Session, project: schemas.ProjectCreate, creator_user_id: str):
    db_project = models.Project(project, creator_user_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project_by_id(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


# -- Images CRUD --
def create_image(db: Session, image: schemas.ImageCreate, project_id: int):
    db_image = models.Image(**image.dict(), project_id=project_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def get_images_by_project_id(db: Session, project_id: int, limit = 100):
    return db.query(models.Image).filter(models.Image.project_id == project_id).limit(limit).all()


