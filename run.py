from Priconne.main import Priconne
from config import CONFIG
import os
from keep_alive import keep_alive
my_secret = os.environ['TOKEN']

priconne = Priconne(CONFIG)
priconne.run(CONFIG["my_secret"])
keep_alive()
