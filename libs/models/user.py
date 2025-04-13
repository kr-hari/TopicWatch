from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
import uuid

## Below are a unified Python and Postgres Models
# -------------------------------
# UserAuth Model (user_auth table)
# -------------------------------
class UserAuth(SQLModel, table=True):
    __tablename__ = "user_auth"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(index=True, max_length=50)
    email: str = Field(index=True, max_length=255)
    password_hash: str

    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    demographics: Optional["UserDemographics"] = Relationship(back_populates="user", sa_relationship_kwargs={"uselist": False})
    tokens: List["AuthToken"] = Relationship(back_populates="user")
    subscriptions: List["UserSubscription"] = Relationship(back_populates="user")


# -------------------------------------
# UserDemographics Model (One-to-One)
# -------------------------------------
class UserDemographics(SQLModel, table=True):
    __tablename__ = "user_demographics"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user_auth.id",
        unique=True  # <-- this enforces one-to-one in the ORM
    )
    
    age: Optional[int] = Field(default=None, ge=0)
    gender: Optional[str] = Field(default=None, max_length=100)
    location: Optional[str] = Field(default=None, max_length=255)
    occupation: Optional[str] = Field(default=None, max_length=100)
    company: Optional[str] = Field(default=None, max_length=100)
    country: Optional[str] = Field(default=None, max_length=100)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    user: UserAuth = Relationship(back_populates="demographics")


# ---------------------------
# AuthToken Model (Many-to-One)
# ---------------------------
class AuthToken(SQLModel, table=True):
    __tablename__ = "auth_tokens"

    token_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user_auth.id")
    token: str
    expires_at: datetime

    # Relationships
    user: UserAuth = Relationship(back_populates="tokens")


# --------------------------------------
# UserSubscription Model (Many-to-Many)
# --------------------------------------
class UserSubscription(SQLModel, table=True):
    __tablename__ = "user_subscriptions"

    user_id: uuid.UUID = Field(foreign_key="user_auth.id", primary_key=True)
    subreddit: str = Field(primary_key=True, max_length=255)
    followed_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    user: UserAuth = Relationship(back_populates="subscriptions")



# --------------------------------
# Below are Pydantic Models
# --------------------------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str   

class DemographicsCreate(BaseModel):
    age: Optional[int] = None
    location: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    occupation: Optional[str] = None
    gender: Optional[str] = None