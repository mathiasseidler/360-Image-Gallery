from typing import List, Optional
from pydantic import BaseModel
from fastapi import UploadFile, File


# -- Image Schemas --
class ImageBase(BaseModel):
    file_name: str
    # file_data: UploadFile


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True


# -- Project Schemas --
class ProjectBase(BaseModel):
    title: str
    description: str


class ProjectCreate(ProjectBase):
    creator_user_id: str
    images: List[ImageCreate] = []


class Project(ProjectBase):
    id: int
    images: List[Image] = []

    class Config:
        orm_mode = True
