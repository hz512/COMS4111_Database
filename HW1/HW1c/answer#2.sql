-- update Batting
-- set playerID = NULLIF(playerID, "nan"), yearID = NULLIF(yearID, "nan"), stint = NULLIF(stint, "nan"),
-- teamID = NULLIF(teamID, "nan"), lgID = NULLIF(lgID, "nan"), G = NULLIF(G, "nan"),
-- AB = NULLIF(AB, "nan"), R = NULLIF(R, "nan"), H = NULLIF(H, "nan"), 
-- 2B = NULLIF(2B, "nan"), 3B = NULLIF(3B, "nan"), HR = NULLIF(HR, "nan"), 
-- RBI = NULLIF(RBI, "nan"), SB = NULLIF(SB, "nan"), CS = NULLIF(CS, "nan"),
-- BB = NULLIF(BB, "nan"), SO = NULLIF(SO, "nan"), IBB = NULLIF(IBB, "nan"),
-- HBP = NULLIF(HBP, "nan"), SH = NULLIF(SH, "nan"), SF = NULLIF(SF, "nan"),
-- GIDP = NULLIF(GIDP, "nan");

-- select People.playerID, People.nameFirst, People.nameLast, 
-- tmp.no_of_awards from People join (SELECT cast(playerID as varchar(15)) as casted_pID, 
-- count(*) as no_of_awards from AwardsPlayers group by playerID) as tmp 
-- using playerID;


select People.playerID, People.nameFirst, People.nameLast, award_table.awards, app.gamesPlayed, hrs.homeRuns from People 
join (select playerID, count(*) as awards from AwardsPlayers group by playerID) as award_table 
join (select playerID, sum(G_all) as gamesPlayed from Appearances group by PlayerID) as app
join (select playerID, sum(HR) as homeRuns from Batting group by playerID) as hrs
on People.playerID = award_table.playerID and award_table .playerID = app.playerID and app.playerID = hrs.playerID
group by playerID
order by award_table.awards desc;
