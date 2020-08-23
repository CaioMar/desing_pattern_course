class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


class Mediator:
    def __init__(self):
        self.participants = []

    def broadcast(self, source, value):
        for participant in self.participants:
            if participant != source:
                participant.value += value

if __name__ == "__main__":
    mediator = Mediator()

    p1 = Participant(mediator)
    p2 = Participant(mediator)

    p1.say(3)
    print(p1.value, p2.value)

    p3 = Participant(mediator)
    p2.say(5)

    print(p1.value, p2.value, p3.value)