def load_file(file_name: str) -> dict:
    """Obtiene la infromación de los héroes a partir del archivo especificado. 
    Args:
        file_name (str): Ruta del archivo con la información de los hérores.
    Returns:
        Diccionario con la información de conpleta de todos los héroes encontrados en el archivo
    """
    heroes = {}
    file = open(file_name, "r")
    file.readline()

    line = file.readline()
    while len(line) > 0:
        data = line.split(",")
        key = data[0]
        record = {}
        record['name'] = data[1]
        record['gender'] = data[2]
        record['eye_color'] = data[3]
        record['race'] = data[4]
        record['hair_color'] = data[5]
        record['height'] = data[6]
        record['publisher'] = data[7]
        record['skin_color'] = data[8]
        record['alignment'] = data[9]
        record['weight'] = data[10].replace('\n', '')
        heroes[key] = record
        line = file.readline()

    file.close()
    return heroes
