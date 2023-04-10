import base64
import asyncio
from pathlib import Path
from requests import post
from requests.exceptions import ConnectTimeout

HEADER = {"Content-Type": "text/plain; charset=UTF-8"}
WS_VALIDACION_FIRMA_MINTEL = (
    "https://ws.firmadigital.gob.ec/servicio/validacionavanzadapdf"
)


async def get_firmaec_detail(encoded_string):
    """Gets the dictionary of the signatures from MINTEL service

    Args:
        encoded_string (str): The pdf file encoded in string format
    """

    try:
        response_backup = post(
            url=WS_VALIDACION_FIRMA_MINTEL,
            data=encoded_string,
            headers=HEADER,
        )
        print(response_backup.text + "\n")
    except ConnectTimeout as err:
        print("Request has timed out WS_FIRMA_MINTEL")
        print(f"error info {err=}, {type(err)=}")
    except Exception as err:
        print("Error requesting WS_FIRMA_MINTEL")
        print(f"Unexpected {err=}, {type(err)=}")


def main():
    if not (Path(__file__).parent.parent.joinpath("files").exists()):
        print("Asegúrate de tener creado el directorio 'files'...")
    pdf_files_path = Path(__file__).parent.parent.joinpath("files")
    pdf_files = pdf_files_path.glob("*.pdf")
    pdf_files = [str(file_path) for file_path in pdf_files]
    number = 0
    print(f"Existe un total de {len(pdf_files)} PDFs.\n")
    for pdf in pdf_files:
        number += 1
        print(f"{number}. :::: {str(pdf)} ::::")
        with open(pdf, "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")

        sub_routine = get_firmaec_detail(encoded_string)

        asyncio.run(sub_routine)


if __name__ == "__main__":
    main()
