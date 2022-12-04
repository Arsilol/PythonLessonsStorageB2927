# from random import *

# class University:
# 	def __init__(self, title, faculty):
# 		self.title = title
# 		self.faculty = faculty
# 		self.budget = False
# 	def studying(self, name):
# 		print(name, 'is studying')
# 	def isbudget(self):
# 		if self.budget == True:
# 			print('Congrats! You are on budget')
# 		else:
# 			print('Pay money and study!')
# class Girlfriend:
# 	def __init__(self, name):
# 		self.satisfaction = 0
# 		self.name = name
# 		self.money = 100
# 		self.alive = True
# 	def ask_satisfaction(self):
# 		if human.gladness <= 20:
# 			print('*****I dont want to be with you!')                      
# 	def ask_money(self):
# 		if human.money <= 0:
# 			print('****You are too poor!')
# 			self.alive = False
# 	def death(self):
# 		if self.alive == False:
# 			print("******You have no girlfriend!")
# 	def ask_progress(self):
# 		if human.progress <= -10:
# 			print("****You are very unsuccessfull!")
# 			self.alive = False
# 	def spend_time(self):
# 		print('Yeeeee')
# 		human.gladness += 20
# 		human.progress -= 10
# 		self.satisfaction += 20
# 		if self.satisfaction < 0:
# 			self.alive = False
		
        
# class Student:
# 	def __init__(self, name):
# 		self.name = name
# 		self.gladness = 50
# 		self.progress = 0
# 		self.alive = True
# 		self.money = 50
# 	def ask_budget(self):
# 		if self.progress >= 30:
# 			univer.budget = True
# 	def say_hello(self):
# 		print('Hello!')
# 	def to_study(self):
# 		print('Time to study')
# 		self.progress += 15
# 		self.gladness -= 10
# 		if univer.budget == True:
# 		    self.money += 40
# 	def to_sleep(self):
# 		print('Sleep time')
# 		self.gladness += 5
# 		if univer.budget == True:
# 			self.money += 0 
# 	def to_chill(self):
# 		print('Chill time')
# 		self.gladness += 15
# 		self.progress -= 5            
# 		self.money -= 10
# 	def is_alive(self):
# 		if self.progress < -5:
# 			print('You are bad student')
# 			self.alive = False
# 		elif self.gladness < 15:
# 			print('Depression...')
# 			self.alive = False
# 		elif self.progress > 100:
# 			print('Amazing!')
# 			self.alive = False
# 		elif self.money < 0:
# 			self.alive = False
# 			univer.budget = False
# 		elif self.money >200:
# 			print('Special session hired')
# 			self.progress += 50
# 			self.money  -=100
# 			self.alive = True
# 			univer.budget = True
# 			self.budget = True
# 	def statistics(self):
# 		print('Gladness = ', self.gladness, ' Progress = ', self.progress, 'Money = ', self.money)
# 		print('Budget = ', univer.budget)
# 	def live(self, day):
# 		day = 'Day ' + str(day) + ' of ' + self.name + ' life'
# 		print(day)
# 		live_cube = randint(1,4)
# 		if live_cube == 1:
# 			self.ask_budget()
# 			self.to_study()
# 			univer.studying(self.name)
# 		elif live_cube == 2:
# 			self.to_sleep()
# 		elif live_cube == 3:
# 			self.to_chill()
# 		elif live_cube == 4:
# 				self.say_hello()
# 		if girlfriend.alive == True:
# 			girlfriend.ask_satisfaction()
# 			girlfriend.ask_money()
# 			girlfriend.ask_progress()
# 		# girlfriend.spend_time()
# 		self.statistics()
# 		self.is_alive()

# univer = University('Step', 'Computer Science')
# human = Student('Anton')
# girlfriend = Girlfriend('Natasha')

# for day in range(50):
# 	if human.alive == False:
# 		break
# 	human.live(day)


# class Human:
# 	def __init__(self, name):
# 		self.name = name
# 		self.appearance = 5
# 		self.status = False
# 	def live(self):
# 		print(self.name, 'is alive')
# 	def eat(self):
# 		print('Eating time')

# class Woman(Human):
# 	def live(self):
# 		super().live()
# 		print('What a wonderful day of', self.name)
# 	def cook(self):
# 		print(self.name, 'is cooking')
		
# class Man(Human):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.money = 50
# 	def work(self):
# 		self.money += 10
# 		print(self.name, 'is working')
# 		print('Money: ', self.money)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.cuteness = 10
#     def live(self):
#         print(self.name, 'is alive')
#     def sleep(self):
#         print('Sleeping time!')
#     def eat(self):
#         print("Eating time!")
#     def play(self):
#         print('Playing time!')

# class dog(Animal):
# 	def live(self):
# 		super().live()
# 		print('What a wonderful day of a dog named', self.name)
# 	def hunt(self):
# 		print(self.name, 'is going for a hunt!')
# 		self.cuteness -= 10
# 		print('Cuteness: ', self.cuteness)

# class cat(Animal):
# 	def live(self):
# 		super().live()
# 		print('What a wonderful day of a cat named', self.name)
# 	def playwithowner(self):
# 		self.cuteness += 50
# 		print(self.name, 'is playing with you!')
# 		print('Cuteness: ', self.cuteness)

# class hamster(Animal):
#     def live(self):
#         super().live()
#         print('What a wonderful day of a hamster named', self.name)
#     def runinawheel(self):
#         self.cuteness += 25
#         print(self.name, 'is running in a wheel!')
#         print('Cuteness: ', self.cuteness)
    




# human = Human('Bob')
# human.live()
# w1 = Woman('Clara')
# w1.live()
# w1.cook()
# m1 = Man('John')
# m1.live()
# m1.work()
# animal = Animal('Cute animal')
# animal.live()
# d1 = dog('Rudolf')
# d1.live()
# d1.hunt()
# c1 = cat('Cutie')
# c1.live()
# c1.playwithowner()
# h1 = hamster('Puhlya')
# h1.live()
# h1.runinawheel() 



from random import *
class Cat:
    def __init__(self, name):
        self.name = name
        self.cuteness = 50
        self.progress = 0
        self.alive = True
    def say_meow(self):
        print('Meow')
    def to_hunt(self):
        print('Time to hunt!')
        self.progress += 5
        self.cuteness -= 15
    def to_sleep(self):
        print('Sleep time!')
        self.progress += 5
        self.cuteness += 10
    def to_play(self):
        print('Playtime!')
        self.cuteness += 20
        self.progress -= 5
    def to_donothing(self):
        print('Time to chill!')
        self.progress -= 10
        self.cuteness += 5
    def is_alive(self):
        if self.progress < -10:
            print('You are bad cat!')
            self.alive = False
        elif self.progress > 50:
            print('The most successful cat on the west!')
            self.alive = True
        elif self.cuteness < 20:
            print('Not a cute cat!')
            self.alive = False
        elif self.cuteness > 100:
            print('Cutest cat on the west!')
    def statistics(self):
            print(' Progress = ', self.progress, 'Cuteness =', self.cuteness)
    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' life'
        print(day)
        live_cube = randint(1,5)
        if live_cube == 1:
            self.say_meow()
        elif live_cube == 2:
            self.to_hunt()
        elif live_cube == 3:
            self.to_sleep()
        elif live_cube == 4:
            self.to_play()
        elif live_cube == 5:
            self.to_donothing()
        self.statistics()
        self.is_alive()

cat = Cat('Cute cat')
for day in range(30):
	if cat.alive == False:
		break
	cat.live(day)

