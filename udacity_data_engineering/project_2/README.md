# Non-Relational Data Modeling Project

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

## Project Description

In this project, you'll apply what you've learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python. To complete the project, you will need to model your data by creating tables in Apache Cassandra to run queries. You are provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

We have provided you with a project template that takes care of all the imports and provides a structure for ETL pipeline you'd need to process this data.

## Data

The project uses `event_data` and creates an intermediary `event_datafile_new.csv`.

## Modeling

Apache Cassandra tables have to be created according to the queries one wants to perform on them.
Please see the `ipynb` file for the implementation.

## Project files

`Project.ipynb` contains all implementation.

`event_datafile_new.csv` was created by processing the original `event_data`-files.

`README.md` provides discussion on your project.

## How to run

Use jupyter to run `Project.ipynb`.

## When to use a NoSQL Database

- Need to be able to store different data type formats: NoSQL was also created to handle different data configurations: structured, semi-structured, and unstructured data. JSON, XML documents can all be handled easily with NoSQL.

- Large amounts of data: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. NoSQL databases were created to be able to be horizontally scalable. The more servers/systems you add to the database the more data that can be hosted with high availability and low latency (fast reads and writes).
- Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data

- Need high throughput: While ACID transactions bring benefits they also slow down the process of reading and writing data. If you need very fast reads and writes using a relational database may not suit your needs.

- Need a flexible schema: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.

- Need high availability: Relational databases have a single point of failure. When that database goes down, a failover to a backup system must happen and takes time.

## When NOT to use a NoSQL Database?

- When you have a small dataset: NoSQL databases were made for big datasets not small datasets and while it works it wasn’t created for that.

- When you need ACID Transactions: If you need a consistent database with ACID transactions, then most NoSQL databases will not be able to serve this need. NoSQL database are eventually consistent and do not provide ACID transactions. However, there are exceptions to it. Some non-relational databases like MongoDB can support ACID transactions.

- When you need the ability to do JOINS across tables: NoSQL does not allow the ability to do JOINS. This is not allowed as this will result in full table scans.

- If you want to be able to do aggregations and analytics

- If you have changing business requirements : Ad-hoc queries are possible but difficult as the data model was done to fix particular queries

- If your queries are not available and you need the flexibility : You need your queries in advance. If those are not available or you will need to be able to have flexibility on how you query your data you might need to stick with a relational database
