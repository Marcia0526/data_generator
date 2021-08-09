from jinja2 import Environment, FileSystemLoader
from faker import Faker

class User:

    def __init__(self, first_name, last_name, occupation):

        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation

faker = Faker()
users = []

for _ in range(10):

    first_name = faker.first_name()
    last_name = faker.last_name()
    occupation = faker.job()

    user = User(first_name, last_name, occupation)

    users.append(user)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('users.xml.j2')
output = template.render(users=users)

print(output, file=open('users.xml', 'w'))