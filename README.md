# Data Engineering Toolkit
This is a collection of python scripts that can make your data engineering tasks easier. This project also helps beginners practice **Git/GitHub workflows** (branching, pull requests, code reviews)

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Project Setup](#project-setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)


## Project Overview
This repository contains is a set of basic python scripts that can make your data engineering tasks easier. This is also a  practice project for learning version control and collaboration with Git and GitHub.

## Key Features
- Data Cleaning Script
- Data Transformation Script
- Data Loading Script

## Tools and Technologies Used
- Python: This was used to write the scripts.
- Git: This was used for version control and collaboration.
- GitHub: This was used for documenting the scripts.

## Project Setup
### Prerequisites
- Python **3.8+** installed on your system  
- Git installed and configured  
- A sample CSV dataset (for testing the scripts)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/data-engineering-toolkit.git
   cd data-engineering-toolkit
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How It Works
1. Data Cleaning Script
- Automates removal of missing values, duplicates, or unwanted characters.
- Saves a cleaned dataset into /output.

2. Data Transformation Script
- Applies transformations like renaming columns, type casting, or feature engineering.
- Outputs a processed dataset.

3. Data Loading Script
- Saves transformed data into different formats (CSV, JSON, or database).
- Prepares data for downstream analytics or ML.

## Usage
Run any script individually:
```bash
scripts/data_cleaning.py
scripts/data_transformation.py
scripts/data_loading.py
```

## Future Enhancements
- Add advanced scripts for more complex data engineering tasks.
- Build an end to end ETL pipeline.

# Author: Chelsea Adetan
