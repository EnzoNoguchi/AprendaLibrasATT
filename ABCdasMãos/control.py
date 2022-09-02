import os
import webbrowser as wb
from Model import model

class control:

    def __init__(self):
        self.opcao = -1
        self.modelo = model()

    # ==================================================================== G E T S / S E T S =====================================================================================

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao


    def getOpcaoAdm(self):
        return self.opcaoAdm

    def setOpcaoAdm(self, opcaoAdm):
        self.opcaoAdm = opcaoAdm



#==================================================================== M E N U =====================================================================================

    def menu(self):
        print("\n\n===================================================================" +
              "\nEscolha uma das opções abaixo: \n"+
              "0.Sair\n\n"+
              "1. Cadastrar\n"+
              "2. Entrar como administrador\n"+
              "===================================================================\n\n" +
              "3. Alfabeto em Libras\n"+
              "4. Numeros em Libras\n"+
              "5. Apresentação em Libras\n")
        self.setOpcao(int(input()))

    # ==================================================================== O P E R A C O E S ========================================================================

    def operacoes(self):

        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("OBRIGADO!")


            elif self.getOpcao() == 1:
                self.cadastrar()



            elif self.getOpcao() == 2:
                print("Digite o usuario: ")
                usuario = input()
                print("Digite a senha: ")
                senha = input()


                if (usuario == 'admin') and (senha == '123'):
                    print("Escolha uma das opções abaixo: \n" +
                          "\n0. Sair" +
                          "\n1. Cadastrar" +
                          "\n2. Consultar" +
                          "\n3. Atualizar Nome" +
                          "\n4. Atualizar Email" +
                          "\n5. Atualizar Senha" +
                          "\n6. Excluir")
                    self.setOpcaoAdm(int(input()))


                    if self.getOpcaoAdm() != 0:
                        if self.getOpcaoAdm() == 0:
                            print("Obrigado!")
                        elif self.getOpcaoAdm() == 1:
                            self.cadastrar()
                        elif self.getOpcaoAdm() == 2:
                            print(self.modelo.selecionar())
                        elif self.getOpcaoAdm() == 3:
                            self.atualizarNome()
                        elif self.getOpcaoAdm() == 4:
                            self.atualizarEmail()
                        elif self.getOpcaoAdm() == 5:
                            self.atualizarSenha()
                        elif self.getOpcaoAdm() == 6:
                            self.excluir()
                        else:
                            print("Opção escolhida invalida! Tente novamente!")








            elif self.getOpcao() == 3:
                while True:
                    print('\nSair[0] '
                          '\nA [1]  '
                          '\nB [2]  '
                          '\nC [3]  '
                          '\nD [4]  '
                          '\nE [5]  '
                          '\nF [6]  '
                          '\nG [7]  '
                          '\nH [8]  '
                          '\nI [9]  '
                          '\nJ [10] '
                          '\nK [11] '
                          '\nL [12] '
                          '\nM [13] '
                          '\nN [14] '
                          '\nO [15] '
                          '\nP [16] '
                          '\nQ [17] '
                          '\nR [18] '
                          '\nS [19] '
                          '\nT [20] '
                          '\nU [21] '
                          '\nV [22] '
                          '\nW [23] '
                          '\nX [24] '
                          '\nY [25] '
                          '\nZ [26] '
                          )
                    x = int(input('>>>'))
                    # Condições:
                    if x == 1:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-a.jpg')
                    elif x == 2:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-b.jpg')
                    elif x == 3:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-c.jpg')
                    elif x == 4:
                        wb.open('https://i.pinimg.com/236x/cb/5d/af/cb5dafd7c0b50601dc61a255844d60b1--asl-sign-language-letter-d.jpg')
                    elif x == 5:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-e.jpg')
                    elif x == 6:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-f.jpg')
                    elif x == 7:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-g.jpg')
                    elif x == 8:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-h.jpg')
                    elif x == 9:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-i.jpg')
                    elif x == 10:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-j.jpg')
                    elif x == 11:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-k.jpg')
                    elif x == 12:
                        wb.open('https://i.pinimg.com/736x/6d/b6/c1/6db6c104e313790145fde9c6e2fde270.jpg')
                    elif x == 13:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-m.jpg')
                    elif x == 14:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-n.jpg')
                    elif x == 15:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-o.jpg')
                    elif x == 16:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-p.jpg')
                    elif x == 17:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-q.jpg')
                    elif x == 18:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-r.jpg')
                    elif x == 19:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-s.jpg')
                    elif x == 20:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-t.jpg')
                    elif x == 21:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-u.jpg')
                    elif x == 22:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-v.jpg')
                    elif x == 23:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-w.jpg')
                    elif x == 24:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-x.jpg')
                    elif x == 25:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-y.jpg')
                    elif x == 26:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/alfabeto-em-libras-letra-z.jpg')
                    elif x == 0:
                        input('Aperte enter para sair.')

                        break
                    else:
                        print('Opção não aceita, por favor digite uma opção válida.')



            elif self.getOpcao() == 4:
                while True:
                    print('\nNumero 0 [0] '
                          '\nNumero 1 [1]  '
                          '\nNumero 2 [2]  '
                          '\nNumero 3 [3]  '
                          '\nNumero 4 [4]  '
                          '\nNumero 5 [5]  '
                          '\nNumero 6[6]  '
                          '\nNumero 7 [7]  '
                          '\nNumero 8 [8]  '
                          '\nNumero 9 [9]  '
                          '\nNumero 10 [10] '
                          )
                    x = int(input('>>>'))
                    # Condições:
                    if x == 1:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-1.jpg')
                    elif x == 2:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-2.jpg')
                    elif x == 3:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-3.jpg')
                    elif x == 4:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-4.jpg')
                    elif x == 5:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-5.jpg')
                    elif x == 6:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-6.jpg')
                    elif x == 7:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-7.jpg')
                    elif x == 8:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-8.jpg')
                    elif x == 9:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-9.jpg')
                    elif x == 10:
                        wb.open('https://i0.wp.com/atividadeparaeducacaoespecial.com/wp-content/uploads/2016/08/175.jpg')
                    elif x == 0:
                        wb.open('http://amordepapeis.com.br/wp-content/uploads/2019/12/numeros-em-libras-0.jpg')

                        break
                    else:
                        print('Opção não aceita, por favor digite uma opção válida.')






            elif self.getOpcao() == 5:
                while True:
                    print('\nDigite 1 para aprender a fazer sua apresentação em libras!\n\n0. Sair\n'

                          )
                    x = int(input('>>>'))
                    # Condições:
                    if x == 1:
                        wb.open('https://youtu.be/wWUgNiPhqyU')
                    elif x == 0:
                        print("Obrigado!")
                        break
                    else:
                        print('Opção não aceita, por favor digite uma opção válida.')



    # ==================================================================== M E T O D O S =====================================================================================

    def cadastrar(self):
        print("Informe o seu nome: ")
        nome = input()
        print("Informe seu email: ")
        email = input()
        print("Informe a sua senha: ")
        senha = input()
        print(self.modelo.inserir(nome, email, senha))

    def atualizarNome(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo nome")
        name = input()
        print(self.modelo.atualizar("nome", name, codigo))

    def atualizarEmail(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo Email")
        tel = input()
        print(self.modelo.atualizar("telefone", tel, codigo))

    def atualizarSenha(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe a nova Senha")
        end = input()
        print(self.modelo.atualizar("endereco", end, codigo))



    def excluir(self):
        print("Informe o código do dado que deseja excluir: ")
        cod = int(input())
        print(self.modelo.excluir(cod))




