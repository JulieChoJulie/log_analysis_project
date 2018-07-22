# Log Analysis Project
>The log analysis project will show you the results of analysis on the database 'news' in newsdata file. The expected output is displayed in expected_outcome_in_web_browser.png. This is the part of Udacity Full Stack Web Developer NanoDegree Program.

# Purpose of this project
>In this project, I stretched SQL database skills. I built and refined complex queries and use them to draw business conclusions from data.

# You need to install the following below : 
- [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [the VM configuration](https://github.com/udacity/fullstack-nanodegree-vm)
- [Python3](https://www.python.org/getit/)

# Running the Program
1. Inside the vagrant subdirectory, run the command ```vagrant up```.
2. When ```vagrant up``` is finished running, you will get your shell prompt back. At this point, you can run ```vagrant ssh``` to log in to your newly installed Linux VM.
4. Download the files listed below and locate them in the vagrant directory, which is shared with your virtual machine(VM).
    - newsdata.py
    - newsdata.sql that you can download from unzipping newsdata.sql.zip.
5. To load the data, cd into the vagrant directory (```cd /vagrant```) and use the command ```psql -d news -f newsdata.sql``` to connect to your installed database server.
    - ```psql``` : the PostgreSQL command line program
    - ```d news``` : connect to the database named news which has been set up for you
    - ```f newsdata.sql``` : run the SQL statements in the file newsdata.sql
    
   The database 'news' has 3 tables.
    * authors 
    * articles
    * log   
6. Use ```psql -d news``` to connect to the database.
7. Create view using the command below.
    ```
    create view log_ok as select id, substring(path, 10) as path_sliced from log where method = 'GET' and status = '200 OK' and path != '/';
    ```
8. Execute the command ```contorl + D```.
9. Run the command ```python newsdata.py``` and it will listen on port 8000.
10. Go to your web browser and access it at http://localhost:8000/

# Possible Errors
If this command gives an error message, such as —
```psql: FATAL: database "news" does not exist```
```psql: could not connect to server: Connection refused```
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration. To continue, download the virtual machine configuration into a fresh new directory and start it from there.

# Acknowldgement
Udacity - Full Stack Web Developer NanoDegree Program
