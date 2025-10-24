class clients:
    clients_array = []

    def create_client(self, complete_name, document, landline, email, sistem_user_id):
        id = len(clients.clients_array)+1
        new_client = {
            "client_id":id, 
            "complete_name":complete_name, 
            "email":email, 
            "hash_pass":hash_pass, 
            "profile_id":profile_id 
            }
        clients.clients_array.append(new_client)
