from peewee import Model, SqliteDatabase, CharField, DecimalField, ForeignKeyField, BooleanField
from dotenv import load_dotenv
from os import getenv

# importa o .env para armazenar dados sensíveis ao decorrer do código
load_dotenv()

DB_NAME = getenv('DB_NAME')

# cria o banco de dados
db = SqliteDatabase(f'{DB_NAME}')


class Client(Model):
    cpf = CharField()
    name = CharField()
    balance = DecimalField()

    class Meta:
        database = db


class Car(Model):
    client = ForeignKeyField(Client, backref='car')
    name = CharField()
    plate = CharField()
    model = CharField()
    value = DecimalField()
    sold = BooleanField(default=False)
    
    class Meta:
        database = db
        table_name = 'cars'  # Adicione o nome da tabela aqui


class Buyer(Model):
    cpf = CharField()
    name = CharField()
    deposit = DecimalField()
    balance = DecimalField()

    class Meta:
        database = db


class Bank(Model):
    client = ForeignKeyField(Client, backref='bank1')
    buyer = ForeignKeyField(Buyer, backref='bank2')
    balance = DecimalField()
    deposit = DecimalField()

    class Meta:
        database = db


try:
    db.connect()
    db.create_tables([Client, Buyer, Bank, Car])
    print('Banco e tabelas criadas com sucesso!')
except AttributeError as e:
    print(f'Ocorreu um erro ao criar {e}')
finally:
    db.close()
