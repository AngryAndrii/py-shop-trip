import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:

    with open("config.json", "r") as config:
        data = json.load(config)

    fuel_price = data["FUEL_PRICE"]
    customers = []
    for customer_data in data["customers"]:
        customer = Customer(customer_data["name"],
                            customer_data["product_cart"],
                            customer_data["location"],
                            customer_data["money"],
                            Car(customer_data["car"]["brand"],
                                customer_data["car"]["fuel_consumption"]))

        customers.append(customer)

    shops = []
    for shop_data in data["shops"]:
        shop = Shop(shop_data["name"],
                    shop_data["location"],
                    shop_data["products"])

        shops.append(shop)

    # print(customers[0].calc_trip_cost(shops[0], fuel_price))
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            # min_shop = {"name": 0}
            if shop.check_products(customer.product_cart):
                cost_for_shop = customer.calc_trip_cost(shop, fuel_price)
                print(f"{customer.name}'s trip to the"
                      f" {shop.name} costs {cost_for_shop}")


shop_trip()