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

def compute_metrics():
    total_file_size = 0
    status_code_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            # Remove leading/trailing whitespaces and split the line by space
            parts = line.strip().split()

            # Check if the line matches the expected format
            if len(parts) >= 7 and parts[2] == 'GET' and parts[3].startswith('/projects/') and parts[4].startswith('HTTP/1.') and parts[5].isdigit() and parts[6].isdigit():
                file_size = int(parts[6])
                total_file_size += file_size

                status_code = int(parts[5])
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print("Total file size:", total_file_size)
                print("Number of lines by status code:")
                for status_code in sorted(status_code_counts):
                    print(f"{status_code}: {status_code_counts[status_code]}")
                print()

    except KeyboardInterrupt:
        # Print final statistics upon keyboard interruption
        print("Total file size:", total_file_size)
        print("Number of lines by status code:")
        for status_code in sorted(status_code_counts):
            print(f"{status_code}: {status_code_counts[status_code]}")
        print()

if __name__ == "__main__":
    compute_metrics()