**Sparkify ETL with Postgres and Python(psycopg2)**

In this project, a data model was build within Postgres and the database implemented and an ETL pipeline created using Python.

This process followed these steps:

- Data modeling in Postgres star schema (fact and associated dimension tables) ( <https://en.wikipedia.org/wiki/Star_schema> ).athon. 
- ETL pipeline for loading data using Python. 

**Project Description**

This project is to create a SQL analytics database for a music streaming startup called Sparkify. Sparkify's analytics team wants to understand what songs users are listening on the company's music app. They need an easy way to query this user data. This data is stored as JSON logs on user activity JSON on Song play (user activity + song play).

**Project Dataset**

- **Song Dataset**: files are partitioned by the first three letters of each song's track ID e.g. */data/song\_data.*.json. Sample:

{"artist\_id": "ARD7TVE1187B99BFB1", "artist\_latitude": null, "artist\_location": "California - LA", "artist\_longitude": null, "artist\_name": "Casual", "duration": 218.93179, "num\_songs": 1, "song\_id": "SOMZWCG12A8C13C480", "title": "I Didn't Mean To", "year": 0}

- **Log Dataset**: files in the dataset you'll be working with are partitioned by year and month e.g. \*/data/log\_data.\*json. Sample:

{"artist": "Stephen Lynch", "auth": "Logged In", "firstName": "Jayden", "gender": "M", "itemInSession": 0, "lastName": "Bell", "length": 182.85669, "level": "free", "location": "Dallas-Fort Worth-Arlington", "method": "TX PUT", "page": "NextSong", "registration": 1.540992.., "sessionId": "829", "song":"Jim Henson's Dead", "status": 200, "ts": 1543537327796, "userAgent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT...", "userId": 91}

**Data Modeling**

This project uses a Star Schema: one fact table consist of the measures associated with each event songplays, and referencing four dimensional tables *songs*, *artists*, *users* and *time*, each with a primary key that is being referenced from the fact table

Given the requirements of the project this was the most logical approach as load considerations are not given as a factor.

**Project template (taken from project instructions)**

“The data files, the project includes six files:

1. test.ipynb displays the first few rows of each table to let you check your database.
2. create\_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3. etl.ipynb reads and processes a single file from song\_data and log\_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. etl.py reads and processes files from song\_data and log\_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5. sql\_queries.py contains all your sql queries, and is imported into the last three files above.
6. README.md provides discussion on your project.”

**How to Run**

1. Run ***create\_tables.py*** (console)to create the database and tables.
1. Run ***etl.py*** (console) to process loading, extracting and inserting of data.
1. Run ***test.ipynb*** (Juypternotebook) to confirm the creation of database and columns.



