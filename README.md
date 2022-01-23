# Election_Analysis
## Project Overview
A Colorado Board of Elections employee assigned the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes for each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
Data Source: election_results.csv

Software: Python 3.9.7, Visual Studio Code 1.63.2 

## Election-Audit Results:
The analysis of the election shows that there were 369,711 votes cast in the election. During the election, there was 3 candidates: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. We collected data from 3 counties: Jefferson, Denver, and Arapahoe. The total number of votes collected in all three counties was 369,711 votes. Jefferson county had 38,855 votes, which is 10.5% of the total votes. Denver county had 306,055 votes, which is 82.8% of the total votes. Lastly, Arapahoe county had 24,801 votes, which is 6.7% of the total. Therefore, the county that had the largest number of votes was Denver.

When considering the candidates, Charles Casper Stockham received a total of 85,213 votes, which is 23.0% of the total votes. Diana DeGette received a total of 272,892 votes, which is 73.8% of the total votes. Lastly, Raymon Anthony Doane received a total of 11,606 votes, which was 3.1% of the totale votes. The candidate who won the election was Diana DeGette.


## Challenge Overview
![image](https://user-images.githubusercontent.com/78320504/150664676-e5ec9630-5435-4edd-af35-0ce7555404b3.png)

![image](https://user-images.githubusercontent.com/78320504/150699835-842f22f4-7e4b-4b58-b2d4-b4043ccf233f.png)


## Election-Audit Summary:
In this project, we were tasked with reporting the total votes and number of candidates in a Colorado campaign. Therefore, I generated a vote count report to caluclate the total number of votes cast and more. With the election_results.csv, I was able to import that data and get a ist of candidates and the number of votes they each received. With those two information (total # of votes and the # of votes each candidate received), I was able to get the percentage of votes for each candidate. From that calculation, I was able to determine, using Python, which candidate was the winner of the election based on popular vote.

To election commission, this script can be used—with some modifications—for any election. One example of how the script can be modified for use in future elections, is we can look at broader data, like state votes during presidental election. We can see what majority of the votes for each state would look like. Anothe example would be modifying the script when you have more than 3 candidates. If there is more (or less), we can modify the code to see their impact of getting votes.
