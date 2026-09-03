import ClienteRepository
from models.Cliente import Cliente

teste = Cliente("Arthur", "art@gmail.com", "123123123")
ClienteRepository.cadastrar_cliente(teste)