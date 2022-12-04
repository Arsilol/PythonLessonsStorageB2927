from random import *

class University:
	def __init__(self, title, faculty):
		self.title = title
		self.faculty = faculty
		self.budget = False
	def studying(self, name):
		print(name, 'is studying')
	def isbudget(self):
		if self.budget == True:
			print('Congrats! You are on budget')
		else:
			print('Pay money and study!')
class Girlfriend:
	def __init__(self, name):
		self.satisfaction = 0
		self.name = name
		self.money = 100
		self.alive = True
	def ask_satisfaction(self):
		if human.gladness < 20:
			print('*****I dont want to be with you!')
	def ask_money(self):
		if human.money < 0:
			print('****You are too poor!')
			self.alive = False
	def death(self):
		if self.alive == False:
			print("******You have no girlfriend!")
	def ask_progress(self):
		if human.progress < 0:
			print("****You are very unsuccessfull!")
			self.alive = False
	def spend_time(self):
		print('Yeeeee')
		human.gladness += 20
		human.progress -= 10
		self.satisfaction += 20
		if self.satisfaction < 0:
			self.alive = False
		
        
class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 50
		self.progress = 0
		self.alive = True
		self.money = 0
	def ask_budget(self):
		if self.progress >= 50:
			univer.budget = True
	def say_hello(self):
		print('Hello!')
	def to_study(self):
		print('Time to study')
		self.progress += 15
		self.gladness -= 10
		if univer.budget == True:
		    self.money += 40
	def to_sleep(self):
		print('Sleep time')
		self.gladness += 5
		if univer.budget == True:
			self.money += 0 
	def to_chill(self):
		print('Chill time')
		self.gladness += 15
		self.progress -= 5
		if univer.budget == True:            
			self.money -= 20
	def is_alive(self):
		if self.progress < -5:
			print('You are bad student')
			self.alive = False
		elif self.gladness < 15:
			print('Depression...')
			self.alive = False
		elif self.progress > 100:
			print('Amazing!')
			self.alive = False
		elif self.money < 0:
			self.alive = False
			univer.budget = False
		elif self.money >200:
			print('Special session hired')
			self.progress += 50
			self.money  -=100
			self.alive = True
			univer.budget = True
			self.budget = True
	def statistics(self):
		print('Gladness = ', self.gladness, ' Progress = ', self.progress, 'Money = ', self.money)
		print('Budget = ', univer.budget)
	def live(self, day):
		day = 'Day ' + str(day) + ' of ' + self.name + ' life'
		print(day)
		live_cube = randint(1,4)
		if live_cube == 1:
			self.ask_budget()
			self.to_study()
			univer.studying(self.name)
		elif live_cube == 2:
			self.to_sleep()
		elif live_cube == 3:
			self.to_chill()
		elif live_cube == 4:
				self.say_hello()
		girlfriend.ask_satisfaction()
		girlfriend.ask_money()
		girlfriend.ask_progress()
		girlfriend.spend_time()
		self.statistics()
		self.is_alive()

univer = University('Step', 'Computer Science')
human = Student('Anton')
girlfriend = Girlfriend('Natasha')

for day in range(50):
	if human.alive == False:
		break
	human.live(day)