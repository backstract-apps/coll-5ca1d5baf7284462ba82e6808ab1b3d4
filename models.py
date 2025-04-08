from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class UploadedAttachment(Base):
    __tablename__ = 'uploaded_attachment'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    attachment_url = Column(String, primary_key=False)
    bs_user_id = Column(Integer, primary_key=False)


class BsUser(Base):
    __tablename__ = 'bs_user'
    full_name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    email_verified = Column(Integer, primary_key=False)
    form_credits = Column(Integer, primary_key=False)
    update_at = Column(Time, primary_key=False)
    created_at = Column(Time, primary_key=False)
    secret_key = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    id = Column(Integer, primary_key=True)


class ParkingOwner(Base):
    __tablename__ = 'parking_owner'
    id = Column(Integer, primary_key=True)
    owner_name = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    parking_name = Column(String, primary_key=False)
    email_id = Column(String, primary_key=False)
    owner_id = Column(String, primary_key=False)


class BsFormSubmission(Base):
    __tablename__ = 'bs_form_submission'
    id = Column(Integer, primary_key=True)
    title = Column(String, primary_key=False)
    message = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    mobile_number = Column(Integer, primary_key=False)
    additional_info = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    attachment_url = Column(String, primary_key=False)
    contact_to = Column(Integer, primary_key=False)
    source_type = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    full_name = Column(String, primary_key=False)


class ParkingSlots(Base):
    __tablename__ = 'parking_slots'
    id = Column(Integer, primary_key=True)
    direction = Column(String, primary_key=False)
    car_id = Column(Integer, primary_key=False)
    booking_at = Column(Time, primary_key=False)
    parking_id = Column(Integer, primary_key=False)
    price_hourly = Column(Integer, primary_key=False)
    parking_for = Column(String, primary_key=False)
    check_in_time = Column(Time, primary_key=False)
    check_out_time = Column(Time, primary_key=False)


class CarDetails(Base):
    __tablename__ = 'car_details'
    license_plate_number = Column(String, primary_key=False)
    car_model = Column(String, primary_key=False)
    owner_name = Column(String, primary_key=False)
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)


