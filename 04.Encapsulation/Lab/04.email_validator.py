class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = set(mails)
        self.domains = set(domains)

    def __is_name_valid(self, name):
        name_length = len(name)
        return False if name_length < self.min_length else True

    def __is_mail_valid(self, mail):
        return True if mail in self.mails else False

    def __is_domain_valid(self, domain):
        return True if domain in self.domains else False

    def validate(self, email: str):
        at_position = email.find('@')
        name = email[:at_position]

        dot_position = email.rfind('.')
        domain = email[dot_position + 1:]

        mail = email[at_position + 1:dot_position]

        if not all([self.__is_name_valid(name), self.__is_domain_valid(domain), self.__is_mail_valid(mail)]):
            return False
        return True


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

email = 'sadasdasd.com'
