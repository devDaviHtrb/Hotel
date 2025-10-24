class type_rooms:
    type_rooms_array = []

    def create_type_room(self, type_name, max_cap, price, details):
        id = len(type_rooms.type_rooms_array)+1
        new_type = {
            "type_id":   id, 
            "type_name": type_name, 
            "max_cap":   max_cap, 
            "price":     price, 
            "details":   details 
            }
        type_rooms.type_rooms_array.append(new_type)
