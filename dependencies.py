import subprocess
dependencies=['flask', 'flask_jwt_extended', 'os', 'dotenv', 'flask_sqlalchemy']

for dependency in dependencies:
    try:
        subprocess.check_call(['pip', 'install', dependency])
        print(f'Installation de {dependency} réussie.')
    except subprocess.CalledProcessError:
        print(f'Erreur lors de l\'installation de {dependency}.')

print('Toutes les dépendances ont été installées.')