'''This is the backend of the project.
    A database is created named medicines, using that DB we can store data required for the medicine predictor.
    Using sqlite3 we can create, connect, insert, retrieve, delete and execute sql commands directly.
'''
import sqlite3

# Connect to SQLite
conn = sqlite3.connect('medicines.db')
cursor = conn.cursor()

# Create medicines table
cursor.execute('''
CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT,
    age_limit TEXT,
    medicine TEXT,
    medical_history TEXT,
    chemical_formula TEXT
)
''')

# Sample 50 rows of medicine data
medicine_data = [
    ("fever", "1-12", "Paracetamol, Acetaminophen", "None", "C8H9NO2, C8H9NO2"),
    ("fever", "13-60", "Ibuprofen, Naproxen", "None", "C13H18O2, C14H14O3"),
    ("cough", "18-60", "Dextromethorphan, Codeine", "Diabetes", "C18H25NO, C18H21NO3"),
    ("cold", "18-60", "Cetirizine, Loratadine", "None", "C21H25ClN2O3, C22H23ClN2O2"),
    ("headache", "18-60", "Aspirin, Ibuprofen", "None", "C9H8O4, C13H18O2"),
    ("sore throat", "10-50", "Lozenges, Chlorhexidine", "None", "C6H8O6, C22H30Cl2N10"),
    ("stomach pain", "15-60", "Omeprazole, Pantoprazole", "None", "C17H19N3O3S, C16H15F2N3O4S"),
    ("acidity", "12-60", "Ranitidine, Famotidine", "None", "C13H22N4O3S, C8H15N7O2S3"),
    ("diarrhea", "5-60", "Loperamide, Racecadotril", "None", "C29H33ClN2O2, C21H23NO4S"),
    ("vomiting", "5-50", "Ondansetron, Domperidone", "None", "C18H19N3O, C22H24ClN5O2"),
    ("muscle pain", "18-60", "Diclofenac, Naproxen", "None", "C14H11Cl2NO2, C14H14O3"),
    ("hypertension", "30-70", "Amlodipine, Losartan", "None", "C20H25ClN2O5, C22H23ClN6O"),
    ("diabetes", "30-70", "Metformin, Glibenclamide", "None", "C4H11N5, C23H28ClN3O5S"),
    ("allergy", "5-60", "Loratadine, Fexofenadine", "None", "C22H23ClN2O2, C32H39NO4"),
    ("migraine", "18-60", "Sumatriptan, Rizatriptan", "None", "C14H21N3O2S, C15H19N5"),
    ("back pain", "18-60", "Naproxen, Diclofenac", "None", "C14H14O3, C14H11Cl2NO2"),
    ("asthma", "10-60", "Salbutamol, Budesonide", "None", "C13H21NO3, C25H34O6"),
    ("anemia", "10-60", "Ferrous Sulfate, Folic Acid", "None", "FeSO4, C19H19N7O6"),
    ("thyroid disorder", "18-60", "Levothyroxine, Liothyronine", "None", "C15H11I4NO4, C15H12I3NO4"),
    ("infection", "12-60", "Amoxicillin, Azithromycin", "None", "C16H19N3O5S, C38H72N2O12"),
    ("flu", "5-60", "Oseltamivir, Zanamivir", "None", "C16H28N2O4, C12H20N4O7"),
    ("sinusitis", "10-60", "Pseudoephedrine, Fluticasone", "None", "C10H15NO, C22H27FO4S"),
    ("depression", "18-60", "Fluoxetine, Sertraline", "None", "C17H18F3NO, C17H17Cl2N"),
    ("anxiety", "18-60", "Diazepam, Alprazolam", "None", "C16H13ClN2O, C17H13ClN4"),
    ("insomnia", "18-60", "Melatonin, Zolpidem", "None", "C13H16N2O2, C19H21N3O"),
    ("arthritis", "40-70", "Methotrexate, Celecoxib", "None", "C20H22N8O5, C17H14F3N3O2S"),
    ("osteoporosis", "40-70", "Alendronate, Risedronate", "None", "C4H13NO7P2, C7H11NO7P2"),
    ("seizures", "10-60", "Valproic Acid, Carbamazepine", "None", "C8H16O2, C15H12N2O"),
    ("high cholesterol", "30-70", "Atorvastatin, Rosuvastatin", "None", "C33H35FN2O5, C22H28FN3O6S"),
    ("gout", "30-70", "Allopurinol, Febuxostat", "None", "C5H4N4O, C16H16N2O3S"),
    ("eczema", "5-50", "Hydrocortisone, Tacrolimus", "None", "C21H30O5, C44H69NO12"),
    ("heartburn", "12-60", "Omeprazole, Esomeprazole", "None", "C17H19N3O3S, C17H19N3O3S"),
    ("ear infection", "5-60", "Ciprofloxacin, Amoxicillin", "None", "C17H18FN3O3, C16H19N3O5S"),
    ("UTI", "10-60", "Nitrofurantoin, Ciprofloxacin", "None", "C8H6N4O5, C17H18FN3O3"),
    ("pneumonia", "5-70", "Clarithromycin, Levofloxacin", "None", "C38H69NO13, C18H20FN3O4"),
]

# Insert data into table
cursor.executemany('''
INSERT INTO medicines (symptom, age_limit, medicine, medical_history, chemical_formula)
VALUES (?, ?, ?, ?, ?)
''', medicine_data)

# Commit changes and close connection
conn.commit()

# printing rows of table

cursor = conn.cursor()
cursor.execute("SELECT * FROM medicines")
print(cursor.fetchall())

#closing the connection
conn.close()

print(" Database initialized with 50 medicine records!")