from api import API, TreeNode
from geocoders.geocoder import Geocoder


class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        result = self.bfs(self.__data, str(area_id))
        return ", ".join([node.name for node in result][::-1])

    def bfs(self, root_children, area_id: str) -> list[TreeNode] | None:#с помощью метода bfs мы выполняем поиск ширину в дереве, начинаем с корневых узлов
        result = []
#далее происходит цикл который обходит узлы в дереве
#если найдется узел с заданным area_id,  то он добавляется в результуат, а если у узла есть дочерние области, рекурсивно вызывается метод для каждой области.
        for node in root_children:
            if node.id == area_id:
                result.append(node)
                return result
            if len(node.areas) != 0:
                res_return = self.bfs(node.areas, area_id)
                if res_return:
                    result.extend(res_return)
                    result.append(node)
                    return result
                if parent_node is None:
                    break
                address_parts.insert(0, parent_node.name)
                current_node = parent_node

            full_address = ", ".join(address_parts)#здесь мы формируем полный адресс из частей адреса
            return full_address #возвращаем полный адресс из метода
