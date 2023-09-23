class Tenente:
    def __init__(self):
        self.report = {
            "occupation": [0, 0, 0, 0],
            "queue_lengths": [0, 0, 0],
            "service_times": [0, 0, 0],
            "wait_times": [0, 0, 0],
            "customer_counts": [0, 0, 0, 0],
        }

    def update_report(self, category, service_time):
        self.report["occupation"][category] += 1
        self.report["queue_lengths"][category] += 1
        self.report["service_times"][category] += service_time
        self.report["customer_counts"][category] += 1

    def print_report(self):
        print("Relatório do Tenente:")
        print("Ocupação das cadeiras:")
        for category, occupation in enumerate(self.report["occupation"]):
            print(f"Categoria {category}: {occupation}%")

        print("Comprimento médio das filas:")
        for category, queue_length in enumerate(self.report["queue_lengths"]):
            print(f"Categoria {category}: {queue_length:.2f} clientes")

        print("Tempo médio de atendimento por categoria:")
        for category, service_time in enumerate(self.report["service_times"]):
            print(f"Categoria {category}: {service_time:.2f} segundos")

        print("Tempo médio de espera por categoria:")
        for category, customer_count in enumerate(self.report["customer_counts"]):
            if customer_count > 0:
                wait_time = self.report["service_times"][category] / customer_count
                print(f"Categoria {category}: {wait_time:.2f} segundos")
            else:
                print(f"Categoria {category}: 0 segundos")

        print("Número de atendimentos por categoria:")
        for category, customer_count in enumerate(self.report["customer_counts"]):
            print(f"Categoria {category}: {customer_count} clientes")

