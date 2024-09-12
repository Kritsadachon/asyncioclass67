import time
import asyncio
from asyncio import Queue


class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time      


class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    customers_served = 0
    total_time = 0.0
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}")
        for product in customer.products:
            print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} for {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
        checkout_time = round(time.perf_counter() - customer_start_time, ndigits=2)
        total_time += checkout_time
        print(f"The Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} "
              f"in {checkout_time} secs")
        customers_served += 1
        queue.task_done()

    print(f"====The Cashier_{cashier_number+1} take {customers_served} customers total {total_time} secs.")


def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', 0.4),
                    Product('sausage', 0.4),
                    Product('diapers', 0.2)]
    return Customer(customer_id, all_products)


async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    for customer_id in range(customers):
        customer = generate_customer(customer_id)
        print(f"Waiting to put Customer_{customer_id} in line...")
        await queue.put(customer)
        print(f"Customer_{customer_id} put in line...")
        customer_count += 1
    return customer_count


async def main():
    customer_queue = Queue(3)
    customers_start_time = time.perf_counter()

    num_customers = 10

    customer_producer = asyncio.create_task(customer_generation(customer_queue, num_customers))
    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(5)]

    await asyncio.gather(customer_producer)
    await customer_queue.join()
    await asyncio.gather(*cashiers)

    print(f"The supermarket process finished {num_customers} customers "
          f"in {round(time.perf_counter() - customers_start_time, ndigits=2)} secs")


if __name__ == "__main__":
    asyncio.run(main())
