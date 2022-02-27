# -*- coding: utf-8 -*-
my_name = "Sefa"
my_id = "200102002026"
my_email = "s.bazan2020@gtu.edu.tr"

import random

class Person:

    def __init__(self,name, lastname) -> None:

        self.name=name
        self.lastname=lastname

    def get_name(self):
        return self.name+' '+self.lastname
    def __str__(self) -> str:
        return self.name+' '+self.lastname
    def __lt__(self,other):
        if len(self.lastname) == len(other.lastname):
            return len(self.name) < len(other.name)
        else:
            return len(self.lastname) < len(other.lastname)

class Player(Person):
    id_counter=0
    def __init__(self, name, lastname) -> None:
        Person.__init__(self,name, lastname)
        Player.id_counter+=1
        self.id=Player.id_counter
        self.power=random.randint(4,8)
        self.weeklyPoints=[]
        self.totalPoints=0
        self.periodPoints=[]
    def reset(self):
        self.totalPoints=0
        self.weeklyPoints.clear()
        self.periodPoints.clear()
    def get_id(self):
        return self.id
    def get_power(self):
        return self.power
    def set_team(self,t):
        self.playerteam=t
    def get_team(self):
        return self.playerteam
        #This method will get the manager's team as a Team instance.
        # Explanation it prints using Team's __str__ method.

    def add_to_period_points(self,x):
        self.periodPoints.append(x)
    def add_periods_points(self):
        self.add_to_points(sum(self.periodPoints))
        self.periodPoints.clear()
    def get_exact_week_performance(self,week):
        return self.weeklyPoints[week-1] #weeklerden 1 den başlar ama indexler 0'dan
    def add_to_points(self,x):
        self.totalPoints+=x
        self.weeklyPoints.append(x)
    def get_points(self):
        return self.totalPoints
    def get_points_detailed(self):
        return self.weeklyPoints
    def __lt__(self, other):
        if self.totalPoints==other.totalPoints:
            return Person.__lt__(self,other)
        else:
            return self.totalPoints<other.totalPoints
    def __str__(self) -> str:
        return self.get_name()
class Manager(Person):

    id_counter=0
    def __init__(self, name, lastname) -> None:
        Person.__init__(self,name, lastname)
        Manager.id_counter+=1
        self.id=Manager.id_counter
        self.WeeklyInfluencePoints=[]
        self.totalInfluence=0
        self.Fullname=name+' '+lastname
    def reset(self):
        self.WeeklyInfluencePoints.clear()
        self.totalInfluence=0
    def get_id(self):
        return self.id
    def set_team(self,t):
        self.ManagerTeam=t
    def set_influence(self,x):
        self.WeeklyInfluencePoints.append(x)
        self.totalInfluence+=x
    def get_team(self):
        return self.ManagerTeam

        #This method will get the manager's team as a Team instance.
    def get_influence(self):
        return self.totalInfluence
    def get_influence_detailed(self):
        return self.WeeklyInfluencePoints
    def get_exact_week_influence(self,week):
        return self.WeeklyInfluencePoints[week-1]
    def __lt__(self, other):
        if self.totalInfluence == other.totalInfluence:
            return Person.__lt__(other)
        else:
            return self.totalInfluence < other.TotalInfluence
    def __str__(self) -> str:
        return self.get_name()
class Team:

    id_counter=0
    def __init__(self,teamname,manager,players) -> None:
        Team.id_counter+=1
        self.id=Team.id_counter
        self.playerList=players
        self.teamName=teamname
        self.manager=manager
        self.teamFixture=[]
        self.results=[]
        self.total_scored=0
        self.total_conceded=0
        self.wins=0
        self.losses=0
        manager.set_team(self)
    def reset(self):
        self.wins=0
        self.losses=0
        self.total_scored=0
        self.total_conceded=0
        self.results.clear()
        for player in self.playerList:
            player.reset()
        self.manager.reset()
        self.teamFixture.clear()
    def get_id(self):
        return self.id
    def get_name(self):
        return self.teamName
    def get_roster(self):
        return self.playerList
    def get_manager(self):
        return self.manager
    def add_to_fixture(self,m):
        self.teamFixture.append(m)
    def get_fixture(self):
        return self.teamFixture
    def add_result(self,s):
        self.results.append(s)
        if s[0] > s[1]:
            self.wins+=1
        else:
            self.losses+=1
        self.total_scored+=s[0]
        self.total_conceded+=s[1]
    def get_scored(self):
        return self.total_scored
    def get_conceded(self):
        return self.total_conceded
    def get_wins(self):
        return self.wins
    def get_losses(self):
        return self.losses
    def __str__(self) -> str:
        return self.teamName
    def __lt__(self,other):
        if self.wins == other.wins:
            return self.total_scored-self.total_conceded <= other.total_scored-other.total_conceded
        else:
            return self.wins < other.wins

class Match:
    def __init__(self,home_team,away_team,week_no) -> None:
        self.homeTeam=home_team
        self.awayTeam=away_team
        self.is_played=False
        self.homePoints=0
        self.awayPoints=0
        home_team.add_to_fixture(away_team)
        away_team.add_to_fixture(home_team)
        self.matchWeek=week_no
    def is_played(self):
        return self.is_played
    def play(self):
        HomeManagerInf=random.randint(-10,10)
        AwayManagerInf=random.randint(-10,10)
        self.homePoints+=HomeManagerInf
        self.awayPoints+=AwayManagerInf
        self.homeTeam.manager.set_influence(HomeManagerInf)
        self.awayTeam.manager.set_influence(HomeManagerInf)

        def playperiod():
            periodpoint_home=0
            players_Home=self.homeTeam.get_roster()
            
            for player in players_Home:
                playerAddition=player.get_power()+random.randint(-5,5)
                periodpoint_home+=playerAddition
                player.add_to_period_points(playerAddition)

            periodpoint_away=0
            players_Away=self.awayTeam.get_roster()
            for player in players_Away:
                playerAddition=player.get_power()+random.randint(-5,5)
                periodpoint_away+=playerAddition
                player.add_to_period_points(playerAddition)
            return periodpoint_home,periodpoint_away
        def endMatch():
            periodcounter=1
            while periodcounter!=5:
                plusHome,plusAway=playperiod()
                self.homePoints+=plusHome
                self.awayPoints+=plusAway
                periodcounter+=1
                if periodcounter==5 and self.homePoints==self.awayPoints:
                    periodcounter-=1
        endMatch()
        players_Home=self.homeTeam.get_roster()
        for player in players_Home:
            player.add_periods_points()
        players_away=self.awayTeam.get_roster()
        for player in players_away:
            player.add_periods_points()
        self.homeTeam.add_results(self.get_match_score())
        self.is_played=True
    def get_match_score(self):
        return self.homePoints,self.awayPoints
    def get_teams(self):
        return self.homeTeam,self.awayTeam
    def get_home_team(self):
        return self.homeTeam
    def get_away_team(self):
        return self.awayTeam
    def get_winner(self):

        if self.homePoints > self.awayPoints:
            winner=self.homeTeam
        else:
            winner=self.awayTeam

        return winner if self.is_played else None
    def __str__(self) -> str:
        if self.is_played:
            return '{} ({}) vs ({}) {}'.format(self.homeTeam,self.homePoints,self.awayPoints,self.awayTeam)
        else:
            return '{} vs. {}'.format(self.homeTeam,self.awayTeam)

class Season:
    def __init__(self,teams,managers,players) -> None:
        self.teamsFile=teams
        self.managersFile=managers
        self.playersFile=players
        self.teamNameList=[]#str tutar
        self.playerList=[]
        self.playersBy5=[]
        self.managerList=[]
        self.TeamList=[]#Class instance tutar
        self.weeklyMatches=[]
        self.currentweek=1
        def createTeams():
            TeamNameFile=open(teams,'r',encoding="utf8")
            for teamName in TeamNameFile:
                self.teamNameList.append(teamName.replace('\n',''))

            PlayerFile=open(players,'r',encoding="utf8")
            for player in PlayerFile:
                playerFullname=player.replace('\n','').split(' ')
                playerName=playerFullname[0]
                playerLastName=playerFullname[1]
                self.playerList.append( Player(playerName,playerLastName)) #works for 1 space between
            Counter=0
            while Counter<len(self.playerList):
                playerbyfivesubgroup=[]
                for i in range(5):
                    playerbyfivesubgroup.append(self.playerList[Counter])
                    Counter+=1
                self.playersBy5.append(playerbyfivesubgroup)



            ManagerFile=open(managers,'r')
            for manager in ManagerFile:
                managerFullname=manager.replace('\n','').split(' ')
                managerName=managerFullname[0]
                managerLastName=managerFullname[1]
                self.managerList.append(Manager(managerName,managerLastName))


            for i in range(len(self.teamNameList)):
                self.TeamList.append(Team(self.teamNameList[i],self.managerList[i],self.playersBy5[i]))
            random.shuffle(self.TeamList)
        
            self.build_fixture()

        createTeams()

        self.seasonLength=(len(self.TeamList)-1)*2

    def reset(self):
        for team in self.TeamList:
            team.reset()
        for player in self.playerList:
            player.reset()
        for manager in self.managerList:
            manager.reset()

  
    def build_fixture(self):
        def firstHalf(teamlist):
            
            teamListh1=teamlist
            
            empytList=[]
            for i in range(len(teamListh1)):
                empytList.append(0)
            empytList[0]=teamListh1[0]
            for i in range(len(teamListh1)-1):
                matchesOfTheWeek=[]
                for k in range(int(len(teamListh1)/2)):
                    match=Match(teamListh1[k],teamListh1[k+int(len(teamListh1)/2)],i+1)
                    matchesOfTheWeek.append(match)

                self.weeklyMatches.append(matchesOfTheWeek)
                
                
                for j in range(len(teamListh1)):
                    if j==0:
                        pass
                    elif j==len(teamListh1)/2:
                        empytList[1]=teamListh1[j]
                    elif j==(len(teamListh1)/2)-1:
                        empytList[-1]=teamListh1[j]
                    elif j <=(len(teamListh1)/2)-1:
                        empytList[j+1]=teamListh1[j]
                    elif j>(len(teamListh1)/2)-1:
                        empytList[j-1]=teamListh1[j]
                teamListh1=empytList.copy()
        def secondHalf(teamlist):
            
            teamListh1=teamlist
            
            empytList=[]
            for i in range(len(teamListh1)):
                empytList.append(0)
            empytList[int(len(teamListh1)/2)]=teamListh1[int(len(teamListh1)/2)]
            for i in range(len(teamListh1)-1):
                matchesOfTheWeek=[]
                for k in range(int(len(teamListh1)/2)):
                    match=Match(teamListh1[k],teamListh1[k+int(len(teamListh1)/2)],i+1)
                    matchesOfTheWeek.append(match)

                self.weeklyMatches.append(matchesOfTheWeek)
                
                
                for j in range(len(teamListh1)):
                    if j==len(teamListh1)/2:
                        pass
                    elif j==0:
                        empytList[int(len(teamListh1)/2+1)]=teamListh1[j]
                    elif j==len(teamListh1)-1:
                        empytList[int(len(teamListh1)/2-1)]=teamListh1[j]
                    elif j <=(int(len(teamListh1)/2))-1:
                        empytList[j-1]=teamListh1[j]
                    elif j>(int(len(teamListh1)/2))-1:
                        empytList[j+1]=teamListh1[j]
                teamListh1=empytList.copy()



        RM=self.TeamList.copy()
        R1=[]
        R2=[]
        for i in range(len(RM)):
            if i <=(len(RM)/2)-1:
                R2.append(RM[i])
            else:
                R1.append(RM[i])
        
        ReversedList=[]#Asıl listenin Circle algoritmasına göre reverse edilmiş hali
        for elem in R1:
            ReversedList.append(elem)
        for elem in R2:
            ReversedList.append(elem)
        
        firstHalf(self.TeamList.copy())
        secondHalf(ReversedList)
    def get_season_length(self):
        return self.seasonLength

    def get_week_no(self):
        return self.currentweek  
    def get_week_fixture(self,week_no):
        if week_no <=0 or week_no>len(self.weeklyMatches):
            return None
        else :
            return self.weeklyMatches[week_no-1]
    def play_week(self):
        weekFixture= self.get_week_fixture(self.currentweek)
        for match in weekFixture:
            match.play()
        self.currentweek+=1
    def get_players(self):
        return self.playerList
    def get_managers(self):
        return self.managerList
    def get_teams(self):
        return self.TeamList
    def get_best_player(self):
        weekFixture= self.get_week_fixture(self.currentweek-1)# bu method play_week methodundan sonra kullanıldıgı için current week'den 1 hafta öncekini kullanmalı
        weeksPlayers=[]
        for match in weekFixture:
            for player in match.get_home_team().get_roster():
                weeksPlayers.append(player)
            for player in match.get_away_team().get_roster():
                weeksPlayers.append(player)
        
        TheOne=weeksPlayers[0]
        for player in weeksPlayers:
            if player.get_exact_week_performance(self.currentweek-1) < TheOne.get_exact_week_performance(self.currentweek-1):
                pass
            elif not player.get_exact_week_performance(self.currentweek-1) < TheOne.get_exact_week_performance(self.currentweek-1):
                TheOne=player
        return TheOne

    def get_best_manager(self):
        weekFixture= self.get_week_fixture(self.currentweek-1)# bu method play_week methodundan sonra kullanıldıgı için current week'den 1 hafta öncekini kullanmalı
        weeksManagers=[]
        for match in weekFixture:
            weeksManagers.append(match.get_home_team().get_manager())
            weeksManagers.append(match.get_away_team().get_manager())
        TheOne=weeksManagers[0]
        for manager in weeksManagers:
            if manager.get_exact_week_influence(self.currentweek-1) < TheOne.get_exact_week_influence(self.currentweek-1):
                pass
            elif not manager.get_exact_week_influence(self.currentweek-1) < TheOne.get_exact_week_influence(self.currentweek-1):
                TheOne=manager
        return TheOne
        
    def get_most_scoring_team(self):
        weekFixture= self.get_week_fixture(self.currentweek-1)# bu method play_week methodundan sonra kullanıldıgı için current week'den 1 hafta öncekini kullanmalı
        mostPoint=0
        most_scoring_team=0
        for match in weekFixture:
            matchPointHome,matchPointAway=match.get_match_score()
            if matchPointHome > matchPointAway:
                if matchPointHome > mostPoint:
                    mostPoint=matchPointHome
                    most_scoring_team=match.get_home_team()
            else:
                if matchPointAway > mostPoint:
                    mostPoint=matchPointAway
                    most_scoring_team=match.get_away_team()
        return most_scoring_team

    def get_champion(self):
        Teamlist=self.TeamList

        theChamp=Teamlist[0]
        for team in Teamlist:
            if team < theChamp:
                pass
            else:
                theChamp=team
        return theChamp

