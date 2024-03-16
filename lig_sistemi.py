class Team:
    league = ""

    def __init__(self, id, name, wins, defeats, scoresAchieved, scoresConceded):
        self.id = id
        self.name = name
        self.wins = wins
        self.defeats = defeats
        self.scoresAchieved = scoresAchieved
        self.scoresConceded = scoresConceded
        self.average = int(self.scoresAchieved) - int(self.scoresConceded)

    def describe(self):
        return f"Team ID: {self.id}, Team Name: {self.name}"


class Football(Team):
    def __init__(self, id, name, wins, defeats, draws, scoresAchieved, scoresConceded):
        self.draws = draws
        super().__init__(id, name, wins, defeats, scoresAchieved, scoresConceded)

    def calculateMatchsPlayed(self):
        return self.wins + self.defeats + self.draws

    def calculatePoints(self):
        return (self.wins * 3) + self.draws

    def __str__(self):
        mn = self.calculateMatchsPlayed()
        p = self.calculatePoints()
        return super().describe() + f" Played match: {mn}, Total Point: {p}, Average Score: {self.average}"


class Basketball(Team):
    def __init__(self, id, name, wins, defeats, scoresAchieved, scoresConceded, totalFauls, totalRebounds):
        self.totalFauls = totalFauls
        self.totalRebounds = totalRebounds
        super().__init__(id, name, wins, defeats, scoresAchieved, scoresConceded)

    def calculateMatchsPlayed(self):
        return int(self.wins) + int(self.defeats)

    def calculatePoints(self):
        return (self.wins * 2) + self.defeats

    def __str__(self):
        mn = self.calculateMatchsPlayed()
        p = self.calculatePoints()
        return super().describe() + f" Played match: {mn}, Total Point: {p}, Average Score: {self.average}\nFauls &" \
                                   f" Rebounds: {self.totalFauls}, {self.totalRebounds}"

leagues = []

while True:
    print("\t1 Add Basketball Team")
    print("\t2 Add Football Team")
    print("\t3 List all teams")
    print("\t4 List specific team")

    mChoice = int(input("Make a choice:"))

    if mChoice == 1:
        idB = int(input("Enter id:"))
        nameB = input("Enter name:")
        winsB = input("Enter Win Number:")
        defeatsB = input("Enter Defeats Number")
        scoresAB = input("Achieved Score:")
        scoresCB = input("Conceded Score:")
        totalF = input("Total Faul:")
        totalR = input("Total Rebound:")
        leagues.append(Basketball(idB, nameB, winsB, defeatsB, scoresAB, scoresCB, totalF, totalR))

    elif mChoice == 2:
        idF = int(input("Enter id:"))
        nameF = input("Enter name:")
        winsF = input("Enter Win Number:")
        defeatsF = input("Enter Defeats Number")
        drawsF = input("Enter Draws Number")
        scoresAF = input("Achieved Score:")
        scoresCF = input("Conceded Score:")
        leagues.append(Football(idF, nameF, winsF, defeatsF, drawsF, scoresAF, scoresCF))

    elif mChoice == 3:
        for team in leagues:
            print(team.describe())

    elif mChoice == 4:
        for team in leagues:
            print(team.describe())

        i = int(input("Enter the team ID:"))
        for team in leagues:
            if team.id == i:
                print(team)
