class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def host_event(self):
        print("Hosting adoption event with participants:")
        for p in self.participants:
            print(p)

    def register_participant(self, participant):
        self.participants.append(participant)
