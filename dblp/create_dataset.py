import os
import csv
import xml.etree.ElementTree as ET
import re


def get_publication_type(pub_element):
    if 'publtype' in pub_element.attrib:
        return 'Informal or Other Publication'
    else:
        if pub_element.find('journal') is not None:
            return 'Journal Article'
        elif pub_element.find('booktitle') is not None:
            return 'Conference or Workshop Paper'
        else:
            return 'Informal or Other Publication'


def extract_data_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    professor_name = root.attrib['name']
    professor_name = re.sub(r'\d+$', '', professor_name).strip()

    publications = []

    for article in root.findall('.//r/*'):
        if article.tag == 'article' or article.tag == 'inproceedings':
            publication_type = get_publication_type(article)
            venue = article.find('journal')
            if venue is None:
                venue = article.find('booktitle')
            if venue is None:
                venue = ''
            else:
                venue = venue.text

            title = article.find('title').text if article.find('title') is not None else ''
            authors = [re.sub(r'\d+$', '', author.text).strip() for author in article.findall('author')]
            authors = ';'.join(authors)
            year = article.find('year').text if article.find('year') is not None else ''

            publications.append({
                'Professor': professor_name,
                'Publication Type': publication_type,
                'Venue': venue,
                'Title': title,
                'Authors': authors,
                'Year': year
            })

    return publications, professor_name


def save_to_csv(data, filename):
    keys = data[0].keys() if data else []
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def create_dataset_from_xml_folder(xml_folder, output_filename):
    all_publications = []

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_file)
            publications, professor_name = extract_data_from_xml(xml_path)
            all_publications.extend(publications)
            print(f"Finished processing '{professor_name}' publications")

    save_to_csv(all_publications, output_filename)


def main():
    xml_folder_path = 'xml'
    output_csv_filename = 'dataset.csv'
    create_dataset_from_xml_folder(xml_folder_path, output_csv_filename)


if __name__ == "__main__":
    main()
