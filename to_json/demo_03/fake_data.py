from faker import Faker
from dataclasses import dataclass, field, asdict, astuple
import json

from faker.generator import random

fake = Faker()  # 默认为英文locale
fake_zh_cn = Faker(locale='zh_CN')  # 设置为中文locale


@dataclass
class Emp:
    # dataclass 字段
    badge: str = field(default_factory=lambda: str(random.randrange(1, 8000)).zfill(5))
    name: str = field(default_factory=fake_zh_cn.name)
    ename: str = field(default_factory=fake.name)
    department: str = field(default_factory=lambda: random.choice(Emp.dept))
    job: str = field(default_factory=fake.job)
    idcard: str = field(default_factory=fake_zh_cn.ssn)
    phone: str = field(default_factory=fake_zh_cn.phone_number)
    gender: str = field(init=False)
    birthday: str = field(init=False)
    postcode: str = field(default_factory=fake.postalcode)
    email: str = field(default_factory=fake.email)
    workcity: str = field(default_factory=fake_zh_cn.city)
    address: str = field(default_factory=fake_zh_cn.address)

    # 辅助字段
    dept = ['IT部', '人事部', '财务部', '采购部', '运营部', '市场部', '销售部', '客服部']

    # 关联字段（根据身份证获取性别和生日）
    def __post_init__(self):
        self.gender = '男' if int(self.idcard[16:17]) % 2 else '女'
        self.birthday = self.idcard[6:14]


emp = [asdict(Emp()) for _ in range(5000)]
with open(r'fake_data.json', 'w') as f:
    json.dump(emp, f, ensure_ascii=False, indent=4)
