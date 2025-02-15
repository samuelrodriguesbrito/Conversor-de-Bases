#Bibliotecas
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

def converter(textoatual):
    return list(map(int, str(textoatual)))

#Janela
class janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Binary to Decimal Converter') #Título do programa
        self.resize(400, 200) #Tamanho da janela
        self.troca = False
#Botões
        #Botão C
        self.c = QPushButton('C', self)
        self.c.setGeometry(10,140, 80, 50)
        self.c.clicked.connect(self.limpar)
        #Converter
        self.converter = QPushButton('CONVERT', self)
        self.converter.setGeometry(90,140, 150, 50)
        self.converter.clicked.connect(self.resultado)
        #Trocar
        self.mudar = QPushButton('CHANGE', self)
        self.mudar.setGeometry(240,140, 150, 50)
        self.mudar.clicked.connect(self.trocar)
        self.mudar.clicked.connect(self.verificar)
#Campo de Texto
        #Campo 1
        self.texto1 = QLineEdit(self)
        self.texto1.setGeometry(10,70, 380, 65)
        self.texto1.setReadOnly(True)
        self.texto1.setPlaceholderText('Result')
        #Campo 2
        self.texto2 = QLineEdit(self)
        self.texto2.setGeometry(10,0, 380, 65)
        self.texto2.setPlaceholderText('Binary')
        regra = QRegularExpression("0|1[01]*")  # Aceita apenas 0 e 1 repetidamente
        validador = QRegularExpressionValidator(regra, self.texto2)
        self.texto2.setValidator(validador)
#Funções
    #Função de troca
    def trocar(self):
        self.texto1.setText('')
        self.texto2.setText('')
        if self.troca == True:
            self.texto2.setPlaceholderText('Binary')
            self.troca = False
        else:
            self.texto2.setPlaceholderText('Decimal')
            self.troca = True
    #Função números possíveis
    def verificar(self):
        textoatual = self.texto2.text()
        if self.troca == False:
            regra = QRegularExpression("0|1[01]*")  # Aceita apenas 0 e 1 repetidamente
            validador = QRegularExpressionValidator(regra, self.texto2)
            self.texto2.setValidator(validador)
        elif self.troca == True:
            regra = QRegularExpression("0|[1-9][0-9]*")  # Aceita de 0 e 9 repetidamente
            validador = QRegularExpressionValidator(regra, self.texto2)
            self.texto2.setValidator(validador)
    #Função de limpar
    def limpar(self):
        self.texto1.setText('')
        self.texto2.setText('')
    #Função de resultado
    def resultado(self):
        if self.troca == False:
            textoatual = self.texto2.text()
            lista = converter(textoatual)
            pot = 0
            resultado = 0
            for n in reversed(lista):
                p1 = n * (2 ** pot)
                p2 = p1 * n
                pot += 1
                resultado += p2
            self.texto1.setText(str(resultado))
        if self.troca == True:
            binario = ''
            textoatual = self.texto2.text()
            if textoatual == '0':
                self.texto1.setText('0')
            else:
                cod = int(textoatual)
                while cod > 0:
                    resto = cod % 2
                    binario += str(resto)
                    cod = int(cod / 2)
                self.texto1.setText(binario[::-1])

#Aplicação
program = QApplication(sys.argv)
window = janela()
window.show()
sys.exit(program.exec())