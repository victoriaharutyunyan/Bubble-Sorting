import json

def bubble_sort(books):

    for i in range(0, len(books)-1):
      for j in range(0, len(books)-1-i ):
        if books[j]["publishing date"] > books[j+1]["publishing date"]:
            temp = books[j]
            books[j] = books[j+1]
            books[j+1] = temp

def main():
    def get_data():
        books = {}
        with open("bubble.json") as file_data:
            books = json.load(file_data)

        return books

    books = get_data()
    bubble_sort(books["book"])
    def pretty_print(current, step=0):

      if (type(current) == list):
        for item in current:
            pretty_print (item, step + 1)
            print(", ", end="")
        print("\n", end="")

      elif (type(current) == dict):
        for key in current:
            print("\n", "\t" * step, key, ": ", end="")
            pretty_print(current[key], step+1)

      else:
        print(current, "", end="")

    for obj in books["book"]:
        pretty_print(obj)


main()