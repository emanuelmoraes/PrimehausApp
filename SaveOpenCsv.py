import csv
from itertools import islice

class SaveOpenCsv:
    nome_arquivo = ''
    custo_m2 = ''
    ipi = ''
    frete = ''
    base_m2 = ''
    altura = ''
    largura = ''
    desperdicio = ''
    resultado_ipi = ''
    resultado_frete = ''
    resultado = ''
    m2t = ''
    custo_tpt = ''
    custo_desperdicio = ''
    custo_total = ''
    custo_com_50 = ''
    margem = ''
    percentual_comissao = ''
    valor_comissao = ''
    percentual_imposto = ''
    valor_imposto = ''
    markup_bruto = ''
    valor_venda_metro_quadrado = ''
    percentual_markup = ''
    def __int__(self, custo_m2='', ipi='', frete='', base_m2='', altura='', largura='', desperdicio='', resultado_ipi='',
                  resultado_frete='', resultado='', m2t='', custo_tpt='', custo_desperdicio='', custo_total='',
                  custo_com_50='', margem='', percentual_comissao='', valor_comissao='', percentual_imposto='',
                  valor_imposto='', markup_bruto='', valor_venda_metro_quadrado='', percentual_markup=''):
        self.custo_m2 = custo_m2
        self.ipi = ipi
        self.frete = frete
        self.base_m2 = base_m2
        self.altura = altura
        self.largura = largura
        self.desperdicio = desperdicio
        self.resultado_ipi = resultado_ipi
        self.resultado_frete = resultado_frete
        self.resultado = resultado
        self.m2t = m2t
        self.custo_tpt = custo_tpt
        self.custo_desperdicio = custo_desperdicio
        self.custo_total = custo_total
        self.custo_com_50 = custo_com_50
        self.margem = margem
        self.percentual_comissao = percentual_comissao
        self.valor_comissao = valor_comissao
        self.percentual_imposto = percentual_imposto
        self.valor_imposto = valor_imposto
        self.markup_bruto = markup_bruto
        self.valor_venda_metro_quadrado = valor_venda_metro_quadrado
        self.percentual_markup = percentual_markup

    def set_dados(self, custo_m2='', ipi='', frete='', base_m2='', altura='', largura='', desperdicio='', resultado_ipi='',
                  resultado_frete='', resultado='', m2t='', custo_tpt='', custo_desperdicio='', custo_total='',
                  custo_com_50='', margem='', percentual_comissao='', valor_comissao='', percentual_imposto='',
                  valor_imposto='', markup_bruto='', valor_venda_metro_quadrado='', percentual_markup=''):
        self.custo_m2 = custo_m2
        self.ipi = ipi
        self.frete = frete
        self.base_m2 = base_m2
        self.altura = altura
        self.largura = largura
        self.desperdicio = desperdicio
        self.resultado_ipi = resultado_ipi
        self.resultado_frete = resultado_frete
        self.resultado = resultado
        self.m2t = m2t
        self.custo_tpt = custo_tpt
        self.custo_desperdicio = custo_desperdicio
        self.custo_total = custo_total
        self.custo_com_50 = custo_com_50
        self.margem = margem
        self.percentual_comissao = percentual_comissao
        self.valor_comissao = valor_comissao
        self.percentual_imposto = percentual_imposto
        self.valor_imposto = valor_imposto
        self.markup_bruto = markup_bruto
        self.valor_venda_metro_quadrado = valor_venda_metro_quadrado
        self.percentual_markup = percentual_markup

    def __str__(self):
        return f'custo_m2: {self.custo_m2}, ipi: {self.ipi}, frete: {self.frete}'
    def abrir(self):
        if (len(str(self.nome_arquivo)) == 0):
            return
        with open(self.nome_arquivo, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|')
            for row in islice(spamreader, 1, None):
                print(row[0])
                self.custo_m2 = row[0]
                print(row[1])
                self.ipi = row[1]
                self.frete = row[2]
                self.base_m2 = row[3]
                self.altura = row[4]
                self.largura = row[5]
                self.desperdicio = row[6]
                self.resultado_ipi = row[7]
                self.resultado_frete = row[8]
                self.resultado = row[9]
                self.m2t = row[10]
                self.custo_tpt = row[11]
                self.custo_desperdicio = row[12]
                self.custo_total = row[13]
                self.custo_com_50 = row[14]
                self.margem = row[15]
                self.percentual_comissao = row[16]
                self.valor_comissao = row[17]
                self.percentual_imposto = row[18]
                self.valor_imposto = row[19]
                self.markup_bruto = row[20]
                self.valor_venda_metro_quadrado = row[21]
                self.percentual_markup = row[22]

    def salvar(self):
        if (len(str(self.nome_arquivo)) == 0):
            return
        with open(self.nome_arquivo, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_ALL)
            spamwriter.writerow(['custo_m2'] + ['ipi'] + ['frete'] + ['base_m2'] + ['altura'] +
                                ['largura'] + ['desperdicio'] + ['resultado_ipi'] + ['resultado_frete'] +
                                ['resultado'] + ['m2t'] + ['custo_tpt'] + ['custo_desperdicio'] + ['custo_total'] +
                                ['custo_com_50'] + ['margem'] + ['percentual_comissao'] + ['valor_comissao'] +
                                ['percentual_imposto'] + ['valor_imposto'] + ['markup_bruto'] + ['valor_venda_metro_quadrado'] +
                                ['percentual_markup'])
            spamwriter.writerow([self.custo_m2] + [self.ipi, self.frete, self.base_m2, self.altura,
                                 self.largura, self.desperdicio, self.resultado_ipi, self.resultado_frete,
                                 self.resultado, self.m2t, self.custo_tpt, self.custo_desperdicio, self.custo_total,
                                 self.custo_com_50, self.margem, self.percentual_comissao, self.valor_comissao,
                                 self.percentual_imposto, self.valor_imposto, self.markup_bruto, self.valor_venda_metro_quadrado,
                                 self.percentual_markup])

teste = SaveOpenCsv()
#teste.nome_arquivo = 'tmp.csv'
teste.custo_m2='88.0'
teste.salvar()