items = ["apple", "banana", "cherry","orange","banana", "cherry", "apple"]

unique_item = ()

for item in items:
    if item in unique_item:
        print("Duplicate ", item)
        break
    unique_item.add(item)