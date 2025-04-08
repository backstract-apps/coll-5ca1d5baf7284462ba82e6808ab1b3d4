from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_car_details(db: Session):

    car_details_all = db.query(models.CarDetails).all()
    car_details_all = [new_data.to_dict() for new_data in car_details_all] if car_details_all else car_details_all

    res = {
        'car_details_all': car_details_all,
    }
    return res

async def get_car_details_id(db: Session, licence_number: str):

    car_details_one = db.query(models.CarDetails).filter(models.CarDetails.license_plate_number == licence_number).first() 
    car_details_one = car_details_one.to_dict() if car_details_one else car_details_one

    res = {
        'car_details_one': car_details_one,
    }
    return res

async def post_car_details(db: Session, raw_data: schemas.PostCarDetails):
    license_plate_number:str = raw_data.license_plate_number
    car_model:str = raw_data.car_model
    owner_name:str = raw_data.owner_name


    import time
    import random
    from datetime import datetime

    try:
        timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
        random_number = random.randint(1, 1000)  # Generate a 4-digit random number
        unique_digit = f"{timestamp}{random_number}"  # Concatenate both
        user_id =  int(unique_digit)
        
        current_timestamp:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'license_plate_number': license_plate_number, 'car_model': car_model, 'owner_name': owner_name, 'id': user_id, 'created_at': current_timestamp}
    new_car_details = models.CarDetails(**record_to_be_added)
    db.add(new_car_details)
    db.commit()
    db.refresh(new_car_details)
    car_details_inserted_record = new_car_details.to_dict()

    res = {
        'car_details_inserted_record': car_details_inserted_record,
    }
    return res

async def put_car_details_id(db: Session, raw_data: schemas.PutCarDetailsId):
    license_plate_number:str = raw_data.license_plate_number
    car_model:str = raw_data.car_model
    owner_name:str = raw_data.owner_name
    id:str = raw_data.id


    import time
    import random
    from datetime import datetime

    try:
        timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
        random_number = random.randint(1000, 9999)  # Generate a 4-digit random number
        unique_digit = f"{timestamp}{random_number}"  # Concatenate both
        user_id =  int(unique_digit)
        
        current_timestamp:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    car_details_edited_record = db.query(models.CarDetails).filter(models.CarDetails.id == id).first()
    for key, value in {'license_plate_number': license_plate_number, 'car_model': car_model, 'owner_name': owner_name, 'id': id, 'created_at': current_timestamp}.items():
          setattr(car_details_edited_record, key, value)
    db.commit()
    db.refresh(car_details_edited_record)
    car_details_edited_record = car_details_edited_record.to_dict() 

    res = {
        'car_details_edited_record': car_details_edited_record,
    }
    return res

async def delete_car_details_id(db: Session, id: int):

    car_details_deleted = None
    record_to_delete = db.query(models.CarDetails).filter(models.CarDetails.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        car_details_deleted = record_to_delete.to_dict() 

    res = {
        'car_details_deleted': car_details_deleted,
    }
    return res

async def get_parking_slots(db: Session):

    parking_slots_all = db.query(models.ParkingSlots).all()
    parking_slots_all = [new_data.to_dict() for new_data in parking_slots_all] if parking_slots_all else parking_slots_all

    res = {
        'parking_slots_all': parking_slots_all,
    }
    return res

async def get_parking_slots_id(db: Session, id: int):

    parking_slots_one = db.query(models.ParkingSlots).filter(models.ParkingSlots.id == id).first() 
    parking_slots_one = parking_slots_one.to_dict() if parking_slots_one else parking_slots_one

    res = {
        'parking_slots_one': parking_slots_one,
    }
    return res

async def post_parking_slots(db: Session, raw_data: schemas.PostParkingSlots , request: Request):
    direction:str = raw_data.direction
    parking_for:str = raw_data.parking_for
    slot_price:int = raw_data.slot_price

    header_authorization:str = request.headers.get('header-authorization')



    try:
        decoded_token_info = jwt.decode(
            header_authorization,
            'wj5rq18kyhqre597tym6rhf02zjj2fdd8p2tacawt71nr',
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        decoded_token_info = 'Token has expired.'
    except jwt.InvalidTokenError:
        decoded_token_info = 'Invalid token.'


    

    try:
        owner_id:str = decoded_token_info["data"]["user_id"]
    except Exception as e:
        raise HTTPException(500, str(e))



    owner_info = db.query(models.ParkingOwner).filter(models.ParkingOwner.owner_id == owner_id).first() 
    owner_info = owner_info.to_dict() if owner_info else owner_info


    import time
    import random
    from datetime import datetime

    try:
        timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
        random_number = random.randint(1, 1000)  # Generate a 4-digit random number
        unique_digit = f"{timestamp}{random_number}"  # Concatenate both
        unique_id =  int(unique_digit)
        
        current_timestamp:datetime = datetime.now()
        car_id:int = 0
        
        parking_owner_id:int= owner_info["id"]
    except Exception as e:
        raise HTTPException(500, str(e))



    slots_list = db.query(models.ParkingSlots).all()
    slots_list = [new_data.to_dict() for new_data in slots_list] if slots_list else slots_list


    record_to_be_added = {'id': unique_id, 'direction': direction, 'car_id': car_id, 'booking_at': current_timestamp, 'parking_id': parking_owner_id, 'price_hourly': slot_price, 'parking_for': parking_for}
    new_parking_slots = models.ParkingSlots(**record_to_be_added)
    db.add(new_parking_slots)
    db.commit()
    db.refresh(new_parking_slots)
    parking_slot = new_parking_slots.to_dict()

    res = {
        'parking_slot': parking_slot,
    }
    return res

async def put_parking_slots_id(db: Session, raw_data: schemas.PutParkingSlotsId):
    id:int = raw_data.id
    direction:str = raw_data.direction
    car_id:int = raw_data.car_id


    import time
    import random
    from datetime import datetime

    try:
        timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
        random_number = random.randint(1, 1000)  # Generate a 4-digit random number
        unique_digit = f"{timestamp}{random_number}"  # Concatenate both
        unique_id =  int(unique_digit)
        
        current_timestamp:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    parking_slots_edited_record = db.query(models.ParkingSlots).filter(models.ParkingSlots.id == id).first()
    for key, value in {'id': id, 'direction': direction, 'car_id': car_id, 'check_in_time': current_timestamp}.items():
          setattr(parking_slots_edited_record, key, value)
    db.commit()
    db.refresh(parking_slots_edited_record)
    parking_slots_edited_record = parking_slots_edited_record.to_dict() 

    res = {
        'parking_slots_edited_record': parking_slots_edited_record,
    }
    return res

async def delete_parking_slots_id(db: Session, id: int):

    parking_slots_deleted = None
    record_to_delete = db.query(models.ParkingSlots).filter(models.ParkingSlots.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_slots_deleted = record_to_delete.to_dict() 

    res = {
        'parking_slots_deleted': parking_slots_deleted,
    }
    return res

async def post_parking_owner(db: Session, owner_name: str, parking_name: str, email_id: str, password: str):

    import time
    import random
    from datetime import datetime

    try:
        timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
        random_number = random.randint(1, 6000)  # Generate a 4-digit random number
        unique_digit = f"{timestamp}{random_number}"  # Concatenate both
        user_id =  int(unique_digit)
        
        current_timestamp:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))




    import requests

    headers = {'X-Stack-Project-Id': 'c225ddc3-02cb-425b-a517-a72579e1b9f1', 'X-Stack-Publishable-Client-Key': 'pck_qs23k4y3gczn08kbt04wyd1a7rjmt88n9kv4mf7bd0ntr', 'x-Stack-Secret-Server-Key': 'ssk_cek3jmwwe69qb522nxth128qqt5d3n5csj7sxxcx8r020', 'X-stack-access-type': 'server'}
    
    payload = {'email': email_id, 'password': password, 'verification_callback_url': 'https://cc1fbde45ead-in-south-01.backstract.io/keen-mcclintock-706dbaccdeed11ef9e510242ac18000231/verification_callback_url'}
    apiResponse = requests.post(
        'https://api.stack-auth.com/api/v1/auth/password/sign-up',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    parking = apiResponse.json() if 'dict' in ['dict', 'list'] else apiResponse.text

    

    try:
        owner_auth_id:str = parking["user_id"]
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': user_id, 'owner_name': owner_name, 'created_at': current_timestamp, 'parking_name': parking_name, 'email_id': email_id, 'owner_id': owner_auth_id}
    new_parking_owner = models.ParkingOwner(**record_to_be_added)
    db.add(new_parking_owner)
    db.commit()
    db.refresh(new_parking_owner)
    parking_owner_details = new_parking_owner.to_dict()

    res = {
        'owner_details': parking_owner_details,
    }
    return res

async def get_parking_owner_id(db: Session, id: int):

    parking_owner_id = db.query(models.ParkingOwner).filter(models.ParkingOwner.id == id).first() 
    parking_owner_id = parking_owner_id.to_dict() if parking_owner_id else parking_owner_id

    res = {
        'parking_owner': id,
    }
    return res

async def post_parking_owner_login(db: Session, email_id: str, password: str):


    import requests

    headers = {'X-Stack-Project-Id': 'c225ddc3-02cb-425b-a517-a72579e1b9f1', 'X-Stack-Publishable-Client-Key': 'pck_qs23k4y3gczn08kbt04wyd1a7rjmt88n9kv4mf7bd0ntr', 'x-Stack-Secret-Server-Key': 'ssk_cek3jmwwe69qb522nxth128qqt5d3n5csj7sxxcx8r020', 'X-stack-access-type': 'server'}
    
    payload = {'email': email_id, 'password': password}
    apiResponse = requests.post(
        'https://api.stack-auth.com/api/v1/auth/password/sign-in',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    auth_post_apis = apiResponse.json() if 'dict' in ['dict', 'list'] else apiResponse.text


    user_data = {}  # Creating new dict


    

    try:
        user_data = {
            "user_id":auth_post_apis["user_id"],
            "email_id":email_id
        }
    except Exception as e:
        raise HTTPException(500, str(e))




    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=6400000)).timestamp()),
        'data': user_data
    }

    login_token = jwt.encode(bs_jwt_payload, 'wj5rq18kyhqre597tym6rhf02zjj2fdd8p2tacawt71nr', algorithm='HS256')

    res = {
        'login_token': login_token,
    }
    return res

async def delete_remove_parking_owner(db: Session, id: int):

    parking_owner = None
    record_to_delete = db.query(models.ParkingOwner).filter(models.ParkingOwner.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_owner = record_to_delete.to_dict() 

    res = {
        'parking_owner': parking_owner['id'],
    }
    return res

async def post_parking_owner_upload_image(db: Session, image: UploadFile , request: Request):
    header_authorization:str = request.headers.get('header-authorization')



    try:
        decoded_token_info = jwt.decode(
            header_authorization,
            'wj5rq18kyhqre597tym6rhf02zjj2fdd8p2tacawt71nr',
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        decoded_token_info = 'Token has expired.'
    except jwt.InvalidTokenError:
        decoded_token_info = 'Invalid token.'


    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CP6X5H4BNH",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1"
    )

    # Read file content
    file_content = await image.read()

    name = image.filename
    file_path = file_path  + '/' + name

    import mimetypes
    image.file.seek(0)
    s3_client.upload_fileobj(
        image.file,
        bucket_name,
        name,
        ExtraArgs={"ContentType": mimetypes.guess_type(name)[0]}

    )

    file_type = Path(image.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    owner_image_url = file_url
    res = {
        'owner_image_url': owner_image_url,
    }
    return res

async def post_parking_slot_check_out(db: Session, raw_data: schemas.PostParkingSlotCheckOut):
    id:int = raw_data.id


    import time
    import random
    from datetime import datetime

    try:
        timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
        random_number = random.randint(1, 1000)  # Generate a 4-digit random number
        unique_digit = f"{timestamp}{random_number}"  # Concatenate both
        unique_id =  int(unique_digit)
        
        current_timestamp:datetime = datetime.now()
        
        car_id = 0
    except Exception as e:
        raise HTTPException(500, str(e))



    data_uploaded = db.query(models.ParkingSlots).filter(models.ParkingSlots.id == id).first()
    for key, value in {'check_out_time': current_timestamp, 'car_id': car_id}.items():
          setattr(data_uploaded, key, value)
    db.commit()
    db.refresh(data_uploaded)
    data_uploaded = data_uploaded.to_dict() 

    res = {
        'updated_details': data_uploaded,
    }
    return res

