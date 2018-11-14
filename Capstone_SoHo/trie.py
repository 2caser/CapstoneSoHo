#Write Trie Class Here if you choose to implement the Trie

class TireNode(object):


    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

    def __str__(self):
        return self.key

class Trie(object):
    def __init__(self):
        self.head = TireNode("", "")

    
    ### Inserts a string in the trie.  
    
    def insert(self, string):
        current_node = self.head
        final_char = False
        data = string

        for idx, c in enumerate(string):
            if (idx == len(string) - 1):
                final_char = True

            # char already exists
            if c in current_node.children:
                current_node = current_node.children[c]

            # char does not exist, create a new node for the char
            else:
                current_node.children[c] = TireNode(c)
                current_node = current_node.children[c]

            # If the Node represents the final character of the string,
            # set its data to the string.
            if (final_char):
                current_node.data = data

    
    ### Returns if the string exists in the trie
    

    def search(self, string):
        current_node = self.head
        final_char = False

        for idx, c in enumerate(string):
            if (idx == len(string) - 1):
                final_char = True

            if c in current_node.children:
                current_node_node = current_node.children[c]
                # does the current node represent final character?
                if (final_char and current_node.data != None):
                    return True
            else:
                return False
        return False

    
    ### Returns a list of words in the trie
    ### that starts with the given prefix.
    

    def starts_with(self, prefix):
        current_node = self.head
        result = []
        subtrie = None

        # Locate the prefix in the trie
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
                subtrie = current_node
            else:
                return None

        # If prefix exists, search for words in the prefix subtrie
        queue = list(subtrie.children.values())
        '''if current_node == self.head:
          queue = [node for key, node in subtrie.children.values()]
        else:
          queue = [current_node]'''

        while queue:
            current = queue.pop()
            if current.data != None:
                result.append(current.data)

            queue += list(current.children.values())

        return result
