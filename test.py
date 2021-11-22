from AdressBook import AdressBook


def test():
    book = AdressBook()

    book.add_record(["Bob", "063 666 99 66", "048 722 22 22"])
    book.add_record(["Nick", "063 666 66 66", "048 222 22 22"])

    book.add_record(["George", "063 666 99 66"])
    book.add_record(["Alex", "063 6879766", "048 722 22 22"])
    book.add_record(["Mark", "063 666 66 66", "048 222 22 22"])
    book.add_record(["John", "063 666 66 66", "048 222 22 22"])
    book.add_record(["John1", "063 666 66 66", "048 222 22 22"])

    # book.show_records()
    print("#" * 10)
    # for record in book:
    #     print(record)
    # next(book.page_iterator())
    # next(book.page_iterator())
    # next(book.page_iterator())
    iter_pages = book.page_iterator(2)
    try:
        print(next(iter_pages))
        print('***')
        print(next(iter_pages))
        print('***')
        print(next(iter_pages))
        print('***')
        print(next(iter_pages))
    except StopIteration:
        print('*End Book*')
    # next(iter_pages)

    # print(book.page_iterator())


test()
