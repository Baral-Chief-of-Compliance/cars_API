from pydantic import BaseModel
from enum import Enum


#виды топлива, которые есть в системе
class FUEL_TYPE(str, Enum):
    PETROL = "бензин"
    DIESEL = "дизель"
    ELECTRICITY = "электричество"
    HYBRID = "гибрид"


#виды КПП
class TRANSMISSION(str, Enum):
    MECHANICAL = "механическая"
    AUTOMATIC = "автоматическая"
    VARIATOR = "вариатор"
    ROBOT = "робот"


#модель данных машины
class CarModel(BaseModel):
    c_id: int or None = None #id машины
    c_brand: str #Марка
    c_model: str #Модель
    c_year_release: int #Год выпуска
    c_fuel_type: FUEL_TYPE #Тип топлива (бензин, дизель, электричество, гибрид)
    c_transmission: TRANSMISSION #Тип КПП (механическая, автоматическая, вариатор, робот)
    c_mileage: int #Пробег
    c_price: int #Цена