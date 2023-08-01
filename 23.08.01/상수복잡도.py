# O(n)
def constant_algo(items):
    result = items[0] * items[0]
    print(result)

constant_algo([4,5,6,8])

# O(2n) = O(n)
def linear_algo(items):
    for item in items:
        print(item)

    for item in items:
        print(item)

linear_algo([4,5,6,8])
