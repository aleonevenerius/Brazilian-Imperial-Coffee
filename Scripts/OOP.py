class Product:
	def __init__(self, id_product, name, category, price, qtd):
        self.id_product = id_product
        self.name = name
        self.category = category
        self.price = price
        self.qtd = qtd
class Order:
    def __init__(self, id_order_client, order_status, name_client, order_client):
        self.id_order_client =  id_order_client
        self.name_client = name_client
        self.order_client = order_client
        self.name_client = name_client
        self.order_client = order_client
class User:
    def __init__(self, id_user, name, password):
        self.id_user = id_user
        self.name = name
        self.password = password