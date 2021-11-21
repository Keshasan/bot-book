from AdressBook import AddressBook


def test():
    book = AddressBook()
    book.add_record(["Yehor", "063 666 99 66", "048 722 22 22"])
    book.add_record(["Pavel", "063 666 66 66", "048 222 22 22"])

    book.delete_record("Yehor")
    book.add_record(["Yehor", "063 666 99 66", "048 333 333 3"])

    # print(record)
    # print("\n")
    # print("#" * 10)
    # record.delete_phone("048 222 22 22")
    # record.edit_phone("095 666 66 66", "067 666 66 66")
    # print(record)
    print("#" * 10)

    # YYYY-MM-DD
    # record.add_birthday('1993-11-15')
    # print(record.days_to_birthday())
    # print("#" * 10)
    book.add_record(["Bob", "063 666 99 66", "048 722 22 22"])
    book.add_record(["Nick", "063 666 66 66", "048 222 22 22"])

    book.add_record(["George", "063 666 99 66"])
    # book.add_record(["John", "063 666 66 66", "048 222 22 22"])

    # book.show_records()
    print("#" * 10)
    # for record in book:
    #     print(record)
    # next(book.page_iterator())
    # next(book.page_iterator())
    # next(book.page_iterator())
    iter_pages = book.page_iterator(2)
    try:
        next(iter_pages)
        next(iter_pages)
        next(iter_pages)
    except StopIteration:
        print('*End Book*')
    # next(iter_pages)

    # print(book.page_iterator())


test()
