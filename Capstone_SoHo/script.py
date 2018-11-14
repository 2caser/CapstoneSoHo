from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

### Printing the Welcome Message
print_welcome()

### Write code to insert food types into a data structure here. The data is in data.py
t = Trie()
for word in types:
  t.insert(word)



### Write code to insert restaurant data into a data structure here. The data is in data.py
hash_data = HashMap(len(restaurant_data))
for type in types:
  ll = LinkedList()
  for data in restaurant_data:
    if type == data[0]:
      ll.insert_beginning(data)
      hash_data.assign(type,ll)
      #print("**************",hash_data.retrieve((type)))
  
# finding food type for retrieving restaurant data here          

def restaurants_in_soho(usr_input):
  lln = hash_data.retrieve((usr_input))
  head_node = lln.get_head_node()
  while head_node.value != None:
    print("\n")
    print("Name: {}".format(head_node.value[1]))
    print("----------------------");
    print("Type: {}".format(head_node.value[0]))
    print("Price: {}/5".format(head_node.value[2]))
    print("Rating: {}/5".format(head_node.value[3]))
    print("Address: {}".format(head_node.value[4]))
    #print("\n")
    head_node = head_node.get_next_node()


#Write code for user interaction here
while True:
  
  #Search for user_input in food types data structure here
    user_input = str(input("\nWhat type of food would you like to eat?\n\nType the beginning of that food type and press enter to see if it's in SoHo or 'quitting' to exit\n")).lower()
    if user_input == 'quitting':
      print("\nThanks for considering SoHo restaurants!")
      exit()
    if user_input.isalpha():
      beginning_letter = t.starts_with(user_input)
      if beginning_letter == None:
        print("\n*** Please try again!! ***, no letters beginning with letter '{}'\n".format(user_input))
        continue
      elif len(beginning_letter) > 1:
        print("\nWith those begining letters, your choices are:\n", beginning_letter)
        continue
      elif user_input in types:
        restaurants_in_soho(user_input)
      elif len(beginning_letter) == 1:
        print("The only option with those begining letter is ", (beginning_letter[0]))
        print("Do you want to look at '{}' restaurants, please select 'y' for yes and 'n' for no.\n".format(beginning_letter[0]))
        y_n_input = str(input('y/n: ')).lower()
        if y_n_input == 'y':
          print("The '{}' restaurants in SoHo are .......\n".format(beginning_letter[0]))
          restaurants_in_soho(beginning_letter[0])
        elif y_n_input == 'n':
          print("selected 'No'!")
          continue
        else:
          print("\nTry again, wrong selection!!")
          continue
        break
    else:
      exit()
print("\n*** Thanks for considering SoHo restaurants! ***")
exit()
