def get_names(garderob):
    # Очередь
    current = garderob.head
    while True:
        try:
            print(current.__getattribute__('name'))
        except Exception:
            print("Очередь пуста")
        if current == garderob.tail:
            break
        try:
            current = current.next_id
        except Exception:
            break


def return_clothes(garderob, id):
    current = garderob.head
    while True:
        if current.__getattribute__('id') == id:
            garderob.delete(id)
            current.previous = None
            current.next_id = None
            return current
        if current == garderob.tail:
            return
        current = current.next_id
    print(current.__getattribute__('id'))
