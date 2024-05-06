#!/usr/bin/python3

# def validUTF8(data):
#     # Variable to keep track of the number of bytes remaining for the current character
#     remaining_bytes = 0

#     for byte in data:
#         # Check if the byte is a continuation byte (starts with '10')
#         if byte >> 6 == 0b10:
#             # If there are no bytes remaining, or the byte is not a valid continuation byte, return False
#             if remaining_bytes == 0:
#                 return False
#             # Decrement the count of remaining bytes
#             remaining_bytes -= 1
#         else:
#             # If there are remaining bytes, it means a new character has started before completing the previous one
#             if remaining_bytes > 0:
#                 return False

#             # Determine the number of bytes for the current character
#             if byte >> 7 == 0b0:
#                 # Single-byte character
#                 remaining_bytes = 0
#             elif byte >> 5 == 0b110:
#                 # Two-byte character
#                 remaining_bytes = 1
#             elif byte >> 4 == 0b1110:
#                 # Three-byte character
#                 remaining_bytes = 2
#             elif byte >> 3 == 0b11110:
#                 # Four-byte character
#                 remaining_bytes = 3
#             else:
#                 # Invalid starting byte
#                 return False

#     # If there are remaining bytes, it means a character is not complete
#     if remaining_bytes > 0:
#         return False

#     # All checks passed, the data represents a valid UTF-8 encoding
#     return True

from typing import Dict, Any

def validUTF8(index: int = None, page_size: int = 10) -> Dict[str, Any]:
    assert index is None or (isinstance(index, int) and index >= 0), "Index must be None or a non-negative integer."
    assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

    dataset = []  # List to store the dataset

    # Read the CSV file and populate the dataset list
    with open('your_csv_file.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        dataset = list(csv_reader)

    if index is None:
        index = 0
    else:
        assert index <= len(dataset), "Index is out of range."

    current_page = dataset[index:index + page_size]

    next_index = index + page_size

    return {
        'index': index,
        'next_index': next_index,
        'page_size': len(current_page),
        'data': current_page
    }