# error_script.py
import sys

# Print a message to standard error
sys.stderr.write("Oh no! Something went wrong!\n")

# Exit with a non-zero status code (e.g., 1) to indicate an error
sys.exit(1)

