#!/usr/bin/python3
import sys
import signal
import re

# Initialize counters
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regex to match the expected log format
log_pattern = re.compile(r'^\d+\.\d+\.\d+\.\d+ - \[\d+-\d+-\d+ \d+:\d+:\d+\.\d+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

def print_stats():
    """Prints the total file size and count of each status code."""
    print("File size:", total_size)
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

# Signal handler for keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Set up signal handling
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read each line from stdin
    for line in sys.stdin:
        # Match the line with the expected format
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update counters
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
