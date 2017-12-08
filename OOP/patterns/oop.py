class Robot:
    """Represents robot, with a name"""

    # class variable
    __population = 0
    # __actives = 0

    def __init__(self, name, energy=20):
        """Initializes the data"""
        self.name = name
        self.energy = energy
        self.active = True
        print("(Initializing {name})".format(name=self.name))

        Robot.__population += 1

        # self.check_active()

    def die(self):
        """I am dying."""
        print("{name} is being destroyed ".format(name=self.name))

        Robot.__population -= 1

        if Robot.__population == 0:
            print('{name} was the last one.'.format(name=self.name))
        else:
            print("There are still {population:d} robots".format(population=Robot.__population))

    # def check_active(self):
    #     """Check if robot have enough energy to by active""""
    #
    #     if self.energy > 0:
    #         self.activate()
    #         Robot.__actives += 1
    #     else:
    #         self.deactivate()
    #         Robot.__actives -= 1
    #
    # def deactivate(self):
    #     """Deacttivate robot"""
    #     self.active = False
    #
    #
    # def activate(self):
    #     """Activate robot"""
    #     self.active = True
    #
    #
    # def increase_energy(self, energy):
    #     """Increase robot's energy"""
    #     self.energy += energy
    #
    # def decrease_energy(self, energy):
    #     """Decrease robot's energy"""
    #     self.energy -= energy

    #getter
    #setter -increase
    #setter -decrease

    def say_hi(self):
        """Greeting by the robot

        Yeah, they can do that."""
        print("Greeting, my masters call me {name}.".format(name=self.name))

    @classmethod
    def how_many(cls):
        """Print the current population."""
        print("We have {population:d}".format(population=cls.__population))

    @classmethod
    def how_many_active(cls):
        """Print the current population."""
        print("We have {active:d}".format(population=cls.__actives))


droid1 = Robot("R2-D2")
droid1.say_hi()
droid1.how_many()


try:
    print(droid1.__population)
except AttributeError as e:
    print("not accesible from instance of Robot class")
    print(e)

try:
    print(Robot.__population)
except AttributeError as e:
    print("not accesible on Robot class")
    print(e)

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()

Robot.how_many()
