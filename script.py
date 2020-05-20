import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

for book in bookshelf:
  print(book['title'])

print(ord('a'))
print(ord(' '))
print(ord('A'))

# BUBBLE SORT BY TITLE

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book['title'])
#There were 2 swaps

# BUBBLE SORT BY AUTHOR

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book['author'])
#There were 26 swaps

# QUICKSORT BY AUTHOR

bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
for book in bookshelf_v2:
  print(book['author'])

# BUBBLE SORT & QUICKSORT BY LENGTH

def by_total_length(book_a, book_b):
  return len(book_a['title_lower']) + len(book_a['author_lower']) > len(book_b['title_lower']) + len(book_b['author_lower'])

long_bookshelf = utils.load_books('books_large.csv')
#sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
#There were 1092069 swaps
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)
