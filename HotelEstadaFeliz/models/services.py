class services:
    services_array = []

    def create_service(self, service_name, price):
        id = len(services.services_array)+1
        new_service = {
            "service_id":   id, 
            "service_name": service_name, 
            "price":        price 
            }
        services.services_array.append(new_service)