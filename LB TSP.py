distance = {
    ('A','B'): 12,
    ('A','C'): 25,
    ('A','D'): 18,
    ('B','C'): 20,
    ('B','D'): 35,
    ('C','D'): 10
}

def calculate(route):
    total = 0

    for i in range(len(route)-1):
        pair = (route[i], route[i + 1])

        if pair in distance:
            total += distance[pair]
        else:
            total += distance[(pair[1], pair[0])]

    pair = (route[-1], route[0])

    if pair in distance:
        total += distance[pair]
    else:
        total += distance[(pair[1], pair[0])]

    return total

beam = [
    ['A','B','C','D'],
    ['A','C','B','D']
]

for step in range(5):
    new_routes = []
    for route in beam:
        for i in range(1,4):
            new_route = route.copy()

            j = (i + 1) % 4

            if j !=0:
                new_route[i], new_route[j] = new_route[j], new_route[i]
                new_routes.append(new_route)

        unique_routes = []
        for route in new_routes: 
            if route not in unique_routes: 
                unique_routes.append(route) 

            unique_routes.sort(key=calculate)   

            print("\nIteration:", step + 1)
            print("All generated routes:")

            for route in unique_routes: 
                print(route, "Distance:", calculate(route)) 

            beam = unique_routes[:2] 
            print("Selected routes:", beam) 

            best = min(beam, key=calculate) 

            print("\nBest Route:", best + [best[0]])
            print("Total Distance:", calculate(best))
                  