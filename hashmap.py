# I  can also implement this using dictionaries but I dont know if that's allowed. 
# it's essentially the same idea but this the more "pure" way to do it. 
class HashMap:
    def __init__(self):
        self.hashmap  = []
        for i in range(10):
            self.hashmap.append([])

    def put(self, key, value):
        location = hash(key) % 10
        self.hashmap[location].append(value)

    def get(self, key):
        location = hash(key) % 10
        return self.hashmap[location]

    def toString(self):
        for i in self.hashmap:
            print(i)
            for j in i:
                print("\t" + j)

def main():
    map = HashMap()
    map.put("hello", "world")
    map.put("hello", "fish")
    map.put("hello", "dog")
    map.put("a", "world")
    map.put("a", "fish")
    map.toString()

if __name__ == "__main__":
    main()
    