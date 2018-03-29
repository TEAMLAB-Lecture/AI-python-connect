from teamlab_note import NoteBook
from teamlab_note import Note

quote_book = NoteBook("The Quote Book")

new_note = Note()
new_note.write_content("Don't cry because it's over, smile because it happened. ― Dr. Seuss")
quote_book.add_note(new_note)

print(quote_book.get_number_of_pages())

quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))

print(quote_book.get_number_of_pages())

my_note = quote_book.remove_note(1)
print(my_note)
my_note = quote_book.remove_note(1)
print(my_note)
