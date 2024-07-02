# Data-Visualization-using-Python-SQL-and-Power-BI Overview

## Introduction
ETL stands for **Extract, Transform, and Load**. It is a crucial process in data warehousing that involves three distinct steps:

- **Extract:** In this step, data is gathered from one or more sources. For my project, I have chosen to use a public dataset from Kaggle, provided in the form of a CSV file.
  
- **Transform:** The extracted data then undergoes various manipulations. These manipulations can include cleaning, filtering, validating, and aggregating data.
  
- **Load:** The final step involves loading the transformed data into a target system, which is often a data warehouse, database, or data lake.

## Project Structure
This project is organized into three main folders, each serving a specific purpose:

1. **Extract & Transform:** Contains a Python script responsible for extracting and transforming the data from a single large CSV file to several smaller CSV files, each representing a table of the SQL database to be created.

2. **Database:** Focuses on SQL database creation and loading the transformed data into the database.

3. **Dashboard:** Includes a copy of the dashboard created to analyze the cleaned and organized data.

Each folder contains an additional README.md file with detailed explanations and instructions for setting up and running the project on your local machine.

## Getting Started
To start, download the whole project and locate it in your files. In the database folder, delete every CSV file before starting (they will be recreated by the extract and transform script in the first folder), be sure to create a new folder for the project and move everything to it, then open this project folder in VS Code or your preferred code editor and follow the instructions provided in the respective README file in each of the folders.

## Dataset Source
- **Kaggle Dataset:** [Superstore Sales Dataset](https://www.kaggle.com/datasets/ishanshrivastava28/superstore-sales)

This is the dataset used in the project. It contains sales data from a fictional superstore.
