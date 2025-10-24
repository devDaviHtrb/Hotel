class books:
    books_array =[]

    def create_book(self, principal_client_id, room_number, checkin_date, checkout_date, book_status, total_value):
        id = len(books.books_array)+1
        new_book = {
            "book_id":             id, 
            "principal_client_id": principal_client_id, 
            "room_number":         room_number, 
            "checkin_date":        checkin_date, 
            "checkout_date":       checkout_date,
            "book_status":         book_status,
            "total_value":         total_value
            }
        books.books_array.append(new_book)