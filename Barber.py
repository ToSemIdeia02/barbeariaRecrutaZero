import queue

class Barber:
    def __init__(self):
        self.customer = None
        self.priority_queue = queue.PriorityQueue()

    def cut_hair(self, customer):
        self.customer = customer
        print(f"The barber is cutting hair for {customer.rank}.")
        # Simulate the time it takes to cut hair
        import time
        time.sleep(1)
        print(f"The barber has finished cutting hair for {customer.rank}.")

    def get_next_customer(self):
        # Check if there is a customer in the priority queue
        if not self.priority_queue.empty():
            return self.priority_queue.get()
        else:
            return None
