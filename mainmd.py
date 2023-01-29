import kivy
kivy.require("2.0.0")
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from SaveOpenCsv import SaveOpenCsv
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import os

class MainMdApp(MDApp):
    manager_open = None
    file_manager = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path, ext=['.csv'])

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        screenTelaSalvar = self.root.get_screen('telasalvar')
        if os.path.isdir(path):
            path += '/tmp.csv'
        screenTelaSalvar.ids['lbFile'].text = path

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("telas.kv")

    def callback(self, tela):
        self.root.current = str(tela)

    def salvar(self, file):
        screenTelaCalculo = self.root.get_screen('telacalculo')
        screenTelaVenda = self.root.get_screen('telavenda')

        custo_m2 = screenTelaCalculo.ids['editCMP2'].text
        ipi = screenTelaCalculo.ids['editIPI'].text
        frete = screenTelaCalculo.ids['editFrete'].text
        base_m2 = screenTelaCalculo.ids['editBaseM2'].text
        altura = screenTelaCalculo.ids['editAltura'].text
        largura = screenTelaCalculo.ids['editLargura'].text
        desperdicio = screenTelaCalculo.ids['editDesperdicioM2'].text
        resultado_ipi = screenTelaCalculo.ids['editIPIoutput'].text
        resultado_frete = screenTelaCalculo.ids['editFreteoutput'].text
        resultado = screenTelaCalculo.ids['editCTM2'].text
        m2t = screenTelaCalculo.ids['editM2T'].text
        custo_tpt = screenTelaCalculo.ids['editCustoTPT'].text
        custo_desperdicio = screenTelaCalculo.ids['editCustoDesperdicio'].text
        custo_total = screenTelaCalculo.ids['editCustocom100'].text
        custo_com_50 = screenTelaCalculo.ids['editCustocom50'].text

        margem = screenTelaVenda.ids['editMargem'].text
        percentual_comissao = screenTelaVenda.ids['editComissao'].text
        valor_comissao = screenTelaVenda.ids['editComissaoOutput'].text
        percentual_imposto = screenTelaVenda.ids['editImposto'].text
        valor_imposto = screenTelaVenda.ids['editImpostoOutput'].text
        markup_bruto = screenTelaVenda.ids['editMarkupBruto'].text
        valor_venda_metro_quadrado = screenTelaVenda.ids['editValorVendaM2'].text
        percentual_markup = screenTelaVenda.ids['editPercentualMarkup'].text

        csv = SaveOpenCsv()
        csv.nome_arquivo = file
        csv.set_dados(custo_m2, ipi, frete, base_m2, altura, largura, desperdicio, resultado_ipi, resultado_frete,
                         resultado, m2t, custo_tpt, custo_desperdicio, custo_total, custo_com_50, margem,
                         percentual_comissao, valor_comissao, percentual_imposto, valor_imposto, markup_bruto,
                         valor_venda_metro_quadrado, percentual_markup)
        csv.salvar()
        toast('Arquivo salvo')

    def abrir(self, file):
        screenTelaCalculo = self.root.get_screen('telacalculo')
        screenTelaVenda = self.root.get_screen('telavenda')

        csv = SaveOpenCsv()
        csv.nome_arquivo = file
        csv.abrir()

        screenTelaCalculo.ids['editCMP2'].text = csv.custo_m2
        screenTelaCalculo.ids['editIPI'].text = csv.ipi
        screenTelaCalculo.ids['editFrete'].text = csv.frete
        screenTelaCalculo.ids['editBaseM2'].text = csv.base_m2
        screenTelaCalculo.ids['editAltura'].text = csv.altura
        screenTelaCalculo.ids['editLargura'].text = csv.largura
        screenTelaCalculo.ids['editDesperdicioM2'].text = csv.desperdicio
        screenTelaCalculo.ids['editIPIoutput'].text = csv.resultado_ipi
        screenTelaCalculo.ids['editFreteoutput'].text = csv.resultado_frete
        screenTelaCalculo.ids['editCTM2'].text = csv.resultado
        screenTelaCalculo.ids['editM2T'].text = csv.m2t
        screenTelaCalculo.ids['editCustoTPT'].text = csv.custo_tpt
        screenTelaCalculo.ids['editCustoDesperdicio'].text = csv.custo_desperdicio
        screenTelaCalculo.ids['editCustocom100'].text = csv.custo_total
        screenTelaCalculo.ids['editCustocom50'].text = csv.custo_com_50

        screenTelaVenda.ids['editMargem'].text = csv.margem
        screenTelaVenda.ids['editComissao'].text = csv.percentual_comissao
        screenTelaVenda.ids['editComissaoOutput'].text = csv.valor_comissao
        screenTelaVenda.ids['editImposto'].text = csv.percentual_imposto
        screenTelaVenda.ids['editImpostoOutput'].text = csv.valor_imposto
        screenTelaVenda.ids['editMarkupBruto'].text = csv.markup_bruto
        screenTelaVenda.ids['editValorVendaM2'].text = csv.valor_venda_metro_quadrado
        screenTelaVenda.ids['editPercentualMarkup'].text = csv.percentual_markup
        toast('Arquivo carregado')
    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

class TelaCalculo(MDScreen):
    def calcular(self):
        custo_m2 = float(self.ids['editCMP2'].text)
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

class TelaVenda(MDScreen):
    def calcular(self):
        screenTelaCalculo = self.manager.get_screen('telacalculo')
        cctd = float(screenTelaCalculo.ids['editCustocom100'].text)
        cc5d = float(screenTelaCalculo.ids['editCustocom50'].text)
        metragem_total_peca = float(screenTelaCalculo.ids['editM2T'].text)
        margem = float(self.ids['editMargem'].text)
        preco_venda = 0.0

        if self.ids['checkCustoVenda100'].active == True:
            preco_venda = cctd * margem
        else:
            preco_venda = cc5d * margem
        self.ids['editPrecoVenda'].text = "{:.2f}".format(preco_venda)

        precentual_comissao = float(self.ids['editComissao'].text)
        valor_comissao = (preco_venda * precentual_comissao)/100
        self.ids['editComissaoOutput'].text = "{:.2f}".format(valor_comissao)

        precentual_imposto = float(self.ids['editImposto'].text)
        valor_imposto = (preco_venda * precentual_imposto)/100
        self.ids['editImpostoOutput'].text = "{:.2f}".format(valor_imposto)

        markup_bruto = preco_venda - cctd - valor_comissao - valor_imposto
        self.ids['editMarkupBruto'].text = "{:.2f}".format(markup_bruto)

        valor_venda_metro_quadrado = preco_venda / metragem_total_peca
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

janela = MainMdApp()
janela.title = "Precificação Primehaus MD"
janela.run()