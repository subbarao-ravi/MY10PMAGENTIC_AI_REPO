class Human:
    def __init__(self):
        self.name='SUNNY'
        self.head = self.Head()
        self.brain=self.Brain()

    def display(self):
        print('Hello ', self.name)

    class Head:
        def talk(self):
            print('talking..')

    class Brain:
        def think(self):
            print('thinking...')

human = Human()
human.display()
human.head.talk()
human.brain.think()