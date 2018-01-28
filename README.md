# Logs Analysis
Logs Analysis is a reporting tool using python program that prints out reports based on the data in the database. 

# Installation
Download the files including sub-folders from [github repository] https://github.com/evelozud2017/log-analysis.

# Code
This consists of the following:
- report.py - main python code that connects, queries and prints output from data in the news database
- output.txt - sample output file

# How to use
Run the report.py using python3 command

# How to run code
1. Download the project from [github repository] https://github.com/evelozud2017/log-analysis.
2. Create the news database
3. Connect to news database and create the view using this command: 
    CREATE VIEW article_log_view
    AS select id, substring(path FROM '/article/(.*)') as article, 
    time, status from log where path like '/article%';
4. From another terminal session, run vagrant using the command: vagrant ssh
5. Then run the report.py by using the command: python3 report.py

# Technologies used
- PYTHON3
- POSTGRESQL
- VAGRANT

License
----

MIT



