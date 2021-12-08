class Profile:
    min_username_length = 5
    max_username_length = 15

    min_password_length = 8

    def __init__(self, username: str, password: str, ):
        self.username = username
        self.password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

    def __validate_username(self, value):
        username_length = len(value)
        if not self.min_username_length <= username_length <= self.max_username_length:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    def __validate_password(self, value):
        upper_case = False
        digit = False
        if len(value) < self.min_password_length:
            self.__raise_error()
        for ch in value:
            if ch.isupper():
                upper_case = True
            elif ch.isdigit():
                digit = True
            if upper_case and digit:
                break

        if not (upper_case and digit):
            self.__raise_error()

    def __raise_error(self):
        raise ValueError(f"The password must be {self.min_password_length} or more characters "
                         f"with at least 1 digit and 1 uppercase letter.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        self.__validate_password(value)
        self.__password = value


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
