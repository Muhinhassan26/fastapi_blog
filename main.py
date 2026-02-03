from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


blogs:list[dict]=[
    {
        "id":1,
        "author":"John Doe",
        "title":"Blog 1",
        "content":"Content of blog 1"
    },
    {
        "id":2,
        "author":"Don Doe",
        "title":"Blog 2",
        "content":"Content of blog 2"
    }
]

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/",include_in_schema=False,name="home")
@app.get("/posts",include_in_schema=False,name="posts")
def home(request:Request,):
    return templates.TemplateResponse(request,"home.html",{"posts":blogs,"title":"Home"})




