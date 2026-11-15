class Head:
    def __init__(self):
        self.name='SUBBARAO'
    print("Head object created...")

    def headMethod(self):
        print('Head object created for ',self.name)


    class Brain:
        def __init__(self,head):
            self.brain = 'SUPER BRAIN'
            self.head = head
        print("Brain object created...")

        def BrainMethod(self):
            print('The Brain is a ',self.brain)
            self.head.headMethod()

head = Head()
brain = head.Brain(head)
brain.BrainMethod()
