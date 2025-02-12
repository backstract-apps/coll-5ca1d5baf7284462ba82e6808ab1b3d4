from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/car_details/')
async def get_car_details(db: Session = Depends(get_db)):
    try:
        return await service.get_car_details(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/car_details/id')
async def get_car_details_id(licence_number: str, db: Session = Depends(get_db)):
    try:
        return await service.get_car_details_id(db, licence_number)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/car_details/')
async def post_car_details(raw_data: schemas.PostCarDetails, db: Session = Depends(get_db)):
    try:
        return await service.post_car_details(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/car_details/id/')
async def put_car_details_id(raw_data: schemas.PutCarDetailsId, db: Session = Depends(get_db)):
    try:
        return await service.put_car_details_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/car_details/id')
async def delete_car_details_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_car_details_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_slots/')
async def get_parking_slots(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_slots(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_slots/id')
async def get_parking_slots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_slots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_slots/')
async def post_parking_slots(raw_data: schemas.PostParkingSlots, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_slots(db, raw_data, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_slots/id/')
async def put_parking_slots_id(raw_data: schemas.PutParkingSlotsId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_slots_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_slots/id')
async def delete_parking_slots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_slots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking-owner')
async def post_parking_owner(owner_name: str, parking_name: str, email_id: str, password: str, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_owner(db, owner_name, parking_name, email_id, password)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking-owner/id')
async def get_parking_owner_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_owner_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking-owner/login')
async def post_parking_owner_login(email_id: str, password: str, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_owner_login(db, email_id, password)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/remove/parking-owner')
async def delete_remove_parking_owner(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_remove_parking_owner(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking-owner/upload-image')
async def post_parking_owner_upload_image(image: UploadFile, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_owner_upload_image(db, image, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking-slot/check-out')
async def post_parking_slot_check_out(raw_data: schemas.PostParkingSlotCheckOut, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_slot_check_out(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

