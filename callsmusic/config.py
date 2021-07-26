from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', '1AgAOMTQ5LjE1NC4xNjcuNTEBuwIfrXKRq9HNU4qoHHkPt9Oj4AwYSN/0LvS1h6Fwpe5MQF4Nir8nLY8Hyl3w1CKyFKb/s1hfdPbAOcPavgl4JnWazV0oX8S1Ybh2ItuUfdwpZAvQF0QFd1N3H7o7cJlETrBw5+dyEUhUT5VxaD2fz+5GfBMIr2mJvfVHzwJ6jHMtrd/zbag9ccsllKp4dpn7FzW6yFLDHQlXzRFp1IjWPFazvsuDvPuxzWjHkwR5WP6T9SH3g9iuIVyHKrKlAfQcY8gMFkGY4gimtBk4fya1pHB45Okk1XBFsMPbusdhagsf+0i6+vHPEoyCLGQcXJTAQ2OGZ0RSAU/uuPk2zeNkD50=')
BOT_TOKEN = getenv('BOT_TOKEN', '1944925185:AAEgrCdZzo3x-QvsaoX91zm8aerQLxJRScs')
API_ID = int(getenv('API_ID', '7097917'))
API_HASH = getenv('API_HASH', 'f48294d395134512a2963d4315d21296')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '7'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1708421347').split()))
