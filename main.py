# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
# print(add_time("11:06 PM", "2:02"))
# print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)