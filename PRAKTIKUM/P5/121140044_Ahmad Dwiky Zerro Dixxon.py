from abc import ABC
from abc import abstractmethod


class person(ABC):

	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	@abstractmethod
	def calculate_income_tax(self):
		pass

class employee(person):

	def __init__(self, name,age,gender,salary):
		super().__init__(name,age,gender)
		self.salary = salary
		self.income = 0

	def calculate_income_tax(self):
		self.income = self.salary*0.10
		print("Income ",self.name," = ",self.income)


class retiree(person):

	def __init__(self, name,age,gender,salary):
		super().__init__(name,age,gender)
		self.salary = salary
		self.income = 0

	def calculate_income_tax(self):
		self.income = self.salary*0.05
		print("Income ",self.name," = ",self.income)


def overloading( *salary ):
	return sum(salary)


objek = [
		employee("daris",15,"pria", 100),
		employee("fikri",30,"pria", 300),
		employee("zhalif",10,"pria", 1000),
		retiree("budi",14,"pria", 500),
		retiree("benedict",14,"pria", 2000),
		retiree("dharmawanti",14,"wanita", 10000),
		]

for idx in objek:
	idx.calculate_income_tax()

print("\nAmount of Income = ",overloading(
										objek[0].income,
										objek[1].income,
										objek[2].income,
										objek[3].income,
										objek[4].income,
										objek[5].income,
										)
										)

