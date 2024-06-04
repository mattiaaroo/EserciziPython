'''class Book:
    def __init__(self, book_id, title, author, is_borrowed=False):
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = is_borrowed

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            return f'{self.book_id} is already borrowed'
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            return f'{self.book_id} is not borrowed yet'
        
    def __str__(self):
        return f'{self.book_id} {self.title} {self.author}'

class Member:
    def __init__(self, member_id, name):
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list = []

    def borrow_book(self, book: Book):
        if book not in self.borrowed_books:
            result = book.borrow()
            if not result:
                self.borrowed_books.append(book)
            else:
                return result
        else:
            return f'Book is already borrowed'

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            result = book.return_book()
            if not result:
                self.borrowed_books.remove(book)
            else:
                return result
        else:
            return f"Book not borrowed by this member"
    
    def __str__(self):
        return f'{self.member_id} {self.name}'

class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
        else:
            return f'Book already exists in the library'

    def register_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
        else:
            return f'Member already registered'

    def borrow_book(self, member_id, book_id):
        if member_id in self.members:
            member = self.members[member_id]
            
            book = self.books[book_id]
            return member.borrow_book(book)
        else:
            return 'Invalid member ID or book ID'

    def return_book(self, member_id, book_id):
        if member_id in self.members:
            member = self.members[member_id]   
            if book_id in self.books:
                book = self.books[book_id]
                return member.return_book(book)
            else: 
                'Book not found'
        else:
            return 'Member not found'
        
    def get_borrowed_books(self, member_id):
        if member_id in self.members:
            member = self.members[member_id]
            return f'{member.borrowed_books}'
        else:
            return 'Invalid member ID'

def anagram(s: str, t: str) -> bool:
    s = sorted(s.lower())
    t = sorted(t.lower())
    for l in range(len(s)):
        result = True
        if s[l] == t[l]:
            pass
        else: 
            return result == False
    return result
        
s = "NeurIPS"
t = "UniReps"
print(anagram(s, t))

#(i//3) * 3 + j//3



def word_break(s: str, wordDict: list[str]) -> bool:
    result = True
    for word in wordDict:
        if word in wordDict:
            s = s[len(word):]
            pass
        else:
            result = False
    return result
        
print(word_break("leetcode",["leet","cod", "de"]))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    lista: list = ListNode
    lista.reverse()
    for l in lista:
        l.reverse()
    return head


head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head))
'''
#(i//3) * 3 + j//3

def valid_sudoku(board: list[list[str]]) -> bool:
    # la tavola del sudo viene rapperentata come una matrice (lista di liste)
    # con 9 righe e 9 colonne
    result = True
    def has_duplicates(lista):
        nums = [x for x in lista if x != '.']
        return len(nums) != len(set(nums))
    
    for row in board:
        if has_duplicates(row):
            return False
        
    for col in range(9):
        if has_duplicates([board[row][col] for row in range(9)]):
            return False
    
    squares: dict = {}
    for l in board:
        for n in l:
            squares[n] = (row//3) * 3 + col//3

    for k, v in squares:
        if squares.count(k[v]) > 1:
            return False
    return True
    




board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
