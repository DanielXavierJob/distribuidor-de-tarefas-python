from companys import obter_quantidade
import json


def distribuir(empresas, pessoas):
    # ordena a array de empresas em ordem decrescente de quantidade de funcionários
    empresas.sort(key=lambda x: x['quantity_emp'], reverse=True)

    # calcula a quantidade total de funcionários e a quantidade média que cada pessoa deve receber
    total_emp = sum([e['quantity_emp'] for e in empresas])
    emp_por_pessoa = total_emp // len(pessoas)

    # cria um dicionário para armazenar a distribuição de empresas para cada pessoa
    distribuicao = {p: [] for p in pessoas}

    # lista de empresas já distribuídas
    empresas_distribuidas = []

    # itera sobre todas as empresas
    for empresa in empresas:
        # verifica se a empresa já foi distribuída antes
        if empresa in empresas_distribuidas:
            continue

        # itera sobre todas as pessoas, ordenando pelo número de funcionários que já receberam
        for pessoa in sorted(distribuicao, key=lambda x: sum([e['quantity_emp'] for e in distribuicao[x]])):
            # se a pessoa já recebeu funcionários suficientes, passa para a próxima pessoa
            if sum([e['quantity_emp'] for e in distribuicao[pessoa]]) >= emp_por_pessoa:
                continue

            # se a pessoa ainda pode receber funcionários, adiciona a empresa para a distribuição
            distribuicao[pessoa].append(empresa)

            # adiciona a empresa à lista de empresas já distribuídas
            empresas_distribuidas.append(empresa)

            break

    # itera sobre todas as pessoas para verificar se alguma não recebeu nenhuma empresa grande
    for pessoa in distribuicao:
        # se a pessoa não recebeu nenhuma empresa grande, adiciona a maior empresa à distribuição
        if not any([e['quantity_emp'] >= emp_por_pessoa*2 for e in distribuicao[pessoa]]):
            for empresa in empresas:
                if empresa not in distribuicao[pessoa] and empresa not in empresas_distribuidas:
                    distribuicao[pessoa].append(empresa)
                    empresas_distribuidas.append(empresa)
                    break

    # retorna a distribuição de empresas para cada pessoa
    return distribuicao


pessoas = ['Daniel', 'Thales', 'Pep']
grupos = distribuir(obter_quantidade(), pessoas)
with open("dados.json", "w") as arquivo:
    json.dump(grupos, arquivo)
    print("Json criado com as empresas")
for i, grupo in enumerate(grupos):
    print(
        f'Grupo {grupo} recebeu {len(grupos[grupo])} empresas com {sum([e["quantity_emp"] for e in grupos[grupo]])} funcionários')
    for empresa in grupos[grupo]:
        print(f'- {empresa["name"]}: {empresa["quantity_emp"]} funcionários')
    print()
