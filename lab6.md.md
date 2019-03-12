
# Part 1

```
root@DESKTOP-1O100B3:/mnt/c/Users/roched/Documents/csci4966/lab6# python ladder.py
Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ in one letter.
Graph has 5757 nodes with 14135 edges
853 connected components
Shortest path between chaos and order is
chaos
chats
coats
colts
colas
codas
codes
coder
cider
eider
elder
older
order
Shortest path between nodes and graph is
nodes
modes
moles
molds
golds
goads
grads
grade
grape
graph
Shortest path between pound and marks is
None
Shortest path between moron and smart is
moron
boron
baron
caron
capon
capos
capes
canes
banes
bands
bends
beads
bears
sears
stars
start
smart
```


# Part 2

Function generate_graph() was kept unchanged, and is thus ommitted for the sake of brevity.

```
def words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    fh = gzip.open('words4_dat.txt.gz', 'r')
    words = set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w = str(line[0:4])
        words.add(w)
    return generate_graph(words)


if __name__ == '__main__':
    G = words_graph()
    print("Loaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          % (nx.number_of_nodes(G), nx.number_of_edges(G)))
    print("%d connected components" % nx.number_connected_components(G))

    for (source, target) in [('cold', 'warm'),
                             ('love', 'hate')]:
        print("Shortest path between %s and %s is" % (source, target))
        try:
            sp = nx.shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")
```


# Part 3

```
Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ in one letter.
Graph has 2174 nodes with 8040 edges
129 connected components
Shortest path between cold and warm is
cold
cord
word
worm
warm
Shortest path between love and hate is
love
hove
have
hate
```


# Part 4

The modified `generate_graph()` is listed below; all other functions remain identical to the original.

```
def generate_graph(words):
    G = nx.Graph(name="words")
    lookup = dict((c, lowercase.index(c)) for c in lowercase)

    def edit_distance_one(word):
        for perm in permutations(word):
            s = ''.join(perm)
            for i in range(len(s)):
                left, c, right = s[0:i], s[i], s[i + 1:]
                j = lookup[c]  # lowercase.index(c)
                for cc in lowercase[j + 1:]:
                    yield left + cc + right   
         
    candgen = ((word, cand) for word in sorted(words) for cand in edit_distance_one(word) if cand in words)
    
    
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    
    return G
```

# Part 5
The results for the 4 five letter unordered pairs are here:
```
root@DESKTOP-1O100B3:/mnt/c/Users/roched/Documents/csci4966/lab6# python unordered_ladder.py
Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ in one letter.
Graph has 5757 nodes with 112278 edges
16 connected components
Shortest path between chaos and order is
chaos
echos
chore
coder
order
Shortest path between nodes and graph is
nodes
shoed
hades
heaps
phage
graph
Shortest path between pound and marks is
pound
sound
modus
drums
mrads
marks
Shortest path between moron and smart is
moron
moors
morts
smart
```
