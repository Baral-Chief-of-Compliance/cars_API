from src.database import Conn
from src.cars.schemas import CarModel


#добавление машины в базу данных
def add_car_in_db(car: CarModel) -> None:
    con = Conn()
    con.make_query(
        query_text='''INSERT INTO Cars 
        (c_brand, c_model, c_year_release, 
        c_fuel_type, c_transmission, c_mileage, c_price) 
        values (?, ?, ?, ?, ?, ?, ?)''',
        values= (
            car.c_brand, car.c_model, car.c_year_release,
            car.c_fuel_type, car.c_transmission, car.c_mileage, car.c_price
        ),
        commitFlag=True,
        resultFlag=False
    )

#удаление автомобиля по его id 
def delete_car_from_db(c_id: int) -> None | TypeError:
    try:
        con = Conn()
        con.make_query(
            query_text='''DELETE FROM Cars WHERE c_id = ?''',
            values=(c_id,),
            commitFlag=True,
            resultFlag=False
        )
        del con
    except Exception as e:
        return e


#получение списка машин по характеристикам, если таковые есть
def get_cars_from_db(query_text: str, values: list) -> list:
    con = Conn()
    res_cars = con.make_query(
        query_text=query_text,
        values=values,
    )
    del con

    result = []

    for c in res_cars:
        car = CarModel(
            c_id=c[0],
            c_brand=c[1],
            c_model=c[2],
            c_year_release=c[3],
            c_fuel_type=c[4],
            c_transmission=c[5],
            c_mileage=c[6],
            c_price=c[7]
        )
        result.append(
            car
        )

    return result





#получение информации об автомобиле по его id
def get_inf_about_car_from_db(c_id: int) -> CarModel | TypeError:
    try:
        con = Conn()
        res_car = con.make_query(
            query_text='''SELECT * FROM Cars WHERE c_id = ?''',
            values=(c_id, ),
            resultManyFlag=False
        )
        del con

        car = CarModel(
            c_id=res_car[0],
            c_brand=res_car[1],
            c_model=res_car[2],
            c_year_release=res_car[3],
            c_fuel_type=res_car[4],
            c_transmission=res_car[5],
            c_mileage=res_car[6],
            c_price=res_car[7]
        )

        return car
    except Exception as e:
        return e


#обновление информации об автомобиле
def upate_car_in_db(car: CarModel) -> None | TypeError:
    try:
        con = Conn()
        con.make_query(
            query_text='''UPDATE Cars SET c_brand=?, c_model=?, c_year_release=?, c_fuel_type=?, c_transmission=?, c_mileage=?, c_price=? WHERE c_id=?''',
            values=[car.c_brand, car.c_model, car.c_year_release, car.c_fuel_type, car.c_transmission, car.c_mileage, car.c_price, car.c_id],
            commitFlag=True,
            resultFlag=False
            )
        del con
    except Exception as e:
        return e