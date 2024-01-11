import psutil

# Obtient la liste des utilisateurs actuellement connectés
users = psutil.users()

# Affiche la liste des utilisateurs
for user in users:
    print(user.name)