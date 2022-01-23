from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    _dvd_capacity = 15
    _customer_capacity = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls._dvd_capacity

    @classmethod
    def customer_capacity(cls):
        return cls._customer_capacity

    def add_customer(self, customer: Customer):
        if len(self.customers) < self._customer_capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self._dvd_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_age = None
        dvd_age_restriction = None
        dvd_name = None
        customer_name = None
        customer_index = 0
        for i, customer in enumerate(self.customers):
            if customer.id == customer_id:
                customer_index = i
                customer_age = customer.age
                customer_name = customer.valid_name
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.valid_name} has already rented {dvd.valid_name}"
        dvd_index = 0
        for j, dvd in enumerate(self.dvds):
            if dvd.id == dvd_id:
                dvd_index = j
                dvd_name = dvd.valid_name
                dvd_age_restriction = dvd.age_restriction
                if dvd.is_rented:
                    return "DVD is already rented"

        if customer_age < dvd_age_restriction:
            return f"{customer_name} should be at least {dvd_age_restriction} to rent this movie"

        self.dvds[dvd_index].is_rented = True
        self.customers[customer_index].rented_dvds.append(self.dvds[dvd_index])
        return f"{customer_name} has successfully rented {dvd_name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_name = None
        for customer in self.customers:
            if customer.id == customer_id:
                customer_name = customer.valid_name
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.valid_name} has successfully returned {dvd.valid_name}"
        return f"{customer_name} does not have that DVD"

    def __repr__(self):
        result = [f'{x}' for x in self.customers]
        result.extend([f'{x}' for x in self.dvds])
        return '\n'.join(result)
