import sqlite3
con = sqlite3.connect("tutorial.db")




con.execute("""
create table students (
  Codmatricola char(3) primary key not null,
  name varchar(15) not null,
  surname varchar(30),
  class varchar(10)
);
""")
con.commit()
con.execute("""
create table entry_exit(
  Codmatricola char(3) not null,
  watch datatime not null,
  entry bool not null,
  foreign key (Codmatricola) references students(Codmatricola)
)
""")
con.commit()
con.execute("""
   insert into students values
   ('110','John','Amto','5F inf'),
   ('111','Matteo','Andreoli','5F inf'),
   ('112','Liming','Cai','5F inf'),
   ('113','Riccardo','Cantoni','5F inf'),
   ('114','Guido','Carlozzo','5F inf'),
   ('115','Riccardo','Colombetti','5F inf'),
   ('116','Klaus','Daja','5F inf'),
   ('117','Daniele','Ene','5F inf'),
   ('118','Edoardo','Ettore','5F inf'),
   ('119','Kris','Kehayov','5F inf'),
   ('120','Giovanni','Grassi','5F inf'),
   ('121','Samuel','La Barba','5F inf'),
   ('122','Matteo','Nastro','5F inf'),
   ('123','Matteo','Pellas','5F inf'),
   ('124','Riccardo','Studer','5F inf')


""")
con.commit()
con.close()
