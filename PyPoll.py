# PyPoll.py
# #path to Csv
# Resources/election_results.csv
# Import the datetime class from the datetime module.
import datetime as dt
import os
import csv
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Import the datetime class from the datetime module.
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     print(election_data)

dir(os.path)
dir(os.path.join("Resources", "election_results.csv"))
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    # print(election_data)
  # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)

# # Add our dependencies.
# import csv
# import os 
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Open the election results and read the file.
# with open(file_to_load, "a") as election_data:
#     file_reader = csv.reader(election_data)
# # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)





# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote