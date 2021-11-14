# Election_Analysis
---

## Overview ##
	This project was intended to count the number of votes cast in an election. 
	The code then determined how many votes each candidate won and the voter turnout of each county. 
	The results are then saved to a printable text file and stated in the computer terminal. 

### Results ### 

	369,711 votes were cast in total.
	Each county contributed the following percentage and number of votes:
---
	Jefferson: 10.5% (38,855)
	Denver: 82.8% (306,055)
	Arapahoe: 6.7% (24,801)
---
	Charles Casper Stockham received 85,213 votes and 23% of the total votes. 
	Raymon Anthony Doane received 11,606 votes and 3.1% of the total votes. 
	The winner, Diana DeGette, received 272,892 votes and 73.8% of the total votes. 
---

### Additional Notes ###

	The code used to generate these results can easily be modified for other elections. 
	The "file_to_load" variable on line 7 can be altered to represent a different path to 
	a data file of election results. Afterwards the row numbers, [2] and [1] that represent 
	the candidate names and county names on lines 32 and 33 respectively, would need to be 
	updated to accurately reflect its counterpart data in a different data set.

	This code could also count votes by other geographic parameters like state, or city. 
	However the variable names and printed texts should then be changed in order to avoid confusion. 

![image](https://user-images.githubusercontent.com/91698325/141662480-d6ab4429-c99b-45d8-9f6f-a8fdbd20d9a7.png)

