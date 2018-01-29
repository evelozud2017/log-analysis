# Logs Analysis
Logs Analysis is a reporting tool using python program that prints out reports based on the data in the database. 

# Installation
Download the files including sub-folders from [github repository] https://github.com/evelozud2017/log-analysis.

# Code
This consists of the following:
- report.py - main python code that connects, queries and prints output from data in the news database

# How to use
Run the report.py using python3 command

# How to run code
1. Prepare the data: 
- Install the Virtual machine Vagrant.  Instructions provided by [Udacity](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
- Next, [download the newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip the file after downloading.  The file inside is newsdata.sql.
- Put the newsdata.sql in the vagrant directory
- `cd` into the vagrant directory and use the command: `psql -d news -f newsdata.sql`
2. Create the view: 
- Connect to the news database: `psql -d news`
- Create the view using the sql command: `CREATE VIEW article_log_view
AS select substring(path FROM '/article/(.*)') as article, 
views
from (select path,
count(*) as views
From log
group by path) as agg_log
Where path like '/article%';`
3. Download the project from [github repository](https://github.com/evelozud2017/log-analysis).
4. From another terminal session, run vagrant using the command: `vagrant ssh`
5. Then run the report.py by using the command: `python3 report.py`

# Technologies used
- PYTHON3
- POSTGRESQL
- VAGRANT

License
----

MIT



