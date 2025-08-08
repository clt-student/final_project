from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import promotions as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Promotion(
        code=request.code,
        discount_percent=request.discount_percent,
        expiration_date=request.expiration_date
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e.__dict__["orig"]))
    return new_item


def read_all(db: Session):
    try:
        return db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e.__dict__["orig"]))


def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.Promotion).filter(model.Promotion.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        return item
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e.__dict__["orig"]))


def update(db: Session, item_id: int, request):
    try:
        item = db.query(model.Promotion).filter(model.Promotion.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.update(request.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return item.first()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e.__dict__["orig"]))


def delete(db: Session, item_id: int):
    try:
        item = db.query(model.Promotion).filter(model.Promotion.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e.__dict__["orig"]))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
