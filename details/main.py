import utilities as f
from flask import jsonify, abort

#Importación de la información de los heroes
data = f.load_file('./heroes.csv')

def get_heroe(request):
    """Definición de la función invocada por la Cloud Function. 
    La función retorna la información del héroe asociado al identificador especificado. 
    
    Args:
        request (flask.Request): Objeto con la infromación de la petición.
    Returns:
        Representación en formato JSON de la información del héroe especificado
        Para la respuesta se utiliza `flask.jsonify`
    """
    request_args = request.args
    if request_args and 'id' in request_args:
        id = request_args['id']
        if id in data:
            return jsonify(data[id])
    abort(404)
