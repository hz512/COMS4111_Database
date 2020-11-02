-- update People
-- set birthYear = NULLIF(birthYear, "nan"), birthMonth = NULLIF(birthMonth, "nan"), birthDay = NULLIF(birthDay, "nan"),
-- birthCountry = NULLIF(birthCountry, "nan"), birthState= NULLIF(birthState, "nan"), birthCity = NULLIF(birthCity, "nan"),
-- deathYear = NULLIF(deathYear, "nan"), deathMonth = NULLIF(deathMonth, "nan"), deathDay = NULLIF(deathDay, "nan"), 
-- deathCountry = NULLIF(deathCountry, "nan"), deathState = NULLIF(deathState, "nan"), deathCity = NULLIF(deathCity, "nan"), 
-- nameFirst = NULLIF(nameFirst, "nan"), nameLast = NULLIF(nameLast, "nan"), nameGiven = NULLIF(nameGiven, "nan"),
-- weight = NULLIF(weight, "nan"), height = NULLIF(height, "nan"), bats = NULLIF(bats, "nan"),
-- throws = NULLIF(throws, "nan"), debut = NULLIF(debut, "nan"), finalGame = NULLIF(finalGame, "nan"),
-- retroID = NULLIF(retroID, "nan"), bbrefID = NULLIF(bbrefID, "nan");


-- update People
-- set birthYear = left(birthYear, 4), birthMonth = left(lpad(birthMonth, 4, "0"), 2), birthDay = left(lpad(birthDay, 4, "0"), 2),
-- deathYear = left(deathYear, 4),  deathMonth = left(lpad(deathMonth, 4, "0"), 2), deathDay = left(lpad(deathDay, 4, "0"), 2);


-- update People 
-- set isDead = "Y"
-- where deathYear is not null;

-- update People 
-- set isDead = "N"
-- where deathYear is null;

-- update People 
-- set birthDate = timestamp(concat_ws("-", birthYear, birthMonth, birthDay), "00:00:00")
-- where birthYear is not null and birthMonth is not null and birthDay is not null;

-- update People 
-- set deathDate = timestamp(concat_ws("-", deathYear, deathMonth, deathDay), "00:00:00")
-- where deathYear is not null and deathMonth is not null and deathDay is not null;
