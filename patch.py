# Определение параметров , используя синтаксис форматированных строк Python 
from enum import Enum 
from fastapi import FastAPI 
 
app = FastAPI() 
 
 
@app.get("/items/{item_id}") 
async def read_item(item_id): 
    return {"item_id": item_id} 
 
# Параметры пути с типами 
 
app = FastAPI() 
 
 
@app.get("/items/{item_id}") 
async def read_item(item_id: int): 
    return {"item_id": item_id} 
 
# Проверка данных 
{ 
    "detail": [ 
        { 
            "loc": [ 
                "path", 
                "item_id" 
            ], 
            "msg": "value is not a valid integer", 
            "type": "type_error.integer" 
        } 
    ] 
} 
 
# путь для /users/me объявлен раньше, чем путь для /users/{user_id} 
 
app = FastAPI() 
 
 
@app.get("/users/me") 
async def read_user_me(): 
    return {"user_id": "the current user"} 
 
 
@app.get("/users/{user_id}") 
async def read_user(user_id: str): 
    return {"user_id": user_id} 
 
# Создание класса Enum 
 
 
class ModelName(str, Enum): 
    alexnet = "alexnet" 
    resnet = "resnet" 
    lenet = "lenet" 
 
 
app = FastAPI() 
 
 
@app.get("/models/{model_name}") 
async def get_model(model_name: ModelName): 
    if model_name is ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW!"} 
 
    if model_name.value == "lenet": 
        return {"model_name": model_name, "message": "LeCNN all the images"} 
 
    return {"model_name": model_name, "message": "Have some residuals"} 
 
# Определение параметра пути 
 
 
class ModelName(str, Enum): 
    alexnet = "alexnet" 
    resnet = "resnet" 
    lenet = "lenet" 
 
 
app = FastAPI() 
 
 
@app.get("/models/{model_name}") 
async def get_model(model_name: ModelName): 
    if model_name is ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW!"} 
 
    if model_name.value == "lenet": 
        return {"model_name": model_name, "message": "LeCNN all the images"} 
 
    return {"model_name": model_name, "message": "Have some residuals"} 
# Значение параметра пути будет элементом перечисления 
 
 
class ModelName(str, Enum): 
    alexnet = "alexnet" 
    resnet = "resnet" 
    lenet = "lenet" 
 
 
app = FastAPI() 
 
 
@app.get("/models/{model_name}") 
async def get_model(model_name: ModelName): 
    if model_name is ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW!"} 
 
    if model_name.value == "lenet": 
        return {"model_name": model_name, "message": "LeCNN all the images"} 
 
    return {"model_name": model_name, "message": "Have some residuals"} 
 
# Получение значения перечисления 
 
 
class ModelName(str, Enum): 
    alexnet = "alexnet" 
    resnet = "resnet" 
    lenet = "lenet" 
 
 
app = FastAPI() 
 
 
@app.get("/models/{model_name}") 
async def get_model(model_name: ModelName): 
    if model_name is ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW!"} 
 
    if model_name.value == "lenet": 
        return {"model_name": model_name, "message": "LeCNN all the images"} 
 
    return {"model_name": model_name, "message": "Have some residuals"} 
 
# Возврат элементов перечисления 
 
 
class ModelName(str, Enum): 
    alexnet = "alexnet" 
    resnet = "resnet" 
    lenet = "lenet" 
 
 
app = FastAPI() 
 
 
@app.get("/models/{model_name}") 
async def get_model(model_name: ModelName): 
    if model_name is ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW!"} 
 
    if model_name.value == "lenet": 
        return {"model_name": model_name, "message": "LeCNN all the images"} 
 
    return {"model_name": model_name, "message": "Have some residuals"}