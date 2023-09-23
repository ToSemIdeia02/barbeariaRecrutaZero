import threading
import time
import datetime

class Barber(threading.Thread):
    def __init__(self, name, semaphore, customers):
        threading.Thread.__init__(self)
        self.name = name
        self.semaphore = semaphore
        self.customers = customers
        self.current_customer = None

    def run(self):
        while True:
            self.semaphore.acquire()  # Wait for a customer
            self.cut_hair()

    def cut_hair(self):
        self.current_customer = self.customers.get()  # Get the next customer in line
        start_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{start_time}] {self.name} starts cutting hair of {self.current_customer.rank} {self.current_customer.name}")
        time.sleep(self.current_customer.hair_cut_time)  # simulate the time it takes to cut hair
        end_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{end_time}] {self.name} finished cutting hair of {self.current_customer.rank} {self.current_customer.name}")
        self.current_customer = None
