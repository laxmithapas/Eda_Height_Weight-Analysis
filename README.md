# Exploratory Data Analysis (EDA) - Height and Weight Dataset

This project is focused on performing *Exploratory Data Analysis (EDA)* on a dataset containing *Height (in inches)* and *Weight (in pounds)* of individuals. The main objective of this project is to clean the data, perform basic statistical analysis, and visualize the distribution of the data.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Data Source](#data-source)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Analysis and Results](#analysis-and-results)
7. [Conclusion](#conclusion)

## Project Overview

The dataset consists of *200 data points* including two features: *Height* and *Weight*. This project demonstrates the basic steps of data cleaning, visualization, and analysis.

- *Data Cleaning*: Columns are cleaned to remove any extra spaces and symbols for easy processing.
- *Statistical Analysis*: Basic summary statistics like mean, median, standard deviation, etc., are calculated.
- *Visualizations*: 
  - Distribution of Height (in inches) and Weight (in pounds) using histograms.
  - Scatter plot to explore the relationship between Height and Weight.

## Technologies Used

- *Python*: Programming language for analysis and visualization.
- *Pandas*: Data manipulation and cleaning.
- *Matplotlib*: Plotting library for generating graphs.
- *Seaborn*: Statistical data visualization.

## Data Source

This dataset is a sample data of *height* and *weight* measurements.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/eda-project.git
   cd eda-project

2. Create and activate a virtual environment (optional but recommended):

python -m venv .venv
.\.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Mac/Linux


3. Install required packages:

pip install -r requirements.txt


4. You can install the required packages manually:

pip install pandas matplotlib seaborn



Usage

1. Place the dataset (data.csv) in the project directory.


2. Run the main.py script:

python main.py



This will:

Load the data.

Clean the data by renaming columns and handling missing values.

Perform statistical analysis.

Generate and display visualizations (Histograms and Scatter Plot).


Analysis and Results

The analysis includes:

1. Summary Statistics: Key statistics like mean, median, and standard deviation for Height and Weight.


2. Histograms:

Distribution of Height (in inches).

Distribution of Weight (in pounds).



3. Scatter Plot: A plot showing the relationship between Height (in inches) and Weight (in pounds).



Conclusion

The Exploratory Data Analysis (EDA) for this dataset provides basic insights into the distribution and relationship between Height and Weight. The visualizations highlight the data's spread, central tendency, and the correlation between the two features.


