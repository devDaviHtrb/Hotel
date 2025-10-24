class rooms:
    rooms_array = []

    def createroom(self, room_number, type_id, cleaning_status, location):
        id = len(rooms.rooms_array)+1
        new = {
            "id":              id, 
            "room_number":     room_number, 
            "type_id":         type_id, 
            "cleaning_status": cleaning_status, 
            "location":        location
            }
        rooms.rooms_array.append(new)