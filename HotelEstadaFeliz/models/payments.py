class payments:
    payments_array = []
    
    def create_payment(self, book_id, emission_date, services_value, daily_value, payment_status):
        id = len(payments.payments_array)+1
        new_payment = {
            "payment_id":     id,
            "book_id":        book_id, 
            "emission_date":  emission_date, 
            "services_value": services_value, 
            "daily_value":    daily_value, 
            "payment_status": payment_status
            }
        payments.payments_array.append(new_payment)