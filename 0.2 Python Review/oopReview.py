class YoutubeVideo:
	def __init__(self, title, description, likes, dislikes, comments):
		self.title = title
		self.description = description
		self.likes = likes
		self.dislikes = dislikes
		self.comments = comments

def like(likes): 
	print (likes + 1)

def dislike(dislikes):
	print (dislikes + 1)

def add_comment(comments):
	username = input('Enter your Username:')
	print('Hello, ' + username)
	comment = input("What is your comment?")
	print(comment)
	
def print_info(YoutubeVideo):
	print(title)
	print(description)
	print(likes)
	print(dislikes)
	print(comments)

class Utube:
	like = (like + "495")

Test = Utube()
print(Test.likes)











