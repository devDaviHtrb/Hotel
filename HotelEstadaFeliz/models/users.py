class users:
    users_array = []

    def create_user(self, complete_name, email, hash_pass, profile_id):
        id = len(users.users_array)+1
        new_user = {"user_id":id, "complete_name":complete_name, "email":email, "hash_pass":hash_pass, "profile_id":profile_id }
        users.users_array.append(new_user)
