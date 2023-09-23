import queue
import random
import threading

from Barber import Barber
from Customer import Customer

# Create a queue for customers
customers = queue.Queue(maxsize=20)


def barber_shop():
    # Create a semaphore
    semaphore = threading.Semaphore(0)

    # Create barbers
    barber1 = Barber("Recruta Zero", semaphore, customers)
    barber2 = Barber("Dentinho", semaphore, customers)
    barber3 = Barber("Otto", semaphore, customers)

    # Start barbers
    barber1.start()
    barber2.start()
    barber3.start()

    # Add customers to queue and release the semaphore for each one
    for i in range(10):
        # Determine rank randomly for demonstration
        rank = random.choice(["Officer", "Sargent", "Private"])
        customer = Customer(f"Customer{i}", rank)
        customers.put(customer)
        semaphore.release()


barber_shop()
