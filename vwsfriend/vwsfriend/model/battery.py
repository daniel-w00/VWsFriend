from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from vwsfriend.model.base import Base


class Battery(Base):
    __tablename__ = 'battery'
    __table_args__ = (
        UniqueConstraint('vehicle_vin', 'carCapturedTimestamp'),
    )
    id = Column(Integer, primary_key=True)
    vehicle_vin = Column(String, ForeignKey('vehicles.vin'))
    carCapturedTimestamp = Column(DateTime)
    vehicle = relationship("Vehicle")
    currentSOC_pct = Column(Integer)
    cruisingRangeElectric_km = Column(Integer)

    def __init__(self, vehicle, carCapturedTimestamp, currentSOC_pct, cruisingRangeElectric_km):
        self.vehicle = vehicle
        self.carCapturedTimestamp = carCapturedTimestamp
        self.currentSOC_pct = currentSOC_pct
        self.cruisingRangeElectric_km = cruisingRangeElectric_km