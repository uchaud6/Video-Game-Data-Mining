Sole Documentation Author: Umar Chaudhry

Introduction:

Hello! This project, game_analyzing.py, is about creating functions that help to analyze a dataset about video game sales. The dataset is analyzed in csv format, and the original dataset 
can be found at "https://www.kaggle.com/sidtwr/videogames-sales-dataset?select=Video_Games_Sales_as_at_22_Dec_2016.csv". The csv file has relavent headers of 'Name, Platform, 
Year_of_Release, Genre, Global_Sales, Developer, Rating' (headers utilized in programming). Using the pandas and numpy modules, I will create five functions.

The highestsales(year) function is designed to find the highest selling game of a given year based on the given argument to the function in a form of a pandas dataframe. The highestgenres() 
function is designed to gather all the genres of the games in the dataset and place them in a dataframe with data showing how many games of each respective genre have been sold. The 
highestplatforms() function is designed to place all the platforms in the dataset into a dataframe showing how many games under each respective platform have been sold.The highestESRB() 
function is designed to place all the ESRB ratings in the dataset into a dataframe showing how many games with each respective rating have been sold. The highestdevelopers() function is 
designed to place all the developers in the dataset into a dataframe showing how many games under each respective developer have been sold (enable code in a comment of this function to get
a dataframe that only shows the top 106 developers in the dataset as opposed to the whole 1696 developers). All of these functions will return their mentioned pandas dataframes when called.


Files Needed:

game_analyzing.py - Main program file with five functions for data analysis

videogames.csv - Video game data file that is analyzed by project4.py


Insights from Data:

The highest selling games of the latest six years of the dataset have all fit under one of the the top three most successful genres with those being action, sports, and shooter games. This 
may hint that producing a game that fits under one of these three categories will give it a more likely chance to be successful. However, I feel that this data covering genres is too 
unreliable to make big claims since the highest selling action genre has around 1,745,269,000 games sold under its name, but the genre of 'action' can be applied to a game very easily with 
concepts of other genres like shooting, fighting, etc. being named under a very broad term as "action", which would explain why the action genre is ahead with sales. Some evidence to 
back my claim would be how 'action' is mentioned 3401 times while other genres aren't mentioned half as much as that in 'videogames.csv' (using ctrl F). For example, 'shooter' is only 
mentioned 1326 times.

The goal for seeing which consoles sold the most games was to see if the public was more likely to buy games on specific types of consoles. Of the ten consoles that sold the most games,
half of the consoles were from Sony's Playstation models, a third of the consoles were from Nintendo's products, Microsoft's Xbox 360 made the list, and PC gaming made the list as the 
tenth console with the most sold games. Therefore, Sony's Playstation models would seem to have the best success rate to sell games based on how many of their consoles have done so before.
It's impressive for PC systems to make the top ten consoles in this list as PC gaming is relatively new compared to tradtional console gaming, especially at the time of this dataset's 
completition of the year 2016, so this data shows how PC gaming has been on the rise.

The goal for seeing which games sold the most copies based on their ESRB ratings was to see if the public bought games for a specific age demographic. However, a large portion of games in
the dataset didn't actually have an ESRB rating, and while games rated E had the most games sold with around 2,851,000,000 games, rated T games and rated M games had much less but very
similar amount of games sold. Despite the rated E games having a larger amount of games sold, I believe there is no direct correlation with ESRB ratings and game sales as there are
many more rated E games in the market, and rated T and M games had very similar games sold. Meaning, at the very least, there isn't a linear correlation with how ESRB ratings sell copies
since the ratings of T for teen and M for mature have similar data.

The goal for seeing which ten developers have helped to sell the most games was just to show the developers who've had the most success in producing high-selling games. Of the highest
selling games in the latest six years of the dataset, three of the developers listed in highestdevelopers() worked on all but one of those games, with those devleopers being Treyarch,
Rockstar North,and EA Sports. This knowledge could be used to examine the tactics and design approach these companies use to be very successful in producing high-selling video games.


Data Summaries/Function Output Summaries:

	highestsales(latest 6 years) produced:

FIFA 17 was the best global selling game of 2016 with 7.59 million copies sold. - PS4 console
Call of Duty: Black Ops 3 was the best global selling game of 2015 with 14.63 million copies sold - PS4 console
Grand Theft Auto V was the best global selling game of 2014 with 12.61 million copies sold. - PS4 console
Grand Theft Auto V was the best global selling game of 2013 with 21.04 million copies sold - PS3 console
Call of Duty: Black Ops II was the best global selling game of 2012 with 13.79 million copies sold. - PS3 console
Call of Duty: Modern Warfare 3 was the best global selling game of 2011 with 14.73 million copies sold. - Xbox 360 console

	highestgenres() produced:

Action games have 1745.2699999999693 million games sold
Sports games have 1331.9999999999861 million games sold
Shooter games have 1052.9399999999764 million games sold
Role-Playing games have 934.3999999999937 million games sold
Platform games have 828.0799999999966 million games sold
Misc games have 803.1799999999942 million games sold
Racing games have 728.8999999999947 million games sold
Fighting games have 447.47999999999917 million games sold
Simulation games have 390.4199999999976 million games sold
Puzzle games have 243.02000000000064 million games sold
Adventure games have 237.69000000000122 million games sold
Strategy games have 174.50000000000057 million games sold


	highestplatforms() produced:

The PS2 console has sold 1255.6399999999871 million games 
The X360 console has sold 971.6299999999992 million games 
The PS3 console has sold 939.4299999999982 million games 
The Wii console has sold 908.129999999998 million games 
The DS console has sold 807.0999999999868 million games 
The PS console has sold 730.679999999997 million games 
The GBA console has sold 318.499999999998 million games 
The PS4 console has sold 314.22999999999905 million games 
The PSP console has sold 294.2999999999953 million games 
The PC console has sold 260.29999999999643 million games 
The 3DS console has sold 259.0899999999991 million games
The XB console has sold 258.25999999999834 million games
The GB console has sold 255.44999999999987 million games
The NES console has sold 251.06999999999988 million games
The N64 console has sold 218.87999999999985 million games
The SNES console has sold 200.05000000000024 million games
The GC console has sold 199.3600000000007 million games
The XOne console has sold 159.44000000000003 million games
The 2600 console has sold 97.08000000000003 million games
The WiiU console has sold 82.16000000000003 million games
The PSV console has sold 54.12000000000018 million games
The SAT console has sold 33.59000000000002 million games
The GEN console has sold 30.780000000000005 million games
The DC console has sold 15.969999999999997 million games
The SCD console has sold 1.8700000000000003 million games
The NG console has sold 1.4400000000000004 million games
The WS console has sold 1.42 million games
The TG16 console has sold 0.16 million games
The 3DO console has sold 0.1 million games
The GG console has sold 0.04 million games
The PCFX console has sold 0.03 million games

	highestESRB() produced:

2436.900000000087 million games with the ESRB rating of E have been sold.
1494.3999999999687 million games with the ESRB rating of T have been sold.
1473.8399999999926 million games with the ESRB rating of M have been sold.
655.8099999999987 million games with the ESRB rating of E10+ have been sold.
4.33 million games with the ESRB rating of K-A have been sold.
1.95 million games with the ESRB rating of AO have been sold.
1.7800000000000002 million games with the ESRB rating of EC have been sold.
0.08 million games with the ESRB rating of RP have been sold.

	highestdeveloper() produced:

The developing company Nintendo has sold 531.7100000000002 million games.
The developing company EA Sports has sold 175.38000000000002 million games.
The developing company EA Canada has sold 142.32000000000005 million games.
The developing company Ubisoft has sold 132.54000000000028 million games.
The developing company Rockstar North has sold 119.47 million games.
The developing company Capcom has sold 115.70999999999995 million games.
The developing company Ubisoft Montreal has sold 108.31000000000002 million games.
The developing company Treyarch has sold 103.16 million games.
The developing company EA Tiburon has sold 96.12000000000003 million games.

Thank you for reading!
Footer
?? 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
