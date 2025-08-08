from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import ratings as controller
from ..schemas import ratings as schema
from ..dependencies.database import get_db

router = APIRouter(tags=["Ratings"], prefix="/ratings")


@router.post("/", response_model=schema.Rating)
def create(request: schema.RatingCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)


@router.get("/", response_model=list[schema.Rating])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Rating)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)


@router.put("/{item_id}", response_model=schema.Rating)
def update(item_id: int, request: schema.RatingCreate,  # add RatingUpdate when needed
           db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)


@router.delete("/{item_id}", status_code=204)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
