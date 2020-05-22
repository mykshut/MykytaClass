from decimal import Decimal

class Mykyta:
    def __init__(self):
        name = str(input("Hi how can I call you?: "))
        weight = Decimal(input(f'Thank you {name} what is your weight?: ' ))
        print(f'There you can use other commands like:\n[yname - Shows your name]\n[yweight - Shows your weight]\n[splitname - Shows your name and surname]\n[addweight() - help you to add your current weight]\n[email - show your email]\n[inpounds - show your weight in pounds]')
        self.name = name
        self.weight = weight

    @property
    def yname(self):
        return (f'Your name is {self.name}')

    @property
    def yweight(self):
        return (f'{self.name} your weight is {self.weight}')

    @property
    def splitname(self):
        if len(self.name.split()) >= 2:
            return (f'Your name is {self.name.split()[0]} and your surname is {self.name.split()[1]}')
        else:
            raise ValueError("Your nickname must have name and surname")

    @property
    def inpounds(self):
        return (f'Your weight in pounds{self.weight * 2,20462}')

    def addweight(self):
        newweight = Decimal(input("How much do you want to add?: "))
        self.weight += newweight
        return (f'Your new weight is: {self.weight}')

    @property
    def email(self):
        return (f'Email for you is {self.name.split()[0].lower()}.{self.name.split()[1].lower()}@gmail.com')

    def __repr__(self):
        return (f'Your name is {self.name:<10}\n' +
                f'Your weight is {self.weight:<10}\n'
                f'Your email is {self.name.split()[0].lower()}.{self.name.split()[1].lower()}@gmail.com')
