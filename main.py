import json
import selenium
import os

# main.py will use login() and send_reel() functions of utility.py to login and send_reel()
# main.py will hold account data and select the reel to be posted
# After a reel is sent, the reel's name should be appended with letter S as in Sent.
# each account should have a folder named after its name. Folders should contain reels to be sent. Reels should have a number in them to show its order of postage(?)
# If a reel's name ends with a capital S, it shouldn't be sent.
# If there isn't a folder for an account. main.py should create it and notify the user.

with open("accounts.json","r") as accounts:
    accounts = json.load(accounts) 



