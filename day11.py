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

### Part 2 ###
cache: dict[
    tuple[str, bool, bool],
    int
] = {
    ("out", True, True): 1
}

def num_ways_to_out_2(source: str, dac_seen: bool, fft_seen: bool):
    key = (source, dac_seen, fft_seen)
    if key in cache:
        return cache[key]
    elif source == "out":
        cache[key] = 0
        return cache[key]
    
    result = 0
    for destination in edges[source]:
        if destination == "fft":
            result += num_ways_to_out_2(destination, dac_seen, True)
        elif destination == "dac":
            result += num_ways_to_out_2(destination, True, fft_seen)
        else:
            result += num_ways_to_out_2(destination, dac_seen, fft_seen)

    cache[key] = result

    return result

print(num_ways_to_out_2("svr", False, False))
