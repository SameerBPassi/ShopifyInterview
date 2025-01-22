import random

class GiftExchange:
    def __init__(self):
        self.participants = []
        self.partners = {}

    def add_participant(self, name, partner_name):
        self.participants.append(name)
        self.participants.append(partner_name)
        self.partners[name] = partner_name
        self.partners[partner_name] = name
    
    def draw_names(self):
        assignments = {}
        available = self.participants[:]
        random.shuffle(available)

        for name in self.participants:
            drawn = self.pick(name, available)
            if not drawn:
                print("Failed to draw name that passes reqs.")
                return self.draw_names()
            assignments[name] = drawn
            available.remove(drawn)
        return assignments
    
    def pick(self, name, available_names):
        for drawn_name in available_names:
            if drawn_name != name and drawn_name != self.partners[name]:
                return drawn_name
        return None
    
    def view(self, assignments):
        for giver, receiver in assignments.items():
            print(f"{giver} gives to {receiver}")

def main():
    exchange = GiftExchange()

    exchange.add_participant("A", "D")
    exchange.add_participant("B", "E")
    exchange.add_participant("C", "F")

    assignments = exchange.draw_names()

    exchange.view(assignments)

main()