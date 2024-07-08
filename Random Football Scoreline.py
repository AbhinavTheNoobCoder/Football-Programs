import random
print('''Write the lineups of two football teams to get a random scorecard.
When giving the name of a defender, add (d) to the end of the name.
Similarly for the goalkeeper, use (gk).
For the midfielders, add (m), and for the attackers, add (a) at the end of the name.''')

class Player:
  def __init__(self, name):
    self.name = name
    self.goals = 0
    self.assists = 0

class FootballTeam:
  def __init__(self, name):
    self.name: str = name
    self.starting_xi: list[Player] = []
    self.subs: list[Player] = []
    self.defenders: list[Player] = []
    self.attackers: list[Player] = []
    self.midfielders: list[Player] = []
    self.gk: Player = None
    self.goals_scored: int = 0
    self.goals_timeline: list[str] = []

  def initialiseTeam(self):
    for _ in range(11):
      player = Player(input(f"Enter a player for {self.name}: ").strip(" "))
      if "(D)" in player.name or "(d)" in player.name:
        player.name = player.name.replace("(D)", "")
        player.name = player.name.replace("(d)", "")
        self.defenders.append(player)
      
      elif "(gk)" in player.name or "(GK)" in player.name:
        player.name = player.name.replace("(gk)", "")
        player.name = player.name.replace("(GK)", "")
        self.gk = player
      
      elif "(A)" in player.name or "(a)" in player.name:
        player.name = player.name.replace("(a)", "")
        player.name = player.name.replace("(A)", "")
        self.attackers.append(player)

      elif "(m)" in player.name or "(M)" in player.name:
        player.name = player.name.replace("(m)", "")
        player.name = player.name.replace("(M)", "")
        self.midfielders.append(player)

#accepting two teams
home_team = FootballTeam(input("Enter the home team's name: "))
home_team.initialiseTeam()
print()
away_team = FootballTeam(input("Enter the away team's name: "))
away_team.initialiseTeam()
print()

def scoring(minute):
  opportunity = False
  number = int(random.triangular(1, 100, 50))
  if number >= 95 or number <= 5:
    opportunity = True

  if opportunity:
    scoring_team: FootballTeam = random.choice((home_team, away_team))
    scorer_type = ("A", "M", "A", "M", "D")[int(random.triangular(0, 4, 0))]
    assister_type = ("A", "M", "M", "A", "D")[int(random.triangular(0, 4, 1))]
    type_dict = {"A": scoring_team.attackers, "M": scoring_team.midfielders, "D": scoring_team.defenders}

    if scorer_type == "A":
      scorer = random.choice(scoring_team.attackers)
    
    elif scorer_type == "M":
      scorer = random.choice(scoring_team.midfielders)
    
    else:
      scorer = random.choice(scoring_team.defenders)
    
    possible_assisters = type_dict[assister_type].copy()
    if scorer in possible_assisters:
      possible_assisters.remove(scorer)
    
    assister = random.choice(possible_assisters)
    scorer.goals += 1
    assister.assists += 1
    scoring_team.goals_scored += 1
    if scoring_team == home_team:
     scoring_team.goals_timeline.append(f"{scorer.name} (asst. {assister.name})   {minute}'")
    
    elif scoring_team == away_team:
      scoring_team.goals_timeline.append(f"{minute}'   {scorer.name} (asst. {assister.name})")

additional_time = random.randint(0, 6)
for minute in range(1, 91):
  scoring(minute)

for min in range(additional_time):
    scoring(f"90+{min}")

max_goals = max(home_team.goals_scored, away_team.goals_scored)
print(f"{home_team.name:<40}{home_team.goals_scored} - {away_team.goals_scored}{away_team.name:>40}")
for i in range(max_goals):
  try:
    home_goal = home_team.goals_timeline[i]
  except:
    home_goal = ""
  
  try:
    away_goal = away_team.goals_timeline[i]
  except:
    away_goal = ""

  print(f"{home_goal:<36}\t\t  {away_goal:>36}")
print()
