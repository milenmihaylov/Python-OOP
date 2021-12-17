from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ''
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result = f'{subscription}'
                customer_id = subscription.customer_id
                trainer_id = subscription.trainer_id
                break
        for customer in self.customers:
            if customer.id == customer_id:
                result += '\n' + f'{customer}'
                break
        for trainer in self.trainers:
            if trainer.id == trainer_id:
                result += '\n' + f'{trainer}'
                break
        for equipment in self.equipment:
            if equipment.id == subscription_id:
                result += '\n' + f'{equipment}'
                break
        for plan in self.plans:
            if plan.id == subscription_id:
                result += '\n' + f'{plan}'
                break
        return result
