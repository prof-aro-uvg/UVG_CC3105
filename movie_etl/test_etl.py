import pytest
from etl import extract, transform, load
import os

def test_transform():
    sample_data = [
        {'movie': 'Inception', 'rating': '5'},
        {'movie': 'Inception', 'rating': '4'},
        {'movie': 'Interstellar', 'rating': '5'}
    ]
    result = transform(sample_data)
    assert result == {'Inception': 4.5, 'Interstellar': 5.0}

def test_load(tmp_path):
    data = {'Inception': 4.5, 'Interstellar': 5.0}
    output_file = tmp_path / "output.csv"
    load(data, output_file)

    with open(output_file) as f:
        lines = f.readlines()
        assert lines[0].strip() == "movie,average_rating"
        assert "Inception,4.5" in lines[1] or lines[2]
