from Priconne.main import Priconne
from config import CONFIG
import os
my_secret = os.environ['TOKEN']

priconne = Priconne(CONFIG)
priconne.run(CONFIG["my_secret"])

