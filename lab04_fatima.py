#Zadatak 1

student = {"ime": "Fatima","prezime": "Salic", "godina": 3, "email": "ime.prezime@untz.ba"}
print(f"Ispis studenta: {student}")
print(f"Ime studenta:{student['ime']}")

student["aktivan"] = True

studenti_lista = [
    {"ime": "Fatima","prezime": "Salic", "godina": 3, "email": "fatima.salic@untz.ba","aktivan": True},
    {"ime": "Sejla","prezime": "Muminovic", "godina": 3, "email": "sejla.muminovic@untz.ba","aktivan": True},
    {"ime": "Edin","prezime": "Hodzic", "godina": 3, "email": "edin.hodzic@untz.ba","aktivan": True}
]

#Zadatak 2

# Definisanje funkcije pod nazivom get_student_info koja prima tri parametra:
# name (string/tekst), year (integer/cijeli broj) i email (string/tekst)
def get_student_info(name: str, year: int, email: str) -> dict:
    # Funkcija vraća rječnik (dictionary) koji sadrži proslijeđene podatke
    return {
        # Ključ 'name' dobija vrijednost iz parametra 'name'
        'name': name,
        # Ključ 'year' dobija vrijednost iz parametra 'year'
        'year': year,
        # Ključ 'email' dobija vrijednost iz parametra 'email'
        'email': email,
        # Ključ 'greeting' dobija vrijednost iz f-string-a koji kreira personaliziranu poruku pozdrava
        'greeting': f"Zdravo {name}, vi ste {year} godina studija"
    }
print(get_student_info("Fatima", 3, "fatima.salic@untz.ba"))

#Zadatak 3

def ispisi_poziv(func):  
    def wrapper(*args, **kwargs):  
        print(f"Pozivam funkciju: {func.__name__}")  
        return func(*args, **kwargs)  
    return wrapper  

@ispisi_poziv  
def info_o_studentu(ime: str, godina: int) -> dict:  
    pozdrav = f"Zdravo {ime}, vi ste {godina}. godina studija"  
    return {  
        'ime': ime,  
        'godina': godina,  
        'pozdrav': pozdrav  
    }

rezultat = info_o_studentu("Fatima", 3)

#Zadatak 4

# Definiraj klasu pod nazivom Course koja predstavlja kurs
class Course:
    # Konstruktor metoda koja inicijalizuje objekat Course sa imenom, kodom i kreditima
    def __init__(self, name: str, code: str, credits: int, professor: str):
        # Dodijeli parametar name instancnoj varijabli self.name
        self.name = name
        # Dodijeli parametar code instancnoj varijabli self.code
        self.code = code
        # Dodijeli parametar credits instancnoj varijabli self.credits
        self.credits = credits
        self.professor=professor

    # Metoda koja vraća opisni string kursa
    def description(self) -> str:
        # Vrati formatirani string sa kodom, imenom i kreditima
        return f"{self.code} - {self.name} ({self.credits} kredita), Profesor: {self.professor}"  
print(rezultat)  


course1 = Course("Razvoj telekomunikacijske programske podrške", "TK207", 6, "Alma Secerbegovic")  
course2 = Course("Baze podataka", "RI207", 6, " Emir Meskovic") 

print(course1.description())  
print(course2.description())  

#Zadatak 5

students = [
{"name": "Amina", "year": 3, "email": "amina@untz.ba"},
{"name": "Emir", "year": 2, "email": "emir@untz.ba"},
{"name": "Fatima", "year": 3, "email": "fatima@untz.ba"},
{"name": "Sejla", "year": 2, "email": "sejla@untz.ba"},
]

def filter_by_year(students: list, year: int) -> list:
    rezultat = [] 
    for stud in students:
        if stud["year"] == year:
            rezultat.append(stud) 
    return rezultat 

def print_registry(students: list) -> None:
    for stud in students:
        print(f"{stud['name']}-{stud['email']}")

print_registry(students)
filtered=filter_by_year(students, 2)
print(f"Filtrirani studenti:")
print_registry(filtered)