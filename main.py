from fastapi import FastAPI,Cookie,Request,Form
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
template=Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def login(request:Request):
    return template.TemplateResponse("login.html",{"request":request})
@app.post("/")
def get_data(request:Request,email:str=Form(...,description="abc@gmail.com"),password:str=Form(...)):
    print(email,password)
