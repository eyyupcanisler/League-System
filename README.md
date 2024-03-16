# Sports League Management System README

## Introduction:
The Sports League Management System is a Python program designed to manage teams and their statistics for two sports: basketball and football. It allows users to add teams, list all teams, and view detailed information about specific teams.

## Features:
- **Add Basketball Team:** Allows users to add a basketball team to the league, including details such as wins, defeats, scores achieved, scores conceded, total fouls, and total rebounds.
- **Add Football Team:** Enables users to add a football team to the league, providing information such as wins, defeats, draws, scores achieved, and scores conceded.
- **List all teams:** Displays a list of all teams in the league along with basic information such as team ID and name.
- **List specific team:** Allows users to view detailed information about a specific team, including matches played, total points, average score, total fouls, and total rebounds.

## Classes:
### Team:
- Attributes:
  - id: Unique identifier for the team.
  - name: Name of the team.
  - wins: Number of matches won.
  - defeats: Number of matches lost.
  - scoresAchieved: Total scores achieved by the team.
  - scoresConceded: Total scores conceded by the team.
  - average: Average score calculated as scores achieved minus scores conceded.

### Football (inherits from Team):
- Additional Attributes:
  - draws: Number of matches drawn.
- Methods:
  - calculateMatchesPlayed(): Calculates the total number of matches played by the team.
  - calculatePoints(): Calculates the total points earned by the team.
- String Representation:
  - Displays team ID, name, matches played, total points, average score, and additional information for football teams.

### Basketball (inherits from Team):
- Additional Attributes:
  - totalFauls: Total number of fouls committed by the team.
  - totalRebounds: Total number of rebounds achieved by the team.
- Methods:
  - calculateMatchesPlayed(): Calculates the total number of matches played by the team.
  - calculatePoints(): Calculates the total points earned by the team.
- String Representation:
  - Displays team ID, name, matches played, total points, average score, total fouls, and total rebounds for basketball teams.

## Usage:
1. Run the Python script (`sports_league.py`).
2. Choose an option from the menu:
   - Add Basketball Team
   - Add Football Team
   - List all teams
   - List specific team
3. Follow the prompts to input team details or view information about teams.

## Dependencies:
- Python 3.x

