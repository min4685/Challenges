from datetime import datetime
import os

SECRET_KEY = os.urandom(36).hex()

P1_SECRET_CLUE = "Ready or not, here I come!"

today = datetime.now().strftime('%Y-%m-%d')
P2_SECRET_CLUE = today

P3_SECRET_CLUE = "g334fg2"

P1_SECRET_KEY = "Peek-a-boo!"
P2_SECRET_KEY = "A-head of time"
P3_SECRET_KEY = "I spy with my little eye something..."