from pydantic import BaseModel,EmailStr

class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"

class TokenSchema(BaseModel):
    access_token:str
    token_type:str
