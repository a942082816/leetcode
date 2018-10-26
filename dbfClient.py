from dbfpy import dbf

## create empty DBF, set fields

db = dbf.Dbf("test.dbf", new=True)
db.addField(
    ("NAME", "C", 15),
    ("SURNAME", "C", 25),
    ("INITIALS", "C", 10),
    ("BIRTHDATE", "D"),
)

## fill DBF with some records

for name, surname, initials, birthdate in (
    ("John", "Miller", "JM", (1980, 1, 2)),
    ("Andy", "Larkin", "AL", datetime.date(1981, 2, 3)),
    ("Bill", "Clinth", "", DateTime.Date(1982, 3, 4)),
    ("Bobb", "McNail", "", "19830405"),
):
    
    rec = db.newRecord()
    rec["NAME"] = name
    rec["SURNAME"] = surname
    rec["INITIALS"] = initials
    rec["BIRTHDATE"] = birthdate
    rec.store()
db.close()