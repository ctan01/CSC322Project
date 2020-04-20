# Database
# Should have the following tables:
# USER TABLE
## with userID, username, user email, user password, user skills, user interests, user groups
# GROUPS TABLE
## groupID, groupname, group members
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

# tricky thing here is that each of us will have to download mySQL and input our own specific host and user pass
