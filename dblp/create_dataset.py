import os
import csv
import bibtexparser


def process_bib_file(file_path):
    professor_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, 'r', encoding='utf-8') as bib_file:
        bib_database = bibtexparser.load(bib_file)

    rows = []
    for entry in bib_database.entries:
        if entry['ENTRYTYPE'] == 'inproceedings':
            authors = entry.get('author', None).replace(' and\n', ';')
            venue = entry.get('booktitle', None)
            title = entry.get('title', None)
            year = entry.get('year', None)
            row = [professor_name, 'Journal', venue, title, authors, year]
            rows.append(row)
        elif entry['ENTRYTYPE'] == 'article':
            authors = entry.get('author', None).replace(' and\n', ';')
            venue = entry.get('journal', None)
            title = entry.get('title', None)
            year = entry.get('year', None)
            row = [professor_name, 'Paper', venue, title, authors.replace(' and ', ';'), year]
            rows.append(row)
    return rows


def main():
    bib_folder = 'bib'

    all_rows = []
    for file_name in os.listdir(bib_folder):
        if file_name.endswith('.bib'):
            file_path = os.path.join(bib_folder, file_name)
            professor_rows = process_bib_file(file_path)
            all_rows.extend(professor_rows)

            print(f"{file_name} finished")

    csv_columns = ["Professor", "Publication Type", "Venue", "Title", "Authors", "Year"]
    csv_file = 'dataset.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)
        writer.writerows(all_rows)

    print(f"{csv_file} created")


if __name__ == "__main__":
    main()
