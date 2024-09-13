import time
import asyncio
from asyncio import Queue
from random import randrange

class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int):
    total_time = []
    final_queue = []
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"the Cashier {cashier_number} :"
                f"will checkout Customer_{customer.customer_id}")
        
        for product in customer.products:

            if cashier_number == 2:
                product.checkout_time = 0.1
                print("time", product.checkout_time)
                print(f"the Cashier {cashier_number} :"
                    f"will checkout Customer_{customer.customer_id} "
                    f"Product_{product.product_name} "
                    f"in {product.checkout_time}")
                totol_time1 = round(product.checkout_time, ndigits=2)
                total_time.append(totol_time1)
                
                await asyncio.sleep(product.checkout_time)

            else:
                print(f"the Cashier {cashier_number} :"
                    f"will checkout Customer_{customer.customer_id} "
                    f"Product_{product.product_name} "
                    f"in {product.checkout_time + (0.1*cashier_number)} ")
                totol_time1 = round(product.checkout_time + (0.1*cashier_number), ndigits=2)
                total_time.append(totol_time1)
                
                await asyncio.sleep(product.checkout_time + (0.1*cashier_number) )

        print(f"the Cashier_{cashier_number}"
                f"finished checkout Customer_{customer.customer_id}"
                f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")
        
        totol_time2 = round(time.perf_counter() - customer_start_time, ndigits=2)
        final_queue.append(totol_time2)
        print(f"totel time of the Cashier_{cashier_number}")
        print(totol_time1)
        
        queue.task_done()

    return sum(total_time), len(final_queue)


def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)


async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count+customers)]

        for customer in customers:
            print("Waiting to put customer in line....")
            await queue.put(customer)
            
            print("Customer pput in line....")


        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count

async def main():
    totol_time = []
    final_queue = []
    customer_queue = Queue(3)
    cashier_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, 10))
    cashiers = [checkout_customer(customer_queue, i) for i in range(5)]
    result = await asyncio.gather(customer_producer, *cashiers)

    # for i in result:
    print(result)
    totol_time.append(result[0])
    final_queue.append(result)
    
    #print(totol_time)
    print("Time and queue",final_queue)
    print(f"The supermarket process finished"
           f"{customer_producer.result()} customers"
           f"in {round(time.perf_counter() - cashier_time, ndigits=2)} secs")
    
    
    
if __name__ == "__main__":
    asyncio.run(main())