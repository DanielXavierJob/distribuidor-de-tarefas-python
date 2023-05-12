import random

# Lista com nomes aleatórios de empresas
names = ['Acme Inc.', 'Globex Corporation', 'Soylent Green Co.', 'Umbrella Corporation', 'Wayne Enterprises',
         'Tyrell Corporation', 'Stark Industries', 'Aperture Science', 'Initech', 'Weyland-Yutani Corp.']

# Lista com 10 dicionários
empresas = []

for i in range(3):
    empresa = {
        'name': random.choice(names),
        'quantity_emp': random.randint(1, 1000)
    }
    empresas.append(empresa)


def obter_quantidade():
    empresas_refatoradas = []
    for emp in empresas:
        if (emp['quantity_emp'] > 0):
            empresas_refatoradas.append({
                "name": emp['name'],
                "quantity_emp": emp['quantity_emp']
            })
    return empresas_refatoradas
