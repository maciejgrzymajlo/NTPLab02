Opis działania kodu
Plik train.py realizuje zadanie 2 i 3 laboratorium. Główne elementy:
load_wine() to zbiór Wine z scikit-learn (3 klasy, 13 cech)
Model	LogisticRegression – regresja logistyczna 
Hiperparametry	C czyli parametr regularyzacji (0.1, 0.5, 1.0, 2.0, 5.0)
Metryka	accuracy czyli dokładność klasyfikacji
Tracking URI sqlite:///mlflow.db zapis danych do bazy SQLite
Wine_Experiment to nazwa eksperymentu w MLflow
Działanie pętli:
Dla każdej wartości C tworzony jest nowy run. Model jest trenowany na zbiorze treningowym. Obliczana jest dokładność na zbiorze testowym. Do MLflow logowane są - parametr C, parametr max_iter, metryka accuracy oraz sam model. Wyniki są wyświetlane w konsoli

predict.py realizuje zadanie 5 
Tracking sqlite:///mlflow.db zgodny z train.py
Run ID e9db5f690bc84c38b2abeb3c16da02e1 – identyfikator najlepszego runu
Testowanie Pojedyncza próbka (pierwsza) z zbioru Wine
Działanie:
Ustawia tracking URI na bazę SQLite. Ładuje model o podanym Run ID. Przygotowuje pierwszą próbkę z zbioru Wine (klasa 0). Wykonuje predykcję i wyświetla:
- Przewidywaną klasę
- Prawdopodobieństwa przynależności do każdej klasy
- Oczekiwaną klasę

Wnioski z ćwiczenia
- MLflow pozwala na automatyczne logowanie parametrów, metryk i modeli, co ułatwia porównywanie różnych konfiguracji
- Każdy run otrzymuje unikalny identyfikator (Run ID), co umożliwia łatwe przywracanie wcześniejszych wersji modelu
- Ważne jest ustawienie odpowiedniego tracking_uri aby dane eksperymentów były prawidłowo przechowywane.

Link do repozytorium
https://github.com/maciejgrzymajlo/NTPLab02
