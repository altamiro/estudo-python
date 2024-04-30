from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)


restaurante_avenida = Restaurante('avenida', 'bar')
restaurante_avenida.receber_avaliacao('Gui 1', 10)
restaurante_avenida.receber_avaliacao('Lais 2', 21)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()