import random
when=["Yesterday", "A few hours ago", "Earlier", "A long time ago", "Once"]
who=["the barber", "the neighbour", "my best friend", "my cousin-brother", "my dog"]
name=["Bob", "Zak", "Nemin", "Aangad", "Harry", "Mark", "Leo", "Samir", "Anastasios"]
residence=["Colnbrook", "Wales", "Antartica", "South Africa", "North America"]
went=["Cinema", "mall", "shops", "home", "beach", "bowling", "high street"]
happened=["bought chocolates", "ate burger and fries", "went bowling", "won a football match"]
print(random.choice(when)+','+random.choice(who)
+' that lived in '+random.choice(residence)+',went to '
+random.choice(went)+' and '
+random.choice(happened))