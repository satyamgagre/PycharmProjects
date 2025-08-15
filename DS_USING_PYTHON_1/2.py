def print_all_elements(element):
    for item in element:
        print(item)

print_all_elements([1, 2, 3, 4, 5, 6, 7, 8, 9])


def print_pairs(pair):
    for i in pair:
        for j in pair:
            for k in pair:
                print(i, j, k)

print("Triplets")
print_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])


def generate_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    return  matrix

print("\n\n\nMatrix")
print(generate_matrix(4))
