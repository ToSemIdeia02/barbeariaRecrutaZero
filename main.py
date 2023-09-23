import queue
from Barber import Barber
from Customer import Customer
from random import randint


def sleeping_barber(barber):
    # While the barber is not sleeping
    while True:
        # Get the next customer from the priority queue
        customer = barber.get_next_customer()

        # If there is no customer, the barber goes to sleep
        if customer is None:
            print("The barber is sleeping.")
            barber.wait()

        # Otherwise, the barber cuts the customer's hair
        else:
            barber.cut_hair(customer)


def sargent_timer():
    return randint(1, 5)


def customer():
    # Create a new customer
    customer = Customer()

    # Get the barber
    barber = Barber()

    # Add the customer to the priority queue
    barber.priority_queue.put(customer)

    # Wake up the barber
    barber.signal()

    # Wait for the barber to signal that the customer's hair has been cut
    barber.wait()


if __name__ == "__main__":
    # Create a barber
    barber = Barber()

    # Create three customers, one of each rank
    officer = Customer("Officer")
    sargent = Customer("Sergeant")
    recruit = Customer("Recruit")

    # Add the customers to the priority queue
    barber.priority_queue.put(officer)
    barber.priority_queue.put(sargent)
    barber.priority_queue.put(recruit)

    # Start the barber thread
    import threading

    barber_thread = threading.Thread(target=sleeping_barber, args=(barber,))
    barber_thread.start()

    # Start the customer threads
    customer_threads = []
    for customer in [officer, sargent, recruit]:
        customer_thread = threading.Thread(target=lambda: customer())
        customer_threads.append(customer_thread)
        customer_thread.start()

    # Wait for all of the customer threads to finish
    for customer_thread in customer_threads:
        customer_thread.join()

    # Stop the barber thread
    barber.signal()
    barber_thread.join()
