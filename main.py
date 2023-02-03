"""
Run this file to run the application :)
"""
import utils
import controller

config = utils.load_config("config.json")

database = utils.db_connect(config["database"]["dsn"])

SHOULD_EXIT = False
while not SHOULD_EXIT:
    SHOULD_EXIT = controller.run(database)
