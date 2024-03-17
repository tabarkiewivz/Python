import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Titanic:
    def __init__(self):
        self.titanic_data= pd.read_csv(r"/Users/karolcia/Desktop/titanic/train.csv")
        sns.set_style('darkgrid')

#Przedstaw dane w postaci tabeli
    def odczyt(self, n_rows):
        print(self.titanic_data.head(n_rows))

#sporządź histogram wieku ofiar
    def historiogram(self):
        self.titanic_data['Age'].plot(kind='hist', bins=20)
        plt.title('Historiogram wieku ofiar Titanica')
        plt.xlabel('Wiek')
        plt.ylabel('Liczba ofiar')
        plt.show()

#odpowiedz na pytanie - co mogło mieć wpływ na przeżycie pasażerów (płeć, wiek, status społeczny na podstawie klasy biletu)
    def analiza_przezycia(self):
        survival_by_sex = self.titanic_data.groupby('Sex')['Survived'].mean()
        survival_by_class = self.titanic_data.groupby('Pclass')['Survived'].mean()
        survival_by_age = pd.crosstab(self.titanic_data['Survived'], pd.cut(self.titanic_data['Age'], bins=[0, 18, 35, 50, 100]))

        print("\nAnaliza wpływu na przeżycie:")
        print("Średni współczynnik przeżycia według płci:")
        print(survival_by_sex)

        print("\nŚredni współczynnik przeżycia według klasy biletu:")
        print(survival_by_class)

        print("\nTabela przeżycia ze względu na wiek:")
        print(survival_by_age)

        print("\nZe wskazanych średnich można wywnioskować, że ocaleni to w większości osoby z biletami pierwszej klasy, kobiety oraz młodzi dorośli.")

#Następnie utwórz program z interfejsem konsolowym (CLI) do eksploracji wczytanego pliku w danymi
    def menu_show(self):
        while True:
            print('\nOpcje dostępne w programie: ')
            print('1. Wyświetl N wierszy dnych')
            print('2. Wyświetl historiogram')
            print('3. Wyświetl analizę wpływu na przeycie')
            print('4. Wyjście')

            wybor = int(input('Wybierz jedną z dostępnych opcji: '))

            if wybor == 1:
                n_rows = int(input('Ile wyświetlić wierszy? '))
                self.odczyt(n_rows)
            elif wybor == 2:
                self.historiogram()
            elif wybor == 3:
                self.analiza_przezycia()
            elif wybor == 4:
                print('Zakończenie programu')
                exit()
            else:
                print('Nieprawidłowa opcja. Spróbuj ponownie.')

if __name__ == "__main__":
    titanic_instance = Titanic()
    titanic_instance.menu_show()
