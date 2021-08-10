from jsf import JSF

faker = JSF.from_json("demo_schema.json")
fake_json = faker.generate()
print(fake_json)