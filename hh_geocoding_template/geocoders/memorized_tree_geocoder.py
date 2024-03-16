from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.slov_dict={}#создаем словарь для сохранения адрессов

    def tr_tree(self, node: TreeNode, address: str):#использую функцию, которая обходит все дерево и сохраняет адресс каждого узла в словарь который мы создали ранее
        if node is None:#проверяем пуста ли наша нода, и добавлем ее значение в словарь
            return
        self.slov.dict[node.id]=address
        for areas in node.areas:
            self.tr_tree(areas, address+', '+areas.name)
#делаю штуку, которая возвращает данные из словаря с адресами, но перед этим использую функцию get которая
#возвращает значение словаря по коючу
    def get_address(self, area_id: str) -> str:
        if area_id in self.slov.dict:
            return self.slov.dict[area_id]
        else:
            return "пу-пу-пууу, бите"

    def _apply_geocoding(self, area_id: str) -> str:
        return self.get_address(area_id)








