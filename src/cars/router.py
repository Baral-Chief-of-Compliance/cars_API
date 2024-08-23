from fastapi import APIRouter, HTTPException
from src.cars.schemas import CarModel
from src.cars.database import add_car_in_db, delete_car_from_db, get_inf_about_car_from_db, get_cars_from_db, upate_car_in_db


router = APIRouter(
    prefix = "/cars",
    tags=["cars"]
)

#добавление автомобиля
@router.post("/api/cars/")
async def add_car(car: CarModel):
    add_car_in_db(car=car)
    return car 

#получить список автомобилей
@router.get("/api/cars/")
async def get_cars(
    brand: str or None = None,
    model: str or None = None,
    year: int or None = None,
    fuel_type: str or None = None,
    transmission: str or None = None,
    mileage_min: int or None = None,
    mileage_max: int or None = None,
    price_min: int or None = None,
    price_max: int or None = None
    ):
    query_text: str = "SELECT * FROM Cars"
    condition_counter: int = 0
    condition_text: str = " WHERE "
    condition_values: list = []

    #проверка на наличие Query параметра brand
    if brand is not None:
        condition_counter +=1
        condition_text += "c_brand=? "  
        condition_values.append(brand)
    
    #проверка на наличие Query параметра model
    if model is not None:
        condition_counter +=1
        if condition_counter == 1:
            condition_text += "c_model=? "  
        else:
            condition_text += "AND c_model=? "
        condition_values.append(model)
    
    #проверка на наличие Query параметра year 
    if year is not None:
        condition_counter += 1
        if condition_counter == 1:
            condition_text += "c_year_release=? "
        else:
            condition_text += "AND c_year_release=? "
        condition_values.append(year)

    #проверка на наличие Query параметра fuel_type
    if fuel_type is not None:
        condition_counter += 1
        if condition_counter == 1:
            condition_text += "c_fuel_type=? "
        else:
            condition_text += "AND c_fuel_type=? "
        condition_values.append(fuel_type)

    #проверка на наличие Query параметра transmission
    if transmission is not None:
        condition_counter += 1
        if condition_counter == 1:
            condition_text += "c_transmission=? "
        else:
            condition_text += "AND c_transmission=? "
        condition_values.append(transmission)
    
    #проверка на наличие Query параметра mileage_min
    if mileage_min is not None:
        condition_counter += 1
        if condition_counter == 1:
            condition_text += "c_mileage >=? "
        else:
            condition_text += "AND c_mileage >=? "
        condition_values.append(mileage_min)

    #проверка на наличие Query параметра mileage_max
    if mileage_max is not None:
        condition_counter +=1 
        if condition_counter == 1:
            condition_text += "c_mileage <=? "
        else:
            condition_text += "AND c_mileage <=? "
        condition_values.append(mileage_max)

    #проверка на наличие Query параметра price_min
    if price_min is not None:
        condition_counter += 1
        if condition_counter == 1:
            condition_text += "c_price >=? "
        else:
            condition_text += "AND c_price >= ? "
        condition_values.append(price_min)

    #проверка на наличие Query параметра price_max
    if price_max is not None:
        condition_counter += 1
        if condition_counter == 1:
            condition_text += "c_price <=? "
        else:
            condition_text += "AND c_price <=? "
        condition_values.append(price_max)

    if condition_counter > 0:
        query_text += condition_text

    print(query_text)
    cars = get_cars_from_db(query_text=query_text, values=condition_values)
    return {
        "cars": cars
    }

#удаление автомобиля из базы данных
@router.delete("/api/cars/{c_id}")
async def delete_car(c_id: int):
    err = delete_car_from_db(c_id=c_id)

    if type(err) is TypeError:
        raise HTTPException(status_code=404,  detail="Car with c_id={c_id} not found, therefore cannot be deleted")
    return {
        f"car with c_id={c_id} is deleted"
    }

#получение информации об автомобиле по его id
@router.get("/api/cars/{c_id}")
async def get_car(c_id: int):
    car = get_inf_about_car_from_db(c_id=c_id)
    if type(car) is TypeError:
        raise HTTPException(status_code=404,  detail="Car with c_id={c_id} not found")
    else:
        return car
    

#обновление ифнормации об автмобиле по его id
@router.put("/api/cars/{c_id}")
async def update_car(car: CarModel, c_id: int):
    if c_id != car.c_id:
        raise HTTPException(status_code=400,  detail="The c_id in the query and in the model do not match")
    else:
        err = upate_car_in_db(car=car)

        if type(err) is TypeError:
            raise HTTPException(status_code=404,  detail="Car with c_id={c_id} not found")
        else:
            return f"car with c_id = {c_id} is updated"
    