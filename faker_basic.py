from faker import Faker, Factory
from faker.providers import internet

# 初始化Faker生成器并设置语言为中文
faker = Faker('zh_CN')

# 个人信息
print('姓名:', faker.name())
print('first name:', faker.first_name())
print('last name:', faker.last_name())
print('密码:', faker.password())
print('手机号:', faker.phone_number())
print('邮件:', faker.email())
print(f'Safe email: {faker.safe_email()}')
print(f'Free email: {faker.free_email()}')
print('信用卡号:', faker.ssn())
print('银行卡号:', faker.credit_card_number())
print('公司名:', faker.company())
print('职位:', faker.job())
print('个人简介:', faker.simple_profile())
print('个人综合简介:', faker.profile())
print('个人简介男:', faker.simple_profile('M'))
print('个人综合简介女:', faker.profile(sex='F'))

# 地址
print('地址:', faker.address())
print('国家', faker.country())
print('省:', faker.province())
print('城市:', faker.city())
print('城市名', faker.city_name())
print('街道地址:', faker.street_address())
print('街道名:', faker.street_name())
print('邮编:', faker.postcode())


# 随机字符、数字
print('随机字符串长度:', faker.pystr(12))
print('随机字符串最大长度:', faker.pystr(min_chars=2, max_chars=20))
print('随机数字:', faker.random_int())
print('0-100随机数字:', faker.random_int(0, 100))
print('随机整数:', faker.random_digit())

# 文本
print('随机文本:', faker.text())
print('随机段落:', faker.paragraph())
print('多个随机list:', faker.paragraphs())
print('随机词语:', faker.word())
print('随机词语list:', faker.words(6))
enum = ['中国', '美国', '英国', '俄国', 'wood', 'falcon']
print('枚举值中随机选取一个:', faker.words(1, enum, True))

# 货币
print('货币:', faker.currency())
print('货币name:', faker.currency_name())
print('货币code:', faker.currency_code())

# 哈希值 & uuid
print(f'md5: {faker.md5()}')
print(f'sha1: {faker.sha1()}')
print(f'sha256: {faker.sha256()}')
print(f'uuid4: {faker.uuid4()}')

# internet
print(f'Email: {faker.email()}')
print(f'Safe email: {faker.safe_email()}')
print(f'Free email: {faker.free_email()}')
print(f'Company email: {faker.company_email()}')
print(f'Host name: {faker.hostname()}')
print(f'Domain name: {faker.domain_name()}')
print(f'Domain word: {faker.domain_word()}')
print(f'TLD: {faker.tld()}')
print(f'IPv4: {faker.ipv4()}')
print(f'IPv6: {faker.ipv6()}')
print(f'MAC address: {faker.mac_address()}')
print(f'Slug: {faker.slug()}')
print(f'Image URL: {faker.image_url()}')

# 日期&时间
print(f'Date of birth: {faker.date_of_birth()}')
print(f'Century: {faker.century()}')
print(f'Year: {faker.year()}')
print(f'Month: {faker.month()}')
print(f'Month name: {faker.month_name()}')
print(f'Day of week: {faker.day_of_week()}')
print(f'Day of month: {faker.day_of_month()}')
print(f'Time zone: {faker.timezone()}')
print(f'AM/PM: {faker.am_pm()}')
print(f'Datetime this century: {faker.date_time_this_century()}')
print(f'Datetime this decade: {faker.date_time_this_decade()}')
print(f'Datetime this year: {faker.date_time_this_year()}')
print(f'Datetime this month: {faker.date_time_this_month()}')
print(f'Date this century：本世纪: {faker.date_this_century()}')
print(f'Date this decade：十年内: {faker.date_this_decade()}')
print(f'Date this year：今年: {faker.date_this_year()}')
print(f'Date this month: {faker.date_this_month()}')
print(f'Unix time: {faker.unix_time()}')
print(f'Datetime: {faker.date_time()}')
print(f'iso8601: {faker.iso8601()}')
print(f'Date: {faker.date()}')
print(f'Time: {faker.time()}')
print(f"Datetime between: {faker.date_time_between(start_date='-15y', end_date='now')}")
print(f"Date between: {faker.date_between()}")
print(f"Future datetime: {faker.future_datetime()}")
print(f"Future date: {faker.future_date()}")
print(f"Past datetime: {faker.past_datetime()}")
print(f"Past date: {faker.past_date()}")