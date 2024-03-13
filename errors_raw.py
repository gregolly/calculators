class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'unprossableEntity'
        self.status_code = 422

try:
    print('Estou no bloco try')
    raise Exception("Excpet")
except Exception as exception:
    print("Tratamento de error")