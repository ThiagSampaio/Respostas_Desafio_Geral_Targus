import logging
import uvicorn
import time
from fastapi import FastAPI,Request
from uicheckapp.Services import EchoService
import random
import string





logging.config.fileConfig('logging.conf', disable_existing_loggers=False)


logger = logging.getLogger(__name__) 

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response



@app.get("/")
async def index():
    logger.info("logging from the root logger")
    teste = EchoService(msg="hi")
    teste.echo()
    return {"status": "alive"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)