#! python3
# Quiz z zlozonosci algorytmow.


class Algorithm:
    """Klasa zawiera informacje dotyczace pytania takie jak:
     jego nazwa algorytmu oraz jego zlozonosci pamieciowe i obliczeniowe [O(x), gdzie 'x' to okreslona zlozonosc."""

    def __init__(self, name, time_complexity, memory_complexity):
        self.name = name
        self.time_complexity = time_complexity
        self.memory_complexity = memory_complexity

    # Getters

    def get_name(self):
        return self.name.upper()

    def get_tcomplex(self):
        return self.time_complexity

    def get_mcomplex(self):
        return self.memory_complexity

    # Printers

    def print_tcomplex(self):
        return "Zlozonosc czasowa: O(" + self.time_complexity + ")"

    def print_mcomplex(self):
        return "Zlozonosc pamieciowa: O(" + self.memory_complexity + ")"

    # Setters

    def set_name(self, new_name):
        self.name = new_name

    def set_tcomplex(self, new_tcomplex):
        self.time_complexity = new_tcomplex

    def set_mcomplex(self, new_mcomplex):
        self.memory_complexity = new_mcomplex


# Main code execution

# List of algorithms


ALGORITHMS = [Algorithm("potegowanie", "n", "1"),
              Algorithm("szybkie potegowanie", "log n", "log n"),
              Algorithm("potegowanie binarne", "log n", "1"),
              Algorithm("liczby fib. - wpisuje do tablicy", "n", "n"),
              Algorithm("liczby fib. - wylicza F, pamieta dwie ostatnie", "n", "1"),
              Algorithm("liczby fib. - macierz", "log n", "1"),
              Algorithm("euklidesa nwd", "a+b", "1"),
              Algorithm("zoptymalizowany euklidesa", "log a + log b", "1"),
              Algorithm("znajdowanie min/max wartosci - progresja", "n", "1"),
              Algorithm("znajdowanie elementu min i max", "n", "1"),
              Algorithm("sortowanie babelkowe", "n^2", "1"),
              Algorithm("insertion sort", "n^2", "1"),
              Algorithm("selection sort", "n^2", "1"),
              Algorithm("scalanie posortowanych ciagow - iteracyjnie", "n+m", "n+m"),
              Algorithm("merge sort", "n*log n", "n"),
              Algorithm("podzial danych ciagu - Lomuta Sedgewicka", "n", "1"),
              Algorithm("quick sort", "n*log n", "log n"),
              Algorithm("wyszkukiwanie binarne - iteracjnie", "log n", "1"),
              Algorithm("max zysk na gieldzie - dziel i zwyciezaj", "n", "log n"),
              Algorithm("sortowanie przez zliczanie - counting sort", "n+k", "n+k"),
              Algorithm("sortowanie kubelkowe", "n", "n"),
              Algorithm("stokrotki dynamiczne", "n*m", "n*m"),
              Algorithm("trojkat pascala - dynamicznie", "n^2", "n"),
              Algorithm("impoementacja stosu na tablicy", "1", ""),
              Algorithm("implementacja kolejki na tablicy", "1", "")]

list_to_improve = []

test_list = [Algorithm("potegowanie", "n", "1"),
            Algorithm("szybkie potegowanie", "log n", "log n")]


def print_algorithms(algorithms_list):
    for i in range(len(algorithms_list)):
        print(algorithms_list[i].get_name(), algorithms_list[i].print_tcomplex(), algorithms_list[i].print_mcomplex())


def take_quiz(algorithms_list):
    total_points = 0
    t_answer, m_answer = "", ""
    for q in range(len(algorithms_list)):
        is_wrong = False
        current_question = algorithms_list[q]
        print("\n===" + current_question.get_name() + "===\n")
        t_answer = str(input("Podaj zlozonosc CZASOWA algorytmu: "))
        m_answer = str(input("Podaj zlozonosc PAMIECOWA algorytmu: "))

        if t_answer == current_question.get_tcomplex():
            total_points += 1
            print("Zlozonosc czasowa: Dobrze!")
        else:
            is_wrong = True
            print("Zlozonosc czasowa: Zle!")
            print("Poprawna odpowiedz: ", current_question.get_tcomplex())

        if m_answer == current_question.get_mcomplex():
            total_points += 1
            print("Zlozonosc pamieciowa: Dobrze!")
        else:
            is_wrong = True
            print("Zlozonosc pamieciowa: Zle!")
            print("Poprawna odpowiedz: ", current_question.get_mcomplex())

        if is_wrong:
            print("Nie znasz do konca tego algorytmu.")
            list_to_improve.append(current_question)
        else:
            print("Gratulacje! Znasz ten algorytm perfekcyjnie!")

    print("Calkowita ilosc punktow: ", str(total_points), " na ", len(algorithms_list) * 2, " mozliwych.")
    print("Lista algorytmow do douczenia:\n")
    print_algorithms(list_to_improve)


while True:
    print("1 - Test z wszystkich algorytmow")
    print("2 - Test z algorytmow potrzebnych douczenia")
    print("3 - Test testowy")
    print("0 - Wyjdz")
    user_choice = int(input("Podaj swoj wybor: "))
    if user_choice == 1:
        take_quiz(ALGORITHMS)
    if user_choice == 2:
        take_quiz(list_to_improve)
    if user_choice == 3:
        take_quiz(test_list)
    if user_choice == 0:
        break

input("Nacisnij ENTER, aby kontynuowac...\n")
