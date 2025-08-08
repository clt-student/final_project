from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import promotion_menu_items as controller
from ..schemas import promotion_menu_items as schema
from ..dependencies.database import get_db

router = APIRouter(tags=["Promotion Menu Items"], prefix="/promotionmenuitems")


@router.post("/", response_model=schema.PromotionMenuItem)
def create(request: schema.PromotionMenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)


@router.get("/", response_model=list[schema.PromotionMenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.PromotionMenuItem)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)


@router.put("/{item_id}", response_model=schema.PromotionMenuItem)
def update(item_id: int, request: schema.PromotionMenuItemCreate,  # full replace
           db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)


@router.delete("/{item_id}", status_code=204)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
