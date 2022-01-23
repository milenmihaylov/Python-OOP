from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        animals_count_in_zoo = len(self.animals)
        if animals_count_in_zoo >= self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        workers_count = len(self.workers)
        if workers_count >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.valid_name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for i, worker in enumerate(self.workers):
            if worker.valid_name == worker_name:
                self.workers.pop(i)
                return f"{worker.valid_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.valid_salary
        if total_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care
        if total_money_for_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)

        amount_of_lions = len(lions)
        amount_of_tigers = len(tigers)
        amount_of_cheetahs = len(cheetahs)
        nl = '\n'
        result = f"You have {total_animals_count} animals\n" \
                 f"----- {amount_of_lions} Lions:\n" \
                 f"{nl.join([lion.__repr__() for lion in lions])}\n" \
                 f"----- {amount_of_tigers} Tigers:\n" \
                 f"{nl.join([tiger.__repr__() for tiger in tigers])}\n" \
                 f"----- {amount_of_cheetahs} Cheetahs:\n" \
                 f"{nl.join([cheetah.__repr__() for cheetah in cheetahs])}"
        return result

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)

        amount_of_keepers = len(keepers)
        amount_of_caretakers = len(caretakers)
        amount_of_vets = len(vets)
        nl = '\n'
        result = f"You have {total_workers_count} workers\n" \
                 f"----- {amount_of_keepers} Keepers:\n" \
                 f"{nl.join([keeper.__repr__() for keeper in keepers])}\n" \
                 f"----- {amount_of_caretakers} Caretakers:\n" \
                 f"{nl.join([caretaker.__repr__() for caretaker in caretakers])}\n" \
                 f"----- {amount_of_vets} Vets:\n" \
                 f"{nl.join([vet.__repr__() for vet in vets])}"
        return result
