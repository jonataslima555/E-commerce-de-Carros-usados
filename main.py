from models import db, Client, Car, Buyer, Bank

# Banco vendedor
def view_balance_client(cpf):
    try:
        client = Client.get(Client.cpf == cpf)
        print(f"Saldo do cliente {client.name} (CPF: {client.cpf}): R${client.balance}")
    except Client.DoesNotExist:
        print("Cliente não encontrado.")

# Criação de conta Vendedor
def create_account_client(cpf, name, balance):
    try:
        with db.atomic():
            Client.create(
                cpf=cpf,
                name=name,
                balance=balance
            )
        print('User created successfully!')
    except AttributeError as e:
        print(f"Erro ao criar usuário: {e}")

def register_account_client():
    cpf = input('Digite seu CPF: ')
    name = input('Digite seu nome completo: ')
    balance = int(input('Digite o quanto quer depositar: '))
    create_account_client(cpf, name, balance)
    return menu()

# Criação de Carros
def shop_car_client(cpf, name, plate, model, value):
    try:
        with db.atomic():
            Car.create(
                client=Client.get(Client.cpf == cpf),
                name=name,
                plate=plate,
                model=model,
                value=value
            )
        print('Carro cadastrado com sucesso!')
    except AttributeError as e:
        print(f'Erro ao cadastrar carro: {e}')
    finally:
        return home_client()

def view_car_client(cpf):
    try:
        client = Client.get(Client.cpf == cpf)
        cars = Car.select().where(Car.client == client)
        if cars:
            print(f"Carros do cliente {client.name} (CPF: {client.cpf}):")
            for car in cars:
                status = "Carro vendido" if car.sold else "Carro colocado à venda"
                print(f"Nome: {car.name}, Placa: {car.plate}, Modelo: {car.model}, Valor: R${car.value} - {status}")
        else:
            print("Nenhum carro encontrado para este cliente.")
    except Client.DoesNotExist:
        print("Cliente não encontrado.")
    except AttributeError as e:
        print(f"Ocorreu um erro: {e}")

def add_car_in_shop():
    cpf = input('Digite seu CPF: ')
    name = input('Digite o nome do veículo (Fiat Mobi, Fiat Uno): ')
    plate = input('Digite a placa do veículo: ').upper()
    model = input('Digite o modelo do carro (SUV, Hatch): ')
    value = input('Digite o valor do carro: R$')
    shop_car_client(cpf, name, plate, model, value)
    return home_client()

# Login e Home Vendedor
def home_client():
    print('\n1 - Ver carros à venda\n2 - Vender carro\n3 - Ver saldo\n4 - Logout')
    user = input(': ')
    if user == '1':  # Ver carros
        cpf = input('Digite seu CPF: ')
        view_car_client(cpf)
    elif user == '2':  # Vender carros
        return add_car_in_shop()
    elif user == '3':  # Ver saldo
        cpf = input('Digite seu CPF: ')
        view_balance_client(cpf)
        return home_client()
    elif user == '4':  # Logout
        return menu()

# Login Vendedor
def login_client():
    cpf = input("\nDigite seu CPF: ")
    name = input("Digite seu nome: ")
    try:
        client = Client.get(Client.cpf == cpf, Client.name == name)
        print(f"Bem-vindo, {client.name}!")
        return home_client()
    except Client.DoesNotExist:
        print("CPF ou nome incorretos. Tente novamente.")
        return login_client()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return login_client()

# Comprador criação de conta
def create_account_buyer(cpf, name, balance, deposit):
    try:
        with db.atomic():
            Buyer.create(
                cpf=cpf,
                name=name,
                balance=balance,
                deposit=deposit
            )
        print('User created successfully!')
    except AttributeError as e:
        print(f"Erro ao criar usuário: {e}")

def register_account_buyer():
    cpf = input('Digite seu CPF: ')
    name = input('Digite seu nome completo: ')
    balance = int(input('Digite o seu saldo atual: '))
    deposit = int(input('Digite quanto quer depositar: '))
    create_account_buyer(cpf, name, balance, deposit)
    return menu()

# Banco Comprador
def view_balance_buyer(cpf):
    try:
        buyer = Buyer.get(Buyer.cpf == cpf)
        print(f"Saldo do cliente {buyer.name} (CPF: {buyer.cpf}): R${buyer.balance}")
    except Buyer.DoesNotExist:
        print("Comprador não encontrado.")

# Função para visualizar todos os carros à venda
def view_all_cars_for_sale():
    cars = Car.select().where(Car.sold == False)
    if cars:
        print("Carros à venda:")
        for car in cars:
            print(f"ID: {car.id}, Nome: {car.name}, Placa: {car.plate}, Modelo: {car.model}, Valor: R${car.value}")
    else:
        print("Nenhum carro disponível para venda.")

# Função para comprar um carro
def buy_car(buyer_cpf, car_id):
    try:
        buyer = Buyer.get(Buyer.cpf == buyer_cpf)
        car = Car.get(Car.id == car_id)
        seller = car.client

        if buyer.balance >= car.value:
            with db.atomic():
                # Atualiza o saldo do comprador
                buyer.balance -= car.value
                buyer.save()

                # Atualiza o saldo do vendedor
                seller.balance += car.value
                seller.save()

                # Marca o carro como vendido
                car.sold = True
                car.save()

            print(f"Carro {car.name} comprado com sucesso por {buyer.name}!")
        else:
            print("Saldo insuficiente para comprar o carro.")
    except Buyer.DoesNotExist:
        print("Comprador não encontrado.")
    except Car.DoesNotExist:
        print("Carro não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Login comprador
def login_buyer():
    cpf = input("\nDigite seu CPF: ")
    name = input("Digite seu nome: ")
    try:
        client = Buyer.get(Buyer.cpf == cpf, Buyer.name == name)
        print(f"Bem-vindo, {client.name}!")
        return home_buyer()
    except Buyer.DoesNotExist:
        print("CPF ou nome incorretos. Tente novamente.")
        return login_buyer()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return login_buyer()

# Home comprador
def home_buyer():
    print('\n1 - Ver carros à venda\n2 - Comprar carro\n3 - Ver saldo\n4 - Logout')
    user = input(': ')
    if user == '1':  # Ver carros
        view_all_cars_for_sale()
        return home_buyer()
    elif user == '2':  # Comprar carro
        cpf = input('Digite seu CPF: ')
        car_id = int(input('Digite o ID do carro que deseja comprar: '))
        buy_car(cpf, car_id)
        return home_buyer()
    elif user == '3':  # Ver saldo
        cpf = input('Digite seu CPF: ')
        view_balance_buyer(cpf)
        return home_buyer()
    elif user == '4':  # Logout
        return menu()

def menu():
    print('Bem vindo...\n1 - Fazer Login\n2 - Criar conta\n3 - Sair')
    user = input(': ')

    if user == '1':  # login
        print('\n1 - Vendedor\n2 - Comprador\n3 - Voltar')
        user = input(': ')
        if user == '1':  # Vendedor
            return login_client()
        elif user == '2':  # Comprador
            return login_buyer()
        elif user == '3':
            return menu()
        else:
            print('Digite 1, 2 ou 3...')
            return menu()
    elif user == '2':
        print('Criar conta como:\n1 - Vendedor\n2 - Comprador\n3 - Voltar\n')
        user = input(': ')
        if user == '1':
            return register_account_client()
        elif user == '2':
            return register_account_buyer()
        elif user == '3':
            return menu()

if __name__ == "__main__":
    menu()
