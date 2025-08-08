from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(tags=["Promotions"], prefix="/promotions")


@router.post("/", response_model=schema.Promotion)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)


@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Promotion)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)


@router.put("/{item_id}", response_model=schema.Promotion)
def update(item_id: int, request: schema.PromotionCreate,  # create a PromotionUpdate for partials
           db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)


@router.delete("/{item_id}", status_code=204)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
