"""
Seed database with sample data for testing and development.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.db.session import SessionLocal
from src.db.models.user import User, UserRole
from src.db.models.parking_spot import ParkingSpot, ParkingSpotStatus, VehicleType
from src.core.security import get_password_hash
from src.utils.logger import logger


def seed_users(db):
    """Seed users."""
    logger.info("Seeding users...")
    
    # Create admin user
    admin = User(
        email="admin@parkidam.com",
        username="admin",
        hashed_password=get_password_hash("admin123"),
        full_name="Admin User",
        phone_number="+1234567890",
        role=UserRole.ADMIN,
        is_active=True,
        is_verified=True
    )
    
    # Create parking manager
    manager = User(
        email="manager@parkidam.com",
        username="manager",
        hashed_password=get_password_hash("manager123"),
        full_name="Parking Manager",
        phone_number="+1234567891",
        role=UserRole.PARKING_MANAGER,
        is_active=True,
        is_verified=True
    )
    
    # Create regular user
    user = User(
        email="user@parkidam.com",
        username="user",
        hashed_password=get_password_hash("user123"),
        full_name="Regular User",
        phone_number="+1234567892",
        role=UserRole.USER,
        is_active=True,
        is_verified=True
    )
    
    db.add_all([admin, manager, user])
    db.commit()
    
    logger.info(f"Created admin: {admin.username}")
    logger.info(f"Created manager: {manager.username}")
    logger.info(f"Created user: {user.username}")
    
    return admin, manager, user


def seed_parking_spots(db, owner):
    """Seed parking spots."""
    logger.info("Seeding parking spots...")
    
    sections = ['A', 'B', 'C', 'D']
    floors = [1, 2, 3]
    spot_counter = 1
    
    spots = []
    
    for floor in floors:
        for section in sections:
            for i in range(1, 11):  # 10 spots per section
                spot = ParkingSpot(
                    spot_number=f"{section}{floor}{i:02d}",
                    floor=floor,
                    section=section,
                    location_description=f"Floor {floor}, Section {section}",
                    status=ParkingSpotStatus.AVAILABLE if i <= 7 else ParkingSpotStatus.OCCUPIED,
                    vehicle_type=VehicleType.CAR if i <= 8 else VehicleType.MOTORCYCLE,
                    hourly_rate=5.0 + (floor * 0.5),
                    daily_rate=30.0 + (floor * 5.0),
                    is_covered=floor > 1,
                    is_disabled_accessible=i == 1,
                    is_ev_charging=i <= 2,
                    has_camera=True,
                    owner_id=owner.id
                )
                
                # Add some occupied spots with vehicle info
                if spot.status == ParkingSpotStatus.OCCUPIED:
                    spot.current_vehicle_number = f"ABC{spot_counter:04d}"
                    spot_counter += 1
                
                spots.append(spot)
    
    db.add_all(spots)
    db.commit()
    
    logger.info(f"Created {len(spots)} parking spots")
    
    # Print statistics
    available = len([s for s in spots if s.status == ParkingSpotStatus.AVAILABLE])
    occupied = len([s for s in spots if s.status == ParkingSpotStatus.OCCUPIED])
    logger.info(f"Available: {available}, Occupied: {occupied}")


def main():
    """Main seeding function."""
    logger.info("Starting database seeding...")
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_users = db.query(User).count()
        if existing_users > 0:
            logger.warning("Database already contains data. Skipping seed.")
            return
        
        # Seed data
        admin, manager, user = seed_users(db)
        seed_parking_spots(db, manager)
        
        logger.info("Database seeding completed successfully!")
        logger.info("\nDefault credentials:")
        logger.info("  Admin: admin / admin123")
        logger.info("  Manager: manager / manager123")
        logger.info("  User: user / user123")
        
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()