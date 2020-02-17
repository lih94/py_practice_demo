from mimesis import Address
from mimesis import Business
from mimesis import Datetime
from mimesis import Person
from mimesis import Text
from mimesis import Code
from mimesis import Internet

person_zh = Person('zh')
print(person_zh.full_name(reverse=True))
print(person_zh.age())
print(person_zh.email(domains=["163.com", "126.com"]))
print(person_zh.gender())
print(person_zh.telephone(mask='+86 16#########', placeholder='#'))
print(person_zh.identifier(mask='#' * 17 + 'T'))
print('-------------------')
t = Text('zh')
print(t.title())
print(t.quote())
print('-------------------')
a = Address('zh')
print(a.province() + a.city() + a.street_name() + a.street_suffix() + a.street_number() + '号')
print(a.address())
print('-------------------')
b = Business('zh')
print(b.company() + b.copyright())
print('-------------------')
c = Code()
print(c.imei())
print('-------------------')
d = Datetime('zh')
print(d.formatted_datetime(start=2018, end=2018))
print('-------------------')
i = Internet()
print(i.ip_v4() + ' ' + i.mac_address())
