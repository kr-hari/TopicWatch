from fastapi import HTTPException
from sqlmodel import Session, select
from datetime import datetime, timedelta
import uuid
from dotenv import load_dotenv
load_dotenv()

from libs.db.postgres import engine, create_db_and_tables
from libs.models.user import UserAuth, UserDemographics, AuthToken, UserSubscription, UserCreate, DemographicsCreate
from apps.user_service.password_utils import hash_password

from fastapi import FastAPI

app = FastAPI()

@app.post("/user/create")
def create_user(user: UserCreate):
    # Hash the raw password
    password_hash = hash_password(user.password)

    # Create a UserAuth instance (DB model)
    db_user = UserAuth(
        username=user.username,
        email=user.email,
        password_hash=password_hash,
    )

    # Save to DB
    with Session(engine) as session:
        # Check if the user already exists
        existing_user_email = session.exec(select(UserAuth).where(UserAuth.email == user.email)).first()
        existing_user_name = session.exec(select(UserAuth).where(UserAuth.username == user.username)).first()
        if existing_user_email:
            raise HTTPException(status_code=400, detail="User already exists.")
        elif existing_user_name:
            raise HTTPException(status_code=400, detail="Username already exists.")
        
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return {
            "message": "User created",
            "user_id": str(db_user.id),
            "username": db_user.username
        }

@app.get("/user/id")
def get_user_id(user_email: str):
    # Fetch the user by email
    with Session(engine) as session:
        user = session.exec(select(UserAuth).where(UserAuth.email == user_email)).first()

        if not user:
            return {"error": "User not found"}

        return {
            "user_id": str(user.id)
        }

@app.post("/user/demographics")
def insert_demographics(user_email: str, demographics: DemographicsCreate):

    # Fetch the user by email
    user_id = get_user_id(user_email=user_email)
    if "error" in user_id:
        return user_id
    user_id = user_id["user_id"]

    # Create a DB UserDemographics instance
    demographics_db = UserDemographics(
        age=demographics.age,
        gender=demographics.gender,
        location=demographics.location,
        occupation=demographics.occupation,
        company=demographics.company,
        country=demographics.country)
    demographics_db.user_id = user_id

    # Save to DB
    with Session(engine) as session:
        existing = session.exec(select(UserDemographics).where(UserDemographics.user_id == user_id)).first()
        if existing:
            raise HTTPException(status_code=400, detail="Demographics already exist for this user.")
        session.add(demographics_db)
        session.commit()
        session.refresh(demographics_db)

        return {
            "message": "Demographics inserted",
            "user_id": user_id,
            "demographics": demographics_db
        }

@app.get("/user/demographics")
def get_demographics(user_email: str):
    # Fetch the user by email
    user_id = get_user_id(user_email=user_email)
    if "error" in user_id:
        return user_id
    user_id = user_id["user_id"]

    # Fetch demographics
    with Session(engine) as session:
        demographics = session.exec(select(UserDemographics).where(UserDemographics.user_id == user_id)).first()

        if not demographics:
            return {"error": "Demographics not found"}

        return {
            "user_id": user_id,
            "demographics": demographics
        }
    
# def insert_data():
#     with Session(engine) as session:
#         # 1. Create a new user
#         user = UserAuth(
#             username="alice123",
#             email="alice@example.com",
#             password_hash="$2b$12$somethinghashed",  # bcrypt hash
#         )
#         session.add(user)
#         session.commit()
#         session.refresh(user)  # Refresh to get generated UUID

#         print(f"Created user: {user.username} (ID: {user.id})")

#         # 2. Add demographics
#         demographics = UserDemographics(
#             user_id=user.id,
#             age=27,
#             gender="Female",
#             location="New York",
#             occupation="Engineer",
#             company="TechCorp",
#             country="USA"
#         )
#         session.add(demographics)

#         # 3. Add an auth token
#         token = AuthToken(
#             user_id=user.id,
#             token="sample_token_123",
#             expires_at=datetime.utcnow() + timedelta(days=7)
#         )
#         session.add(token)

#         # 4. Add a subreddit subscription
#         sub = UserSubscription(
#             user_id=user.id,
#             subreddit="python"
#         )
#         session.add(sub)

#         # Final commit
#         session.commit()


# def read_data():
#     with Session(engine) as session:
#         # Read all users
#         users = session.exec(select(UserAuth)).all()

#         for user in users:
#             print(f"User: {user.username} | Email: {user.email}")
            
#             if user.demographics:
#                 print(f"  Age: {user.demographics.age} | Country: {user.demographics.country}")

#             if user.tokens:
#                 for token in user.tokens:
#                     print(f"  Token: {token.token} (Expires: {token.expires_at})")

#             if user.subscriptions:
#                 print(f"  Subscribed to: {[s.subreddit for s in user.subscriptions]}")


# def main():
#     print("🔧 Creating database & tables if not exist...")
#     create_db_and_tables()

#     print("📝 Inserting user data...")
#     insert_data()

#     print("🔍 Reading data from DB...")
#     read_data()


# if __name__ == "__main__":
#     main()