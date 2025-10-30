from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ParkingSpot(Base):
    __tablename__ = 'parking_spots'

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    is_available = Column(Boolean, default=True)
    owner_id = Column(Integer)  # Assuming a foreign key to a User model
    price_per_hour = Column(Integer)  # Price in cents or dollars, depending on your currency strategy

    def __repr__(self):
        return f"<ParkingSpot(id={self.id}, location='{self.location}', is_available={self.is_available}, owner_id={self.owner_id}, price_per_hour={self.price_per_hour})>"