# task 12 + 22
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap: # task -1
  def __init__(self, size): # -task 2
    self.array_size = size
    self.array = [LinkedList() for number in range(self.array_size)] # task -13

  def hash(self, key): # -task 3 + 4
    return sum(key.encode())

  def compress(self, hash_code): # -task 5
    return hash_code % self.array_size

  def assign(self, key, value): #- task 6
    array_index = self.compress(self.hash(key))
    # self.array[array_index] = [key, value] #- task 7
    payload = Node([key, value]) # task -14
    list_at_array = self.array[array_index] # task 15


    for item in list_at_array: # task -16
      if key == item[0]:
        item[1] = value # task -17
        return
    list_at_array.insert(payload) # task -18


  def retrieve(self, key): # task 8
    array_index = self.compress(self.hash(key)) # task 9
    list_at_index = self.array[array_index] # task 10 +19
    for item in list_at_index: # task 20 + 21
      if key == item[0]:
        return item[1]
    return None

    # if payload is not None and payload[0] == key: # task 11
    #   return payload[1]
    # else:
    #   return None

# task 23
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions: # task 24
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
