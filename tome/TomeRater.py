class User(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print('{} email changed to {}'.format(self.name, self.email))

    def __repr__(self):
        return "User {}, email: {}, books read {} ".format(self.name,self.email,self.books)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False
    
    def read_book(self, book, rating=None):
        self.books[book] = rating
        
    def get_average_rating(self):
        rating = 0 
        books_ranked = 0
        
        for score in self.books.values():
            if score is not None:
                rating += score
                books_ranked += 1
        return rating / books_ranked
        

        
class Book:
	def __init__(self,title,isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
		
	def __repr__(self):
		return "{} with ISBN: {}".format(self.title, self.isbn)
	
	def get_title(self):
		return self.title
		
	def get_isbn(self):
		return self.isbn

	def set_isbn(self, update_isbn):
		print ("Setting new isbn number to {} on {}".format(update_isbn,self.title))
		
	def add_rating(self, rating):
		if rating >= 0 and rating < 5:
			self.ratings.append(rating)
		else:
			print("Please set a raiting of 0 to 4, you used {}".format(rating)) 
			
	def __eq__(self, other):
		if self.title == other and self.isbn == other:
			return True
        
		else:return False
            
	def get_average_rating(self):
		points = 0
		for num in self.ratings:
			points += num
		if len(self.ratings) == 0 or points == 0:
			return 0
		else: return points/len(self.ratings)
    		
	def __hash__(self):
		 return hash((self.title, self.isbn))
		 
		 
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
        
	def __repr__(self):
		return "{} written by {}".format(self.title, self.author)
		
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
         return "{} a {} manual about {}".format(self.title, self.level, self.subject)         

class TomeRater:

	def __init__(self):
		self.users = {}
		self.books = {}

	def create_book(self, title, isbn):
		return Book(title, isbn)
		
	def create_novel(self, title, author, isbn):
		return Fiction(title, author, isbn)
		
	def create_non_fiction(self, title, subject, level, isbn):
		return Non_Fiction(title, subject, level, isbn)	
		
	def add_book_to_user(self, book, email, rating=None):
		if email in self.users.keys():
		
			self.users[email].read_book(book,rating)

			if rating is not None:
				book.add_rating(rating)

			if book in self.books.keys():
				self.books[book] += 1
			else:
				self.books[book] = 1
		else:
			return ("{} email not found in user list".format(email))

	def add_user(self, name, email, user_books=None):
		self.users[email] = User(name, email)
		if user_books:
			for book in user_books:
				self.add_book_to_user(book, email)

	def print_catalog(self):
		for bok in self.books.keys():
			print(bok)
			
	def print_users(self):
		for user in self.users.keys():
			print (user)
			
	def most_read_book(self):
		name = ''
		count = 0
		
		for book in self.books.keys():
			if self.books[book].get() > count:
				name = book.title
				count = self.books[book].get()
				
		return("Most read book is {}, it has been read {} times kuk".format(name, count))
		
	def highest_rated_book(self):
		name = ''
		rating = 0
		
		for book in self.books.keys():
			if book.get_average_rating() > rating:
				rating = book.get_average_rating()
				name = book.title
				
		return("Highest rated book is {}, with an average rating of {}.".format(name,rating))

	def most_positive_user(self):
		name = ''
		rating = 0
		
		for user in self.users.values():
			if (user.get_average_rating()) > rating:
				rating = user.get_average_rating()
				name = user.name
				
		return("{} is the most positive user, with a average rating of {}.".format(name, rating))
		
	def get_most_read_book(self):
		name = ''
		count = 0
		
		for book in self.books:
			
			if self.books[book] > count:
				count = self.books[book] 
				name = book.title
				
		return("Most read book is {}, it has been read {} times".format(name, count))