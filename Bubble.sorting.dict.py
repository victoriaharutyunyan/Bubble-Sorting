
def bubble_sort(books):

    for i in range(0, len(books)-1):
      for j in range(0, len(books)-1-i ):
        if books[j]["publishing date"] > books[j+1]["publishing date"]:
            temp = books[j]
            books[j] = books[j+1]
            books[j+1] = temp

def main():
    books = [{"Name1": "The Arc Of Triumph",
              "publishing date": 1945,
              "author": "Erich Maria Remarque"},
             {"Name": "Like Death",
              "publishing date": 1889,
              "author": "Guy de Muapassant"},
             {"Name": " A Time to love and a Time to die",
              "publishing date": 1958,
              "author": "Erich Maria Remarque"},
             ]
    bubble_sort(books)
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

    for obj in books:
        pretty_print(obj)


main()




