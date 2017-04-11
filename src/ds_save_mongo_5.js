use myDB
#show dbs
#show tables
db.myCol.insert({"Persons":[{"id":"201511082","이름":"김가령"},{"id":"201511082","이름":"가령"}]})
db.myCol.find({"Persons.이름":"김가령"})