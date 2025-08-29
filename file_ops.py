from pathlib import Path
import csv

def save_participant(path, participant_dict):
    """
    Appends participant details to a CSV file.
    If the file does not exist, creates it and writes a header row.
    """
    path = Path(path)
    file_exists = path.exists()
    with path.open('a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Age', 'Phone', 'Track']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(participant_dict)

def load_participants(path):
    """
    Reads all participants from the CSV and returns them as a list of dictionaries.
    """
    path = Path(path)
    participants = []
    if path.exists():
        with path.open('r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                participants.append(row)
    return participants 