from geocoders.geocoder import Geocoder
from api import API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        areas_inf=API.get_areas(area_id)#используя методо get получаем информацию о всех эриасах
        address=areas_inf.mame#создаем переменую которая принимает значение areas_inf
        while areas_inf := API.get_areas(areas_inf.parent.id):#Начинается цикл while, который будет выполняться до тех пор, пока вызов метода get_areas
            # с аргументом areas_inf.parent.id не вернет ложное значение. В каждой итерации цикла переменная areas_inf обновляется

            address=areas_inf.mame+''+address
        raise NotImplementedError()