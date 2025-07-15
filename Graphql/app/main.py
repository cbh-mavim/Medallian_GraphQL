from fastapi import FastAPI, Request, Depends, HTTPException, Header
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from strawberry.fastapi import GraphQLRouter
from jose import jwt, JWTError

from app.gql.schema import schema
from app.settings import config
from app.settings.ms_auth import get_auth_url, get_token_from_code

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/auth/login")
def login():
    auth_url = get_auth_url()
    return RedirectResponse(auth_url)

@app.get("/auth/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="No auth code provided")
    token_response = get_token_from_code(code)
    return RedirectResponse(url=f"/graphql?token={token_response['access_token']}") 

def verify_token(authorization: str):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise ValueError("Invalid auth scheme")
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        return decoded_token
    except (JWTError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

#The context getter
async def get_context(request: Request):
    token = request.headers.get("Authorization", "")
    user = verify_token(token) if token else None
    return {"request": request, "user": user}

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context
)

app.include_router(graphql_app, prefix="/graphql")
