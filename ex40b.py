#exercise 40 2nd part

class Sing(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Sing(["happy birthday to you!"])

ding_dong = Sing(["dingdingding didididingdongsong!"])

happy_bday.sing_me_a_song()
ding_dong.sing_me_a_song()
