import csv
from collections import defaultdict

def extract(filepath):
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def transform(data):
    ratings = defaultdict(list)
    for row in data:
        movie = row['movie']
        rating = float(row['rating'])
        ratings[movie].append(rating)

    return {movie: round(sum(r)/len(r), 2) for movie, r in ratings.items()}

def load(data, output_path):
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['movie', 'average_rating'])
        for movie, avg in data.items():
            writer.writerow([movie, avg])

def main():
    input_path = 'data/ratings.csv'
    output_path = 'data/average_ratings.csv'

    raw_data = extract(input_path)
    transformed_data = transform(raw_data)
    load(transformed_data, output_path)
    print(f"ETL completed. Results saved to {output_path}")

if __name__ == "__main__":
    main()
