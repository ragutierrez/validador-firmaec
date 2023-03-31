# Validador de documentos firmados electrónicamente con certificados de Ecuador
El presente proyecto es un consumo del API brindada por MINTEL para validar documentos firmados electrónicamente por certificados autorizados en Ecuador. Código realizado en el lenguaje de programación Python versión 3.11.

## Prerequisitos
- Docker (versión 20.10.18 o superior)
- docker-compose (version 1.29.2 o superior)
- Git
- Un archivo PDF firmado electrónicamente con un token o certificado válido para Ecuador.

## Ejecución
1. Clonar el repositorio e ingresar a la carpeta creada.

    ```git clone <ruta-repositorio> <nombre-carpeta>```

    ```cd <nombre-carpeta>```

2. Copiar los archivos PDF firmados electrónicamente en la ruta ```./files```.

3. Se debe construir el contenedor donde se ejecutará el llamado al API (Se puede obviar este paso).

    ```docker-compose -f local.yml build```

4. Ejecutar el siguiente comando:

    ```docker-compose -f local.yml run --rm --service-ports app_python python verifica_firma.py```

    La respuesta será un JSON con la información de cada archivo firmado con la siguiente estructura:
    ```
    {
        "firmasValidas": true/false,
        "integridadDocumento": true/false,
        "error": "Error (null)",
        "certificado": [
            {
                "emitidoPara": "NOMBRES Y APELLIDOS",
                "emitidoPor": "Entidad Emisora del Certificado",
                "validoDesde": "YYYY-MM-DD HH24:MI:SS",
                "validoHasta": "YYYY-MM-DD HH24:MI:SS",
                "fechaFirma": "YYYY-MM-DD HH24:MI:SS",
                "fechaRevocado": "YYYY-MM-DD HH24:MI:SS (OPCIONAL)",
                "certificadoVigente": true/false,
                "clavesUso": "Claves separadas por comas, ",
                "fechaSelloTiempo": "YYYY-MM-DD HH24:MI:SS (OPCIONAL)",
                "integridadFirma": true/false,
                "razonFirma": "Razón (OPCIONAL)",
                "localizacion": "Localizacion (OPCIONAL)",
                "cedula": "número de cédula del firmante",
                "nombre": "NOMBRES FIRMANTE",
                "apellido": "APELLIDOS FIRMANTE",
                "institucion": "Institución (OPCIONAL)",
                "cargo": "Cargo (OPCIONAL)",
                "entidadCertificadora": "Banco Central del Ecuador",
                "serial": "numero de serie",
                "selladoTiempo": true/false,
                "certificadoDigitalValido": true/false
            }
        ]
    }
    ```
## ¿Preguntas?
- [Contacto Telegram](https://t.me/ragutierrez)