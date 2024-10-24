
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return ''.join(file.readlines())
        except FileNotFoundError:
            return 'Файл не найден.'

    def add(self, *products):
        existing_products = self.get_products().splitlines() if self.get_products() != 'Файл не найден.' else []
        existing_names = {p.split(', ')[0] for p in existing_products}

        for product in products:
            if product.name not in existing_names:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')

shop = Shop()
potato = Product('Potato', 50.0, 'Vegetables')
carrot = Product('Carrot', 30.0, 'Vegetables')

shop.add(potato, carrot)
print(shop.get_products())