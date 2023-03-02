# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, data):
    file_path_save = Path("qualifying_loans.csv")
    with open (file = file_path_save, mode = 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        for info in data:
            csvwriter.writerow(info)
        
    return f"The qualifying loans have been saved to 'qualifying_loans.csv'."
 