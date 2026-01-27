from fastapi import FastAPI

blog:list[dict]=[
    {
        "id":1,
        "title":"Blog 1",
        "content":"Content of blog 1"
    },
    {
        "id":2,
        "title":"Blog 2",
        "content":"Content of blog 2"
    }
]

app = FastAPI()

@app.get("/blog")
def get_blogs():
    return {"data": blog}




