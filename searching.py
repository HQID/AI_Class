x = [5, 5, 10, 3, 2, 6, 7]

y1 = 4
y2 = 2

def heuristic_search(x, y1, y2):
    for i in range (len(x)):
        if x[i] == y1 or x[i] == y2:
            return x[i]

output = heuristic_search(x, y1, y2)
print(f"Hasil dari pencarian: {output}")
