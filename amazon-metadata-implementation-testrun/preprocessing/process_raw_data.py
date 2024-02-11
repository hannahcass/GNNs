import pandas as pd


def process_raw_data(file_path):
    metadata = []
    with open(file_path, 'r', encoding='utf-8') as file:
        entry = {}
        in_reviews = False
        for line in file:
            line = line.strip()
            if line.startswith('Id:'):
                if entry:
                    finalize_entry(entry)
                    if entry['title']:
                        metadata.append(entry)
                entry = {'Id': int(line.split(':')[1].strip()), 'ASIN': '', 'title': '', 'group': '', 'salesrank': -1, 'similar': [], 'categories': [], 'total_reviews': 0, 'avg_rating': 0}
                in_reviews = False
            elif in_reviews:
                if line == '':
                    in_reviews = False
            elif line.startswith('ASIN:'):
                entry['ASIN'] = line.split(':')[1].strip()
            elif line.startswith('title:'):
                entry['title'] = line.split(':')[1].strip()
            elif line.startswith('group:'):
                entry['group'] = line.split(':')[1].strip()
            elif line.startswith('salesrank:'):
                entry['salesrank'] = int(line.split(':')[1].strip())
            elif line.startswith('similar:'):
                entry['similar'] = line.split(':')[1].strip().split()[1:]
            elif line.startswith('categories:'):
                cat_count = int(line.split(':')[1].strip())
                for _ in range(cat_count):
                    cat_line = next(file).strip()
                    entry['categories'].append(cat_line)
            elif line.startswith('reviews:'):
                reviews_info = line.split()
                entry['total_reviews'] = int(reviews_info[2])
                entry['avg_rating'] = float(reviews_info[-1])
        if entry and entry['title']:
            finalize_entry(entry)
            metadata.append(entry)
    return metadata


def finalize_entry(entry):
    entry['similar'] = ' '.join(entry.get('similar', []))
    entry['categories'] = ' | '.join(entry.get('categories', []))


def metadata_to_csv(metadata, output_file_path):
    df = pd.DataFrame(metadata)
    df['salesrank'] = df['salesrank'].fillna(-1).astype(int)
    column_order = ['Id', 'ASIN', 'title', 'group', 'salesrank', 'similar', 'categories', 'total_reviews', 'avg_rating']
    df = df[[col for col in column_order if col in df.columns]]
    df.to_csv(output_file_path, index=False)
    print(f"DataFrame saved as CSV file: {output_file_path}")


if __name__ == "__main__":
    #file_path = '../data/raw_2006/amazon-meta.txt'
    #output_file_path = '../data/processed_data/data.csv'
    file_path = 'data/test_data/Amazon0302.txt'
    output_file_path = '../data/test_data/test_data.csv'
    metadata = process_raw_data(file_path)
    metadata_to_csv(metadata, output_file_path)