class payment_items:
    payment_items_array = []

    def create_payment_item(self, payment_id, service_id, quantity, unit_price_register, consumption_date):
        id = len(payment_items.payment_items_array)+1
        new = {
            "payment_item_id":     id, 
            "payment_id":          payment_id, 
            "service_id":          service_id, 
            "quantity":            quantity, 
            "unit_price_register": unit_price_register,
            "consumption_date":    consumption_date
            }
        payment_items.payment_items_array.append(new)
