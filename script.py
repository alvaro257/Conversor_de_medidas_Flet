from flet import *
import flet as ft

# Variaveis globais

pagina_atual = 0
input = None
resultado_string = ft.Text(value='➜', size=20, weight=ft.FontWeight.BOLD, font_family='Verdana' ,color=colors.BLACK)

def main(page: Page):
    
    page.title = "Conversor de Unidades"
    page.window.width = 650
    page.window.height = 450
    page.window.always_on_top = True
    
    # Funcao responsavel por fazer a conversao de unidades conforme sua categoria
    def converter(e):
        global resultado_string
        global input
        global pagina_atual
        
        # Armanena as unidades de conversao selecionadas
        unidade_medida1 = ''
        unidade_medida2 = ''
        
        # Verifica se o valor digitado e valido
        try:
            float(input.value)
        except ValueError:
            if input.value:
                resultado_string.value = "Por favor, insira um número válido."
                page.update()
                return
            else:
                resultado_string.value = '➜'
                page.update()
                return
        
        # ------- CONVERSAO DE MEDIDAS ------- #
        
        # Conversao de Comprimento
        if pagina_atual == 1:
            unidade_medida1, unidade_medida2 = opcoes_comprimento1.value, opcoes_comprimento2.value
            if opcoes_comprimento_key[opcoes_comprimento1.value] < opcoes_comprimento_key[opcoes_comprimento2.value]:
                resultado = float(input.value) * 10**( opcoes_comprimento_key[opcoes_comprimento2.value] - opcoes_comprimento_key[opcoes_comprimento1.value])
            elif opcoes_comprimento_key[opcoes_comprimento1.value] > opcoes_comprimento_key[opcoes_comprimento2.value]:
                resultado = float(input.value) / 10**( opcoes_comprimento_key[opcoes_comprimento1.value] - opcoes_comprimento_key[opcoes_comprimento2.value]) 
            else:
                resultado = float(input.value)
                
        # Conversao de Massa
        elif pagina_atual == 2:
            unidade_medida1, unidade_medida2 = opcoes_massa1.value, opcoes_massa2.value
            if opcoes_massa_key[opcoes_massa1.value] < opcoes_massa_key[opcoes_massa2.value]:
                resultado = float(input.value) * 10**( opcoes_massa_key[opcoes_massa2.value] - opcoes_massa_key[opcoes_massa1.value])
            elif opcoes_massa_key[opcoes_massa1.value] > opcoes_massa_key[opcoes_massa2.value]:
                resultado = float(input.value) / 10**( opcoes_massa_key[opcoes_massa1.value] - opcoes_massa_key[opcoes_massa2.value]) 
            else:
                resultado = float(input.value)
        
        # Conversao de Capacidade
        elif pagina_atual == 3:
            unidade_medida1, unidade_medida2 = opcoes_capacidade1.value, opcoes_capacidade2.value
            if opcoes_capacidade_key[opcoes_capacidade1.value] < opcoes_capacidade_key[opcoes_capacidade2.value]:
                resultado = float(input.value) * 10**( opcoes_capacidade_key[opcoes_capacidade2.value] - opcoes_capacidade_key[opcoes_capacidade1.value])
            elif opcoes_capacidade_key[opcoes_capacidade1.value] > opcoes_capacidade_key[opcoes_capacidade2.value]:
                resultado = float(input.value) / 10**( opcoes_capacidade_key[opcoes_capacidade1.value] - opcoes_capacidade_key[opcoes_capacidade2.value]) 
            else:
                resultado = float(input.value)

        # Conversao de Volume
        elif pagina_atual == 4:
            unidade_medida1, unidade_medida2 = opcoes_volume1.value, opcoes_volume2.value
            if opcoes_volume_key[opcoes_volume1.value] < opcoes_volume_key[opcoes_volume2.value]:
                resultado = float(input.value) * 1000**( opcoes_volume_key[opcoes_volume2.value] - opcoes_volume_key[opcoes_volume1.value])
            elif opcoes_volume_key[opcoes_volume1.value] > opcoes_volume_key[opcoes_volume2.value]:
                resultado = float(input.value) / 1000**( opcoes_volume_key[opcoes_volume1.value] - opcoes_volume_key[opcoes_volume2.value]) 
            else:
                resultado = float(input.value)
        
        # Formata e exibe o resultado
        resultado_formatado = f"{resultado:,.6f}".replace(',','.')
        resultado_formatado = resultado_formatado.rstrip('0').rstrip('.')
        resultado_string.value = f"{input.value}{unidade_medida1} ➜ {resultado_formatado}{unidade_medida2}"
        page.update()
    
    # Funcao que atualiza os elementos da tela
    def atualizar_page(selected_index):
        global pagina_atual
        global input
        pagina_atual = selected_index
        
        # Caixa de texto que recebe o valor a ser convertido
        input = TextField(label='Insira o valor', width=200, on_change=converter)
        
        # Container que exibe o resultado
        resultado_container = Container(
            content=resultado_string,
            padding=10,
            width=490,
            bgcolor=ft.colors.BLUE_200,
            border_radius=10,
            alignment=ft.alignment.center,
            )
        
        # Limpa as informacoes da pagina selecionada anteriormente
        paginas.controls.clear()
        
        # Limpa o input e resultado da pagina anterior
        input.value = ''
        resultado_string.value = '➜'
        page.update()
        
        # Atualiza a pagina conforme o selected_index
        if selected_index == 0:
            paginas.controls.extend([
                Column([
                    ft.Text("Conversor de unidades", size=25, weight=ft.FontWeight.BOLD, font_family='Verdana', height=40),
                    ft.Text('Esse software é capaz de converter diferentes unidades de comprimento, massa, capacidade e volume.', size=18, font_family='Times New Roman', height=60),
                    ft.Text('As unidades de medida nele usadas são:', size=18, font_family='Times New Roman'),
                    ft.Text('   • COMPRIMENTO (km, hm, dam, m, dm, cm, mm);', size=18, font_family='Times New Roman'),
                    ft.Text('   • MASSA (kg, hg, dag, g, dg, cg, mg);', size=18, font_family='Times New Roman'),
                    ft.Text('   • CAPACIDADE (kl, hl, dal, l, dl, cl, ml);', size=18, font_family='Times New Roman'),
                    ft.Text('   • VOLUME (km3, hm3, dam3, m3, dm3, cm3, mm3);', size=18, font_family='Times New Roman'),
                    ft.Text('Os métodos de conversão usados no desenvolvimento desse software estão disponíveis em: https://escolakids.uol.com.br/matematica/unidades-de-medidas-por-que-elas-existem.htm', size=16, font_family='Times New Roman'),
                ])
            ])

        elif selected_index == 1:
            paginas.controls.extend([
                ft.Text("Conversor de Comprimento", size=27, weight=ft.FontWeight.BOLD, font_family='Times New Roman'),
                Row([
                    opcoes_comprimento1,
                    input,
                    opcoes_comprimento2,
                ]),
                Row([ft.Text("Resultado:", size=23, weight=ft.FontWeight.BOLD, font_family='Times New Roman')]),
                Row([
                    resultado_container
                ]),
            ])

        elif selected_index == 2:
            paginas.controls.extend([
                ft.Text("Conversor de Massa", size=27, weight=ft.FontWeight.BOLD, font_family='Times New Roman'),
                Row([
                    opcoes_massa1,
                    input,
                    opcoes_massa2,
                ]),
                Row([ft.Text("Resultado:", size=23, weight=ft.FontWeight.BOLD, font_family='Times New Roman')]),
                Row([
                    resultado_container
                ]),
            ])

        elif selected_index == 3:
            paginas.controls.extend([
                ft.Text("Conversor de Capacidade", size=27, weight=ft.FontWeight.BOLD, font_family='Times New Roman'),
                Row([
                    opcoes_capacidade1,
                    input,
                    opcoes_capacidade2,
                ]),
                Row([ft.Text("Resultado:", size=23, weight=ft.FontWeight.BOLD, font_family='Times New Roman')]),
                Row([
                    resultado_container
                ]),
            ])

        elif selected_index == 4:
            paginas.controls.extend([
                ft.Text("Conversor de Volume", size=27, weight=ft.FontWeight.BOLD, font_family='Times New Roman'),
                Row([
                    opcoes_volume1,
                    input,
                    opcoes_volume2,
                ]),
                Row([ft.Text("Resultado:", size=23, weight=ft.FontWeight.BOLD, font_family='Times New Roman')]),
                Row([
                    resultado_container
                ]),
            ])
        page.update()
    
    # Menu de opcoes
    lateral = NavigationRail(
        selected_index=0,
        destinations=[
            NavigationRailDestination(
                icon= icons.HOME, selected_icon=icons.HOME, label= "Home"
            ),
            NavigationRailDestination(
                icon= icons.STRAIGHTEN, selected_icon=icons.STRAIGHTEN, label= "Comprimento"
            ),
            NavigationRailDestination(
                icon= icons.SCALE, selected_icon=icons.SCALE, label= "Massa"
            ),
            NavigationRailDestination(
                icon= icons.WAVES, selected_icon=icons.WAVES, label= "Capacidade"
            ),
            NavigationRailDestination(
                icon= icons.WATER_DROP, selected_icon=icons.WATER_DROP, label= "Volume"
            ),
        ],
        on_change=lambda e: atualizar_page(e.control.selected_index),
        )
    
    # Coluna para exibir o conteudo das paginas
    paginas = Column(expand=True)
    
    # ------- DROPDOWNS ------- #
    
    # Dropdowns Comprimento
    opcoes_comprimento_key = { 'km': 1,'hm': 2,'dam': 3,'m': 4,'dm': 5,'cm': 6,'mm': 7,}
    opcoes_comprimento1 = Dropdown(width=70, value='km', options=[
        ft.dropdown.Option('km'),
        ft.dropdown.Option('hm'),
        ft.dropdown.Option('dam'),
        ft.dropdown.Option('m'),
        ft.dropdown.Option('dm'),
        ft.dropdown.Option('cm'),
        ft.dropdown.Option('mm'),
        
    ], on_change=converter)
    opcoes_comprimento2 = Dropdown(width=70, value='m', options=[
        ft.dropdown.Option('km'),
        ft.dropdown.Option('hm'),
        ft.dropdown.Option('dam'),
        ft.dropdown.Option('m'),
        ft.dropdown.Option('dm'),
        ft.dropdown.Option('cm'),
        ft.dropdown.Option('mm'),
        
    ], on_change=converter)
    
    # Dropdowns Massa
    opcoes_massa_key = { 'kg': 1,'hg': 2,'dag': 3,'g': 4,'dg': 5,'cg': 6,'mg': 7,}
    opcoes_massa1 = Dropdown(width=70, value='kg', options=[
        ft.dropdown.Option('kg'),
        ft.dropdown.Option('hg'),
        ft.dropdown.Option('dag'),
        ft.dropdown.Option('g'),
        ft.dropdown.Option('dg'),
        ft.dropdown.Option('cg'),
        ft.dropdown.Option('mg'),
        
    ], on_change=converter)
    opcoes_massa2 = Dropdown(width=70, value='g', options=[
        ft.dropdown.Option('kg'),
        ft.dropdown.Option('hg'),
        ft.dropdown.Option('dag'),
        ft.dropdown.Option('g'),
        ft.dropdown.Option('dg'),
        ft.dropdown.Option('cg'),
        ft.dropdown.Option('mg'),
        
    ], on_change=converter)
    
    # Dropdowns Capacidade
    opcoes_capacidade_key = { 'kl': 1,'hl': 2,'dal': 3,'l': 4,'dl': 5,'cl': 6,'ml': 7,}
    opcoes_capacidade1 = Dropdown(width=70, value='kl', options=[
        ft.dropdown.Option('kl'),
        ft.dropdown.Option('hl'),
        ft.dropdown.Option('dal'),
        ft.dropdown.Option('l'),
        ft.dropdown.Option('dl'),
        ft.dropdown.Option('cl'),
        ft.dropdown.Option('ml'),
        
    ], on_change=converter)
    opcoes_capacidade2 = Dropdown(width=70, value='l', options=[
        ft.dropdown.Option('kl'),
        ft.dropdown.Option('hl'),
        ft.dropdown.Option('dal'),
        ft.dropdown.Option('l'),
        ft.dropdown.Option('dl'),
        ft.dropdown.Option('cl'),
        ft.dropdown.Option('ml'),
        
    ], on_change=converter)
    
    # Dropdowns Volume
    opcoes_volume_key = { 'km3': 1,'hm3': 2,'dam3': 3,'m3': 4,'dm3': 5,'cm3': 6,'mm3': 7,}
    opcoes_volume1 = Dropdown(width=80, value='km3', options=[
        ft.dropdown.Option('km3'),
        ft.dropdown.Option('hm3'),
        ft.dropdown.Option('dam3'),
        ft.dropdown.Option('m3'),
        ft.dropdown.Option('dm3'),
        ft.dropdown.Option('cm3'),
        ft.dropdown.Option('mm3'),
        
    ], on_change=converter)
    opcoes_volume2 = Dropdown(width=80, value='m3', options=[
        ft.dropdown.Option('km3'),
        ft.dropdown.Option('hm3'),
        ft.dropdown.Option('dam3'),
        ft.dropdown.Option('m3'),
        ft.dropdown.Option('dm3'),
        ft.dropdown.Option('cm3'),
        ft.dropdown.Option('mm3'),
        
    ], on_change=converter)
    
    page.add(
        Row(
            [
                lateral,
                VerticalDivider(width=1),
                paginas,
            ],
            expand= True
        )
    )
    atualizar_page(0)

app(target=main)