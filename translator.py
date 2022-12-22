from csv import DictWriter

from helpers import read_concept, read_extract
from constants import concepts

"""
nombre banco
    fecha | codigo | concepto | debito | credito | saldo
"""
if __name__ == '__main__':
    banks = ['supervielle']
    for bank in banks:
        extract_data = read_extract('supervielle')
        concepts_bank = read_concept('supervielle')
        with open(f'swap/translations/{bank}.csv', 'w', newline='\n') as transaltion:
            fieldnames=['fecha', 'codigo', 'concepto', 'debito', 'credito', 'saldo']
            csv = DictWriter(transaltion, fieldnames=fieldnames)
            csv.writeheader()
            for line in extract_data:
                codigo = concepts_bank.get(line['Concepto'])
                if codigo is None:
                    continue
                concepto = concepts[codigo]
                csv.writerow(
                    {
                        'fecha': line['Fecha'],
                        'codigo': codigo,
                        'concepto': concepto,
                        'debito': line['Débito'],
                        'credito': line['Crédito'],
                        'saldo': line['Saldo']

                    }
                )