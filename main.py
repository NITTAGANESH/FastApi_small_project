from fastapi import Depends,FastAPI,HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from database import sessionLocal,engine
from sqlalchemy.orm import Session
import model
from schemas import ProductSchema,UserSchema,TokenSchema
from auth import hash_password,verify_password,create_access_token,SECRET_KEY,ALGORITHM
from jose import jwt,JWTError

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

model.Base.metadata.create_all(bind=engine)
oauth2_scheme= OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user:UserSchema,db:Session=Depends(get_db)):
    if len(user.password.encode("utf-8"))>72:
        raise HTTPException(status_code=400, detail="Password too long (max 72 Char)")

    if user.role=="admin":
        existing_admin=db.query(model.User).filter(model.User.role=="admin").first()
        if existing_admin:
            raise HTTPException(status_code=400, detail="Admin user already exists")
    
    existing = db.query(model.User).filter(model.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed=hash_password(user.password)
    new_user=model.User(username=user.username,email=user.email,password=hashed,role=user.role)
    db.add(new_user)
    db.commit()
    return "User Registered Successfully"

@app.post("/login",response_model=TokenSchema)
def login(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user=db.query(model.User).filter(model.User.email==form_data.username).first()

    if not user or not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token=create_access_token({"sub":user.email,"role":user.role})

    return {"access_token":token, "token_type":"bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid token")

def admin_only(user=Depends(get_current_user)):
    if user.get("role")!="admin":
        raise HTTPException(status_code=403,detail="Admin access required")
    return user


@app.get("/products")
def secure_products(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(model.Product).all()


@app.get("/products/{id}")
def get_product_by_id(id:int,user=Depends(admin_only), db:Session=Depends(get_db)):
    product=db.query(model.Product).filter(model.Product.id==id).first()
    return product

@app.post("/products")
def add_product(product:ProductSchema,user=Depends(admin_only),db:Session=Depends(get_db)):
    db.add(model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int, product:ProductSchema, user=Depends(admin_only), db:Session=Depends(get_db)):
    db_product = db.query(model.Product).filter(model.Product.id==id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
    else:
        return {"message":"Product not found"}
    return db_product

@app.delete("/products/{id}")
def delete_product(id:int,user=Depends(admin_only),db:Session=Depends(get_db)):
    db_product = db.query(model.Product).filter(model.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message":"Product deleted successfully"}
    else:
        return {"message":"Product not found"}
    
