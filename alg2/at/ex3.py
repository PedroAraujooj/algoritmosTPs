class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class BookTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, title):
        node = self.root
        for char in title:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, title):
        node = self.root
        for char in title:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, title):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete_child = _delete(node.children[char], word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            return False

        _delete(self.root, title, 0)

    def list_titles(self):
        def _dfs(node, prefix, titles):
            if node.is_end_of_word:
                titles.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, titles)

        titles = []
        _dfs(self.root, "", titles)
        return titles

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        def _dfs(current_node, current_prefix, suggestions):
            if current_node.is_end_of_word:
                suggestions.append(current_prefix)
            for char, child in current_node.children.items():
                _dfs(child, current_prefix + char, suggestions)

        suggestions = []
        _dfs(node, prefix, suggestions)
        return suggestions

    @staticmethod
    def levenshtein_distance(a, b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1],
                                       dp[i - 1][j - 1])
        return dp[m][n]

    def autocorrect(self, word):

        titles = self.list_titles()
        if not titles:
            return []
        distances = {title: self.levenshtein_distance(word, title) for title in titles}
        min_distance = min(distances.values())
        suggestions = [title for title, distance in distances.items() if distance == min_distance]
        return suggestions

    def show_hierarchy(self):
        def dfs(char, node, depth):
            if char is not None:
                print("   " * depth + f"{char}")
            for c, child in node.children.items():
                dfs(c, child, depth + 1)

        for c, child_node in self.root.children.items():
            dfs(c, child_node, 0)

if __name__ == "__main__":
    trie = BookTrie()
    trie.insert("O Senhor dos Aneis")
    trie.insert("O Hobbit")
    trie.insert("O Codigo da Vinci")
    trie.insert("Os Miseraveis")
    trie.insert("Narnia")
    trie.insert("O Segredo")
    trie.insert("Mindset")

    print("Todos os livros:")
    print(trie.list_titles())

    prefix = input("\nEntre com o prefixo do livro: \n")
    print(f"Livros com o começo '{prefix}'")
    print(trie.autocomplete(prefix))

    possivel_livro = input("\n Entre com o nome do livro que você quer achar: ")
    print(f"Livro que o usuario quer achar '{possivel_livro}', possivel resultado'{trie.autocorrect(possivel_livro)}'")
