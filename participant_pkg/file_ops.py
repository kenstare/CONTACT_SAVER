import csv
from pathlib import Path


def save_participant(filepath: Path, participant: list):
    """
    Appends a participant's details to a CSV file.
    If the file does not exist, creates it and writes a header row.
    """
    with open(filepath, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Age', 'Phone', 'Track']
        filepath.exists()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow(participant)
