class KudoConversion:
    ''' Classe que faz a conversão de kudos em valores monetários. Para iniciar, entre com os
        seguintes parâmetros:

        input >
        name:     string   -> Nome do funcionário
        points:   int      -> Número que indica a quantidade de pontos recebida pelo funcionário
        log:      bool     -> Se True mostra o log referente às iterações das análise dos pontos
                                recebido pelo funcionário. Default = False, ou seja, não mostrar.

        Exemplo de funcionamento:
        1- Criar a instância da classe com argumentos name e points na ordem a seguir

            > convert_Ana('Ana', 350)
                -> dessa forma a instância terá convert_Ana.name = 'Ana' e convert_Ana.points = 350

            É possível também usar da seguinte forma:

            > convert_Ana(points=350, name='Ana')
                -> teremos o mesmo resultado acima assinalado
        2- Uma vez que a instância esteja criada, devemos apenas aplicar o método analyse_points à ela:

            > convert_Ana.analyse_points()
                -> cujo resultado é:

                Ana Martis recebeu R$ 92.00 reais em retorno aos kudos ['SUPER', 'SUPER', 'SUPER', 'GREAT', 'OK']!
    '''

    def __init__(self, name, points, log=False):
        assert type(name) == str, 'Argumento name deve ser uma string!'
        assert type(
            points) == int, 'Argumento points deve ser um número inteiro!'
        assert type(log) == bool, 'Argumento log deve ser objeto booleano!'
        self.name = name
        self.points = points
        self.log = log

    def generate_conversion_list(self):
        self.kudos_list = ["SUPER", "GREAT", "GOOD", "NICE", "OK"]
        self.points_list = [100, 50, 20, 10, 5]
        self.cash_list = [25, 15, 8, 5, 2]
        self.kudo_dic = {}
        for key, kudo, cash in zip(self.points_list, self.kudos_list, self.cash_list):
            self.kudo_dic.update({key: (kudo, cash)})

    def analyse_points(self):
        self.generate_conversion_list()
        msg = []
        value = 0
        while self.points >= min(self.kudo_dic.keys()):
            if self.points >= max(self.kudo_dic.keys()):
                msg.append(self.kudo_dic[max(self.kudo_dic.keys())][0])
                value += self.kudo_dic[max(self.kudo_dic.keys())][1]
                if self.log == True:
                    print(f'+++++++ {self.name} +++++++')
                    print('points =', self.points)
                    print('Max kudos =', self.kudo_dic.keys())
                    print('message = ', msg)
                    print('----------------')
                self.points -= max(self.kudo_dic.keys())
            else:
                self.kudo_dic.pop(max(self.kudo_dic.keys()))
        print(f"{self.name} recebeu R$ {value:,.2f} reais em retorno aos kudos {msg}!")


if __name__ == "__main__":
    convert_Ana = KudoConversion('Ana Martis', 355)
    convert_Miguel = KudoConversion('Miguel Araújo', 232)
    convert_Hugo = KudoConversion('Hugo Rocha', 416)
    convert_Fernanda = KudoConversion('Fernanda Rodrigues', 278)
    convert_Milena = KudoConversion('Milena Alvez', 189)
    convert_Lucas = KudoConversion('Lucas Ramos', 501)
    convert_Thiago = KudoConversion('Thiago Simões', 13)
    convert_Natali = KudoConversion('Natali Gomes', 213, True)
    convert_Ana.analyse_points()
    convert_Miguel.analyse_points()
    convert_Hugo.analyse_points()
    convert_Fernanda.analyse_points()
    convert_Milena.analyse_points()
    convert_Lucas.analyse_points()
    convert_Thiago.analyse_points()
    convert_Natali.analyse_points()
