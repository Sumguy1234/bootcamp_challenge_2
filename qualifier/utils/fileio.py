# -*- coding: utf-8 -*-
"""Helper functions to load and save general CSV data as well as a custom function for CSV data specific to the loan qualifier application. Furthermore save_csv function includes a custom header for the loan qualifier app.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
import sys
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

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask() #@DEV: Consider giving user context for how to structure directory and filename
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)   

def save_csv(qualifying_loans):
    """Ask user if they would like to save the loan data as well as where to save it.
    
    Saves loans the user qualifies for in desired directory.
    """
    questionary.confirm("Would you like to save your qualifying loan data?").ask()
    user_defined_path = questionary.text("Where would you like to save your CSV?").ask() #@DEV: Consider giving user context for how to structure directory and filename
    header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"] # @DEV: Custom header for loan qualifier app
    csvpath = Path(user_defined_path)
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        for row in qualifying_loans:
            csvwriter.writerow(row)    