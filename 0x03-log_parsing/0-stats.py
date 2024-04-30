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

status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
lines = []
total_size = 0
status_count = {code: 0 for code in status_codes}

try:
    for line in sys.stdin:
        line = line.strip()

        # Parse the line and extract relevant information
        parts = line.split()
        if len(parts) < 7:
            continue

        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        lines.append(line)
        total_size += file_size
        if status_code in status_codes:
            status_count[status_code] += 1

        # Print statistics every 10 lines
        if len(lines) == 10:
            print("Total file size:", total_size)
            for code in sorted(status_count.keys()):
                if status_count[code] > 0:
                    print(f"{code}: {status_count[code]}")
            print()
            lines = []

except KeyboardInterrupt:
    # Print statistics on keyboard interruption
    print("Total file size:", total_size)
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")