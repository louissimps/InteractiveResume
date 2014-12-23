import django
django.setup()

from db.models import Skill


with open("seed_data/SkillData.txt", 'r') as f:
    for  line in f:
        print (line)

