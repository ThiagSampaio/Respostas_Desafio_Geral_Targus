'''
Explicação do Arquivo:

Temos uma função de fábrica que retorna um aplicativo FastAPI com middleware cors configurado. 
Importamos este middleware do pacote starlette. 

Ultima atualização:05/10/2021 - Thiago Sampaio
'''


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import config, tasks  
from app.api.routes import router as api_router


def get_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)  

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))


    app.include_router(api_router, prefix="/api")

    return app


app = get_application()



