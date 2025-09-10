# Contenu de app.py
import time
import redis
from flask import Flask

app = Flask(__name__)
# On se connecte au service 'redis' sur le port par défaut.
# Docker Compose va s'assurer que l'hostname 'redis' pointe vers le bon conteneur !
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            # On incrémente de 1 la valeur de la clé 'hits' et on la retourne
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Bonjour ! Vous êtes le visiteur numéro {count}.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
