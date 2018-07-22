# log_analysis_project
The log analysis project will show you the results of analysis on the database 'news' in newsdata file. The expected output is displayed in expected_outcome_in_web_browser.png. This is the part of Udacity Full Stack Web Developer NanoDegree Program.


# Running the Program
1. Install Vagrant and VirtualBox.
2. Run newsdata.py using Vagrant. 
3. Bring the virtual machine online (with ```vagrant up```). Then log into it with ```vagrant ssh```.
4. Download the files listed below and locate them in the vagrant directory, which is shared with your virtual machine(VM).
    - newsdata.py
    - newsdata.sql.zip
5. Unzip newsdata.sql.zip file and place the created sql file in the same vagrant folder as well.
6. To load the data, cd into the vagrant directory (```cd /vagrant```) and use the command ```psql -d news -f newsdata.sql``` to connect to your installed database server.
    - ```psql``` : the PostgreSQL command line program
    - ```d news``` : connect to the database named news which has been set up for you
    - ```f newsdata.sql``` : run the SQL statements in the file newsdata.sql
7. Run the command python newsdata.py and it will listen on port 8000.
8. Go to your web browser and access it at http://localhost:8000/




# Acknowldgement
Udacity - Full Stack Web Developer NanoDegree Program
