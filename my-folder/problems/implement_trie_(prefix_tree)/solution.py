class Node:
    def __init__(self, symbol: str = "", endpoint: bool = False) -> None:
        self.symbol = symbol
        self.children = {}
        self.endpoint = endpoint
    
    def __repr__(self) -> str:
        return f"Node(s={self.symbol}, e={self.endpoint}, c={self.children})"


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            new_node = node.children.get(char)

            if new_node is None:
                new_node = Node(char)
                node.children[char] = new_node

            node = new_node
        
        node.endpoint = True

    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            new_node = node.children.get(char)
        
            if new_node is None:
                return False
        
            node = new_node
        
        return node.endpoint

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            new_node = node.children.get(char)
        
            if new_node is None:
                return False
        
            node = new_node
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)