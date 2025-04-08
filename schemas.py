from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class UploadedAttachment(BaseModel):
    id: int
    created_at: datetime.time
    attachment_url: str
    bs_user_id: int


class ReadUploadedAttachment(BaseModel):
    id: int
    created_at: datetime.time
    attachment_url: str
    bs_user_id: int
    class Config:
        from_attributes = True


class BsUser(BaseModel):
    full_name: str
    email: str
    email_verified: int
    form_credits: int
    update_at: datetime.time
    created_at: datetime.time
    secret_key: str
    password: str
    id: int


class ReadBsUser(BaseModel):
    full_name: str
    email: str
    email_verified: int
    form_credits: int
    update_at: datetime.time
    created_at: datetime.time
    secret_key: str
    password: str
    id: int
    class Config:
        from_attributes = True


class ParkingOwner(BaseModel):
    id: int
    owner_name: str
    created_at: datetime.time
    parking_name: str
    email_id: str
    owner_id: str


class ReadParkingOwner(BaseModel):
    id: int
    owner_name: str
    created_at: datetime.time
    parking_name: str
    email_id: str
    owner_id: str
    class Config:
        from_attributes = True


class BsFormSubmission(BaseModel):
    id: int
    title: str
    message: str
    email: str
    mobile_number: int
    additional_info: str
    created_at: datetime.time
    attachment_url: str
    contact_to: int
    source_type: str
    status: str
    updated_at: datetime.time
    full_name: str


class ReadBsFormSubmission(BaseModel):
    id: int
    title: str
    message: str
    email: str
    mobile_number: int
    additional_info: str
    created_at: datetime.time
    attachment_url: str
    contact_to: int
    source_type: str
    status: str
    updated_at: datetime.time
    full_name: str
    class Config:
        from_attributes = True


class ParkingSlots(BaseModel):
    id: int
    direction: str
    car_id: int
    booking_at: datetime.time
    parking_id: int
    price_hourly: int
    parking_for: str
    check_in_time: datetime.time
    check_out_time: datetime.time


class ReadParkingSlots(BaseModel):
    id: int
    direction: str
    car_id: int
    booking_at: datetime.time
    parking_id: int
    price_hourly: int
    parking_for: str
    check_in_time: datetime.time
    check_out_time: datetime.time
    class Config:
        from_attributes = True


class CarDetails(BaseModel):
    license_plate_number: str
    car_model: str
    owner_name: str
    id: int
    created_at: datetime.time


class ReadCarDetails(BaseModel):
    license_plate_number: str
    car_model: str
    owner_name: str
    id: int
    created_at: datetime.time
    class Config:
        from_attributes = True




class PostCarDetails(BaseModel):
    license_plate_number: str
    car_model: str
    owner_name: str

    class Config:
        from_attributes = True



class PutCarDetailsId(BaseModel):
    license_plate_number: str
    car_model: str
    owner_name: str
    id: str

    class Config:
        from_attributes = True



class PostParkingSlots(BaseModel):
    direction: str
    parking_for: str
    slot_price: int

    class Config:
        from_attributes = True



class PutParkingSlotsId(BaseModel):
    id: int
    direction: str
    car_id: int

    class Config:
        from_attributes = True



class PostParkingSlotCheckOut(BaseModel):
    id: int

    class Config:
        from_attributes = True

