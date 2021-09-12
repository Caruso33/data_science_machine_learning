# Relational Data Modeling Project

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Data

The project is based on two datasets, the [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/) and [Event simulator log files](https://github.com/Interana/eventsim).

## Modeling

Schema for Song Play Analysis

Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

### Fact Table

`songplays` - records in log data associated with song plays i.e. records with page NextSong

- songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables

`users` - users in the app

- user_id, first_name, last_name, gender, level

`songs` - songs in music database

- song_id, title, artist_id, year, duration

`artists` - artists in music database

- artist_id, name, location, latitude, longitude

`time` - timestamps of records in songplays broken down into specific units

- start_time, hour, day, week, month, year, weekday

## Projects files

`test.ipynb` displays the first few rows of each table to let you check your database.

`create_tables.py` drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.

`etl.ipynb` reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.

`etl.py` reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.

`sql_queries.py` contains all your sql queries, and is imported into the last three files above.

`README.md` provides discussion on your project.

## How to run

`python create_tables.py` is creating tables. Then `python etl.py` will run the pipeline.
The `etl.ipynb` is a more visual representation of `etl.py` with same content and functionality. Both files use `sql_queries.py` under the hood to perform sql commands against the postgresql database.

## Design

The modeling of relational tables based on the star or snowflake schema doesn't follow the 3NF normalization process. It provides good denormalization advantages though as well as simplifying queries and allowing for fast aggregations.

The star schema doesn't allow for many-to-many relations - snowflake does. Both have schemas have to deal with the drawbacks of denormalization, namely decreased query flexibility and data integrity issues.

## When to use a relational database

Advantages of Using a Relational Database

- Flexibility for writing in SQL queries: With SQL being the most common database query language.

- Modeling the data not modeling queries

- Ability to do JOINS

- Ability to do aggregations and analytics

- Secondary Indexes available : You have the advantage of being able to add another index to help with quick searching.

- Smaller data volumes: If you have a smaller data volume (and not big data) you can use a relational database for its simplicity.

- ACID Transactions: Allows you to meet a set of properties of database transactions intended to guarantee validity even in the event of errors, power failures, and thus maintain data integrity.

- Easier to change to business requirements

## When **NOT** to use a relational database

- Have large amounts of data: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. You are limited by how much you can scale and how much data you can store on one machine. You cannot add more machines like you can in NoSQL databases.

- Need to be able to store different data type formats: Relational databases are not designed to handle unstructured data.

- Need high throughput -- fast reads: While ACID transactions bring benefits, they also slow down the process of reading and writing data. If you need very fast reads and writes, using a relational database may not suit your needs.

- Need a flexible schema: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.

- Need high availability: The fact that relational databases are not distributed (and even when they are, they have a coordinator/worker architecture), they have a single point of failure. When that database goes down, a fail-over to a backup system occurs and takes time.

- Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data.
