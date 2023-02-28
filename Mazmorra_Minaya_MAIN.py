import sys
from PyQt6.QtWidgets import (QApplication, QMessageBox, QMainWindow)
from PyQt6.QtGui import  QAction
from PyQt6 import QtCore, QtWidgets
from Mazmorra_Minaya import Ui_MainWindow
import random
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initializeUI()
        
    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""

        self.norteCompletado=False
        self.surCompletado=False
        self.esteCompletado=False
        self.oesteCompletado=False

        self.ui.bJugar.clicked.connect(self.desocultar)

        self.ui.salaNorte.clicked.connect(self.salaNorte)
        self.ui.salaNorte.hide() # HIDE THE BUTTON AT THE START

        self.ui.salaCentral.hide()

        self.ui.salaSur.clicked.connect(self.salaSur)
        self.ui.salaSur.hide()

        self.ui.salaEste.clicked.connect(self.salaEste)
        self.ui.salaEste.hide()

        self.ui.salaOeste.clicked.connect(self.salaOeste)
        self.ui.salaOeste.hide()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.createActions()
        self.setUpMainWindow()
        self.iniciar()
        self.show()

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu

        self.ui.actionAyuda.triggered.connect(self.ensenar)
        self.ui.actionSalir.triggered.connect(self.close)

    def desocultar(self): # muestra los botones de las salas
        self.ui.salaCentral.show()
        self.ui.salaNorte.show()
        self.ui.salaSur.show()
        self.ui.salaEste.show()
        self.ui.salaOeste.show()


    def iniciar(self):
        self.ui.label.setText("")
        self.ui.label_2.setText("")

        self.ui.radioButton.hide()
        self.ui.radioButton_2.hide()
        self.ui.radioButton_3.hide()
        self.ui.radioButton_4.hide()

    def salaCentral(self):
        self.ui.label.setText("Estas en la sala central, selecciona una sala.")
        self.ui.radioButton.hide()
        self.ui.radioButton_2.hide()
        self.ui.radioButton_3.hide()
        self.ui.radioButton_4.hide()
  

    def ensenar(self):
        QMessageBox.warning(self, "Funcionamiento del juego:",
                "Entraras a una sala la cual tendrá un reto que deberas pasar para completarla. "+
                "Al complatarla se te marcará como tal y podrás elegir otra sala. "+
                "Si completas todas las salas, ganaras!", 
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        
    def comporbar(self):    
            if self.norteCompletado==True and self.surCompletado==True and self.esteCompletado==True and self.oesteCompletado==True:
                    QMessageBox.warning(self, " ENHORABUENA ",
                    "¡¡¡ HAS COMPLETADO EL JUEGO !!!", 
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Cancel)
                    self.ui.label_2.setText("HAS COMPLETADO EL JUEGO\n(reinicia si quieres volver a jugar)")
                    self.ui.label.setText("")


    def seguir(self):
        num=random.randint(0,100)
        strnum=str(num)
        self.ui.label_2.setText("Para pasar de sala debes\nsacar mas de 60 sobre 100 y has sacado--->\n"+strnum+"\(pulsa Jugar)")
        
        if num>=60 :
            self.ui.label_2.setText("HAS VENCIDO ENHORABUENA, PASAS DE SALA")
            self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
            self.ui.salaNorte.setEnabled(False)
            self.norteCompletado=True
            self.comporbar()
            self.salaCentral()
        else:
            self.ui.label_2.setText("NO HAS VENCIDO.\n")
            self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color:lightgray;")
            self.salaCentral()

    def noAttak(self):
        self.ui.label_2.setText("AL NO ATACAR.\n Vuelves a la sala principal")
        self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color:lightgray;")
        self.salaCentral()

    def salaNorte(self):
            self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color : gray")
            self.ui.label.setText("Un enemigo, ha aparecido y te va a atacar.\nSi saca mas de 90 moriras.")
           
            ataca= random.randint(0,100)
            sacar= str(ataca)
            self.ui.label_2.setText("El enemigo ha sacado: \n"+sacar)
            if ataca >=90:
                self.ui.label_2.setText("Has muerto. Debes volver a empezar :C")
                self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color:lightgray;")
                self.salaCentral()
            else:
                   self.ui.label_2.setText("¿Quieres defenderte? (Plusa Jugar o Salir)")
                   
                   self.ui.bJugar.clicked.connect(self.seguir)
                   self.ui.bSalir.clicked.connect(self.noAttak)
                        
    def contestar(self):
        if  self.ui.radioButton_3.isChecked():
                self.ui.label_2.setText("HAS CONTESTADO CORRECTAMENTE ENHORABUENA, PASAS DE SALA")
                self.ui.salaSur.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color : rgb(204, 255, 189);")
                if self.norteCompletado==True:
                    self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                if self.oesteCompletado==True:
                    self.ui.salaOeste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                self.ui.salaSur.setEnabled(False)
                self.surCompletado=True
                self.comporbar()
                self.salaCentral()
                
        else:
                self.ui.label_2.setText("No has respondido correctamente, vuelves a la sala central")
                if self.norteCompletado==True:
                    self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                if self.oesteCompletado==True:
                    self.ui.salaOeste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                self.ui.salaSur.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color:lightgray;")
                self.salaCentral()
        

    def salaSur(self):
            self.ui.salaSur.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color : gray")
            acertijo=["Hay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú. ¿Qué es?",
            "Crezco a pesar de no estar vivo. No tengo pulmones, \npero para vivir necesito el aire. El agua, \naunque no tenga boca, me mata. ¿Qué soy?",
            "Estando roto es más útil que sin romperse. ¿Qué es?",
            "Aparato que vibra y gira, te metes en la boca unas 3 \nveces al día y mide unos 15 cm. ¿Qué es?",
            "Las personas siempre duermen menos en un mes del año. ¿Cuál es este mes?",
            "Estoy en todo pese a estar en nada. ¿Qué soy?",
            "Te paras cuando está verde y continúas cuando está rojo. ¿Qué es?",
            "¿Qué monte era el más alto del mundo antes de descubrir el Everest?",
            "Todos lo llevan por delante, pero lo muestran con recelo. \nTiene cabeza y agujas pero ningún pelo. ¿Qué es?",
            "Soy alto siendo joven y corto cuando soy viejo. Resplandezco\n con la vida y el viento es mi mayor enemigo. ¿Qué soy?"]
            respuesta=["Reloj de bolsillo",
            "Tu nombre",
            "El fuego",
            "El huevo",
            "Un cepillo de dientes eléctrico",
            "Febrero",
            "La letra D",
            "La sandía",
            "El monte Everest",
            "Reloj de bolsillo",
            "Una vela",
            "Tu nombre",
            "El fuego"]
            preg=random.randint(0,9)
            self.ui.label.setText("Para pasar de sala, has de contestar bien a la siguiente pregunta:\n"+acertijo[preg]+"\nPulsa la respuesta que creas correcta y el boton Jugar")
            
            self.ui.radioButton.show()
            self.ui.radioButton_2.show()
            self.ui.radioButton_3.show()
            self.ui.radioButton_4.show()

            self.ui.radioButton.setText(respuesta[preg])
            self.ui.radioButton_3.setText(respuesta[preg+1])
            self.ui.radioButton_2.setText(respuesta[preg+2])
            self.ui.radioButton_4.setText(respuesta[preg-1])
            
            self.ui.bJugar.clicked.connect(self.contestar)
            
    def salaEste(self):
            self.ui.salaEste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color : gray")
            self.ui.label.setText("PARA SALIR: debes tirar un dado y sacar mas de 63 de 100, si no lo haces a la primera, volveras a la sala central")
            
            num=random.randint(0,100)
            strnum=str(num)
            self.ui.label_2.setText("Has sacado: "+strnum)
           
            if num>=63:
                self.ui.label_2.setText("Has sacado: "+strnum+"\nHas pasado!! Enhorabuena sales de la sala")
                self.ui.salaEste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color :  rgb(204, 255, 189);")
                self.ui.salaEste.setEnabled(False)
                self.esteCompletado=True
                self.comporbar()
                self.salaCentral()   
            else:
                self.ui.label_2.setText("Has sacado: "+strnum+"\nNo has conseguido pasar!! Vuelves a la zona central")
                self.ui.salaEste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color:lightgray;")
                self.salaCentral()

    def contestarOeste(self):
        if  self.ui.radioButton_2.isChecked():
                self.ui.label_2.setText("HAS CONTESTADO CORRECTAMENTE ENHORABUENA, PASAS DE SALA")
                self.ui.salaOeste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color :  rgb(204, 255, 189);")
                if self.norteCompletado==True:
                    self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                if self.esteCompletado==True:
                    self.ui.salaEste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                self.ui.salaOeste.setEnabled(False)
                self.oesteCompletado=True
                self.comporbar()
                self.salaCentral()
                
        else:
                self.ui.label_2.setText("No has respondido correctamente, vuelves a la sala central")
                self.ui.salaOeste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color:lightgray;")
                if self.norteCompletado==True:
                    self.ui.salaNorte.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                if self.esteCompletado==True:
                    self.ui.salaEste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color: rgb(204, 255, 189);")
                self.salaCentral()
        
    def salaOeste(self):
            self.ui.salaOeste.setStyleSheet("border-radius: 10px;border: 2px solid black;background-color : gray")
            acertijo=["¿Cuál es el río más largo de España? ",
            "¿Cuál es el río más largo de la península ibérica?",
            "¿Cuál es el río más largo del mundo?",
            "¿Cuál es la montaña más alta de España?",
            "¿Cuál es la montaña más alta del mundo?",
            "¿Cuál es el océano más grande?",
            "¿Cuál es el país con más extensión?",
            "¿Cuál es el país más poblado?"]
            respuesta=["India",
            "Ebro",
            "Tajo",
            "Amazonas",
            "Teide",
            "Everest",
            "Pacífico",
            "Rusia",
            "India",
            "Ebro",
            "Tajo"]
            preg=random.randint(0,7)
            self.ui.label.setText("Para pasar de sala, has de contestar bien a la siguiente pregunta:\n"+acertijo[preg]+"\nPulsa la respuesta que creas correcta y el boton Jugar")
            
            self.ui.radioButton.show()
            self.ui.radioButton_2.show()
            self.ui.radioButton_3.show()
            self.ui.radioButton_4.show()

            self.ui.radioButton.setText(respuesta[preg])
            self.ui.radioButton_2.setText(respuesta[preg+1])
            self.ui.radioButton_3.setText(respuesta[preg+2])
            self.ui.radioButton_4.setText(respuesta[preg-1])
            
            self.ui.bJugar.clicked.connect(self.contestarOeste)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Keypad = MainWindow()
    sys.exit(app.exec())