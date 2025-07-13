from Grocery_list import Grocerylist
class TestGrocerylist:

    def test_grocery_create(self):
        assert Grocerylist()

    def test_grocery_add(self):
        grocery_item = "apple"
        assert Grocerylist.add_task(grocery_item)



# assert Grocery_list.save(task,)

# def save(inner_playlist, filepath):
#     """Save current playlist to filepath"""
#     with open(filepath, 'w') as file:
#         json.dump(inner_playlist, file, indent = 4)
#
# def load(filepath) -> list[str]:
#     """Load a new playlist from filepath and return it"""
#     with open(filepath, 'r') as file:
#         return json.load(file)

#test file is created
#test contains all added tasks
