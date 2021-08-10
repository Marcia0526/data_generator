from faker import Faker
from dataclasses import dataclass, field, asdict, astuple
import pandas as pd
from sqlalchemy.types import NVARCHAR, DATE
from sqlalchemy import create_engine
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


# 设置数据库连接DSN
db_con_str = 'mssql+pyodbc://@AdventureWorks2012'
engine = create_engine(db_con_str)

# 生成数据转并化为字典列表
emp = [asdict(Emp()) for _ in range(5000)]
columns = ['badge', 'ename', 'name', 'department', 'job', 'idcard', 'phone'
    , 'gender', 'birthday', 'postcode', 'email', 'workcity', 'address']
df = pd.DataFrame(emp, columns=columns)

# 指定字段类型
dtype = {column: NVARCHAR(2000) for column in df.columns}
dtype['birthday'] = DATE

# 保存到数据库
df.to_sql('employee', con=engine, if_exists='replace', dtype=dtype, index=False)
