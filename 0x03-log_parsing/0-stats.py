#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


# import sys

# status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
# line_count = 0
# total_file_size = 0
# status_code_counts = {code: 0 for code in status_codes}

# try:
#     for line in sys.stdin:
#         line = line.strip()
        
#         # Skip lines that don't match the expected format
#         if not line.startswith('"GET /projects/260 HTTP/1.1"'):
#             continue
        
#         # Extract the status code and file size
#         parts = line.split(' ')
#         status_code = parts[-2]
#         file_size = int(parts[-1])
        
#         # Update metrics
#         total_file_size += file_size
#         status_code_counts[status_code] += 1
        
#         line_count += 1
        
#         # Print statistics after every 10 lines
#         if line_count % 10 == 0:
#             print(f"Total file size: {total_file_size}")
#             for code in sorted(status_codes):
#                 if status_code_counts[code] > 0:
#                     print(f"{code}: {status_code_counts[code]}")
#             print()
# except KeyboardInterrupt:
#     pass

# # Print final statistics
# print(f"Total file size: {total_file_size}")
# for code in sorted(status_codes):
#     if status_code_counts[code] > 0:
#         print(f"{code}: {status_code_counts[code]}")

import sys

def print_statistics(total_file_size, status_code_counts):
    print("Total file size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        print(f"{status_code}: {count}")

def process_input():
    total_file_size = 0
    status_code_counts = {}

    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()

            # Parse the line and extract the relevant information
            parts = line.split()
            if len(parts) < 7:
                continue
            ip_address = parts[0]
            status_code = parts[-3]
            file_size = int(parts[-2])

            # Update the total file size
            total_file_size += file_size

            # Update the status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)

# Start processing the input
process_input()