import utilities as f
from flask import jsonify

#Importación de la información de los heroes
data = f.load_file('./heroes.csv')

def list_heroes(request):
    """La función retorna la información descriptiva de los héroes. 
    Args:
        request (flask.Request): Objeto con la infromación de la petición.
    Returns:
        Representación en formato JSON de la información de los héroes 
    """
    return jsonify(data)
