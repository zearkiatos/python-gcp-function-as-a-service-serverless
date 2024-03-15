# Step for deployment serverless service

## Validate project

```sh
# Checking the project
$ gcloud config get-value project
```

> [!IMPORTANT]  
> Create a cloud function
> 1. Activate cloud function
> 2. Activate cloud build API

## Public function
```sh
# gcloud functions deploy [FUNCTION_NAME] --entry-point [ENTRYPOINT] --runtime [APPLICATION_TYPE] --trigger-http --allow-unauthenticated --memory 128MB --region [REGION] --timeout 60 --min-instances 0 --max-instances 1

$ gcloud functions deploy function-list-heroes --entry-point list_heroes --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1
```

| Param        | Utility |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
|--entry-point | This set the function that will be call when the function will be invoke, besides it define the consume path where we can call|
|--runtime   | This let us set that how the function is develop with  and with what technology it will use for the execution.  In our case we will use python in 3.9 version. However, others versions and compilators exists    |
|--trigger-http            |Los tags que inician con "trigger" nos permiten definir el tipo de activador que invocará la función. En este caso establecemos que el activador va a ser una petición REST.                            |
|--allow-unauthenticated            |Este tag permite que la función se pueda consumir de manera pública y que no requiera ningún esquema de autenticación.                            |
|--memory            |Establece la cantidad de memoria que puede utilizar la función. Solo se permite la configuración de los siguientes valores: 128MB, 256MB, 512MB, 1024MB, 2048MB, 4096MB, y 8192MB.                           |
|--region            |Especifica la región en la que será publicada la función. Si desea ver las regiones disponibles, puede ver el siguiente enlace: Regiones y zonas.                          |
|--timeout           |Establece el máximo tiempo de espera que se tendrá para crear una función y atender la solicitud del activador.                        |
|--min-instances           |Establece la cantidad mínima de instancias que se tendrán de la función. Normalmente este valor es cero para ahorrar costos. Sin embargo se puede establecer en un valor mañor para evitar problemas de tiempo de espera cuando se realizan llamados entre periodos prolongados de tiempos.                       |
|--max-instances           |Establece la máxima cantidad de funciones que se pueden crear. Esto es muy útil cuando se realiza la definición de la carga del servicio. Tener presente que si las peticiones superan este valor, se pueden llegar a presentar problemas de timeout                       |