import csv

from faker import Faker

import datetime

fake = Faker(['zh_CN'])

file = open("test_data.csv", "w", newline="")
# 此处若不加newline=""则会导致每行数据下多一个空白行
fwrite = csv.writer(file)
# 获取写文件的对象
fwrite.writerow(["name", "phone", "Card_id", "公司", "地址", "信用卡", "职位", "email"])
for i in range(9999):
    user_name = fake.name()
    phone = fake.phone_number()
    card_id = fake.ssn()
    company = fake.company()
    addr = fake.address()
    bank_card = fake.credit_card_number()
    title = fake.job()
    email = fake.email()
    fwrite.writerow([user_name, phone, card_id, company, addr, bank_card, title, email])
file.close()
