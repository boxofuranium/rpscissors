class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(f"{self.name}, select rock, paper, or scissors: ")
        print(f"{self.name} selects {self.choice}")

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissors": 2
        }
        return switcher.get(self.choice, -1)  # Return -1 if the choice is invalid

    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(f"Round resulted in a {self.getResultAsString(result, p1, p2)}")

        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        p1_choice = p1.toNumericalChoice()
        p2_choice = p2.toNumericalChoice()
        if p1_choice == -1 or p2_choice == -1:
            return 0  # Return 0 for invalid choices
        return self.rules[p1_choice][p2_choice]

    def getResultAsString(self, result, p1, p2):
        res = {
            0: "draw",
            1: f"{p1.name} wins",
            -1: f"{p2.name} wins"
        }
        return res.get(result, "invalid")

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        while not self.endGame:
            round_result = GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game? (y/n): ")
        if answer.lower() == 'y':
            return
        else:
            print(f"Game ended. {self.participant.name} has {self.participant.points} points, and {self.secondParticipant.name} has {self.secondParticipant.points} points.")
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = f"Winner is {self.participant.name}"
        elif self.participant.points < self.secondParticipant.points:
            resultString = f"Winner is {self.secondParticipant.name}"
        print(resultString)

game = Game()
game.start()