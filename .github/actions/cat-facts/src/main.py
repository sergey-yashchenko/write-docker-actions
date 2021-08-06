import requests
import random
import sys


# Create an empty list to store individual facts in
# This will make it easy to select a random one later
fact_list = []

random_fact = "cat is not a dog"

# Print the individual randomly returned cat-fact
print(random_fact)

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{random_fact}")
