class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict[str, int | float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def check_products(self, cart: dict[str, int]) -> bool:
        for product in cart:
            if product not in self.products:
                print(f"{self.products} does not contain {product}!")
                return False
        return True
