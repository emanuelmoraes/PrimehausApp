import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class TelaInicial(Screen):
    pass

class TelaCalculo(Screen):
    def calcular(self):
        custo_m2 = float(self.ids['editCPM2'].text)
        ipi = float(self.ids['editIPI'].text)
        frete = float(self.ids['editFrete'].text)
        base_m2 = float(self.ids['editBaseM2'].text)
        altura = float(self.ids['editAltura'].text)
        largura = float(self.ids['editLargura'].text)
        desperdicio = float(self.ids['editDesperdicioM2'].text)

        resultado_ipi = (custo_m2 * ipi) / 100
        resultado_ipi += custo_m2
        tmp = (resultado_ipi * frete) / 100
        resultado_frete = resultado_ipi + tmp
        resultado = resultado_frete + base_m2

        self.ids['editIPIoutput'].text = str(resultado_ipi)
        self.ids['editFreteoutput'].text = "{:.2f}".format(resultado_frete)
        self.ids['editCTM2'].text = "{:.2f}".format(resultado)

        m2t = altura * largura
        self.ids['editM2T'].text = "{:.2f}".format(m2t)

        custo_tpt = resultado * m2t
        self.ids['editCustoTPT'].text = "{:.2f}".format(custo_tpt)

        custo_desperdicio = desperdicio * resultado_frete
        self.ids['editCustoDesperdicio'].text = "{:.2f}".format(custo_desperdicio)

        cctd = custo_desperdicio + custo_tpt
        self.ids['editCustocom100'].text = "{:.2f}".format(cctd)

        cc5d = ((custo_desperdicio * 50) / 100) + custo_tpt
        self.ids['editCustocom50'].text = "{:.2f}".format(cc5d)

        self.ids['btnVenda'].disabled = False
        screenTelaVenda = self.manager.get_screen('telavenda')
        screenTelaVenda.ids['editCustoVenda100'].text = "{:.2f}".format(cctd)
        screenTelaVenda.ids['editCustoVenda50'].text = "{:.2f}".format(cc5d)

    def resetar(self):
        self.ids['editIPIoutput'].text = ''
        self.ids['editFreteoutput'].text = ''
        self.ids['editCTM2'].text = ''
        self.ids['editM2T'].text = ''
        self.ids['editCustoTPT'].text = ''
        self.ids['editCustoDesperdicio'].text = ''
        self.ids['editCustocom100'].text = ''
        self.ids['editCustocom50'].text = ''
        self.ids['btnVenda'].disabled = True

class TelaVenda(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.cctd = 0.0
        self.cc5d = 0.0
        self.metragem_total_peca = 0.0

    def calcular(self):
        screenTelaCalculo = self.manager.get_screen('telacalculo')
        self.cctd = float(screenTelaCalculo.ids['editCustocom100'].text)
        self.cc5d = float(screenTelaCalculo.ids['editCustocom50'].text)
        self.metragem_total_peca = float(screenTelaCalculo.ids['editM2T'].text)
        margem = float(self.ids['editMargem'].text)
        preco_venda = 0.0

        if self.ids['checkCustoVenda100'].active == True:
            preco_venda = self.cctd * margem
        else:
            preco_venda = self.cc5d * margem
        self.ids['editPrecoVenda'].text = "{:.2f}".format(preco_venda)

        precentual_comissao = float(self.ids['editComissao'].text)
        valor_comissao = (preco_venda * precentual_comissao)/100
        self.ids['editComissaoOutput'].text = "{:.2f}".format(valor_comissao)

        precentual_imposto = float(self.ids['editImposto'].text)
        valor_imposto = (preco_venda * precentual_imposto)/100
        self.ids['editImpostoOutput'].text = "{:.2f}".format(valor_imposto)

        markup_bruto = preco_venda - self.cctd - valor_comissao - valor_imposto
        self.ids['editMarkupBruto'].text = "{:.2f}".format(markup_bruto)

        valor_venda_metro_quadrado = preco_venda / self.metragem_total_peca
        self.ids['editValorVendaM2'].text = "{:.2f}".format(valor_venda_metro_quadrado)

        percentual_markup = (markup_bruto * 100) / preco_venda
        self.ids['editPercentualMarkup'].text = "{:.2f}".format(percentual_markup)

    def resetar(self):
        self.ids['editPrecoVenda'].text = ''
        self.ids['editComissaoOutput'].text = ''
        self.ids['editImpostoOutput'].text = ''
        self.ids['editMarkupBruto'].text = ''
        self.ids['editValorVendaM2'].text = ''
        self.ids['editPercentualMarkup'].text = ''

class MainApp(App):
    pass

janela = MainApp()
janela.title = 'Precificação Primehaus'
janela.run()