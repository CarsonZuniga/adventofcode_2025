with open("day11.txt") as f:
    lines = [line.strip() for line in f]

edges = {}
reverse_edges = {}

for line in lines:
    source, dest = line.split(": ")
    destinations = dest.split()
    edges[source] = destinations
    for destination in destinations:
        reverse_edges[destination] = reverse_edges.get(destination, []) + [source]

### Part 1 ###
### We can assume there are no cycles, or else the number of paths from you -> out would be infinite

cache = {
    "out": 1
}

def num_ways_to_out(source):
    if source in cache:
        return cache[source]
    
    result = 0
    for destination in edges[source]:
        result += num_ways_to_out(destination)

    cache[source] = result

    return result

print(num_ways_to_out("you"))
