# ============================================
# PYTHON DICTIONARY EXAMPLES
# ============================================


# --------------------------------------------
# Example 1: Creating a Dictionary
# This creates a dictionary with key-value pairs.
# --------------------------------------------
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("Example 1 - Created Dictionary:", dict1)


# --------------------------------------------
# Example 2: Accessing Values from Dictionary
# This accesses values using keys.
# --------------------------------------------
print("\nExample 2 - Accessing Values")
print("Name:", dict1['Name'])
print("Age:", dict1['Age'])


# --------------------------------------------
# Example 3: Updating Dictionary
# This updates existing values and adds new ones.
# --------------------------------------------
print("\nExample 3 - Updating Dictionary")

dict1['Age'] = 8                 # Update existing key
dict1['School'] = "DPS School"   # Add new key-value pair

print("Updated Age:", dict1['Age'])
print("Added School:", dict1['School'])


print("\nExample 4 - Deleting Dictionary Elements")

dict2 = {'Name': 'hitesh', 'Age': 7, 'Class': 'First'}
print("Before Deletion:", dict2)

del dict2['Name']      # Delete a single key
print("After deleting Name:", dict2)

dict2.clear()          # Clear all items
print("After clearing dict:", dict2)

del dict2print("Dictionary deleted successfully")

# --------------------------------------------
print("\nExample 5 - Looping Through Dictionary")

dict3 = {'Name': 'hitesh', 'Age': 7, 'Class': 'First'}

for key, value in dict3.items():
    print(key, "-", value)
