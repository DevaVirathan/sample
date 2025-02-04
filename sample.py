class CRUD:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        if key in self.data:
            return "Key already exists."
        else:
            self.data[key] = value
            return "Record created."

    def read(self, key):
        return self.data.get(key, "Key not found.")

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
            return "Record updated."
        else:
            return "Key not found."

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            return "Record deleted."
        else:
            return "Key not found."

# Example usage
crud = CRUD()
print(crud.create("1", "Record 1"))  # Record created.
print(crud.read("1"))  # Record 1
print(crud.update("1", "Updated Record 1"))  # Record updated.
print(crud.read("1"))  # Updated Record 1
print(crud.delete("1"))  # Record deleted.
print(crud.read("1"))  # Key not found.
print("crud operation")
