requirements:
+ mysql database v.5.7
+ python 3.6+

installation
+ run migration.sql script
+ install requirement.txt using pip install -r requirements.
+ change database connection string located at './model/db.py'

schema changes:
column: 'a_budget_percentage_notification': this column added to 't_budget' table to store the value of budget usage percentage that notification send to shop.  

run script using:
 + python main.py

description: 
this cli-application notifies shops that budget usage percentage is more than 50% or 100%, also if it exceeds than 100%, the shop goes offline. this solution avoid sending duplicated notifications.
handling budget change needs a little efforts!
