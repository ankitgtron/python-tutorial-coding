def process_file():
    try:
        f = open("H:\\book.txt")
        x = 1 / 0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        print("cleaning up file")
        f.close()
process_file()
