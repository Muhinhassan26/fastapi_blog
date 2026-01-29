from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates



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

templates = Jinja2Templates(directory="templates")

@app.get("/blog")
def get_blogs(request:Request,):
    return templates.TemplateResponse(request,"home.html",{"blogs":blogs,"title":"Home"})




