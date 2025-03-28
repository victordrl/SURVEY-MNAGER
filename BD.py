import BDclave;
import mysql.connector;

def createDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE proyectoProfes")
    mycursor.close()
    mydb.commit()
    mydb.close()
    
def createTables():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor()    
    mycursor.execute(
        '''
            create table Usuarios (
                ID int not null auto_increment,
                username varchar (15) not null unique,
                uPassword varchar(30) not null,
                nombre varchar(30) not null,
                apellido varchar(30) not null,
                escuela varchar(20),
                telefono varchar(20),
                correo varchar(30),
                direccion varchar(30),
                primary key (ID)
                
            );

            CREATE TABLE Escuelas (
            ID  int auto_increment not null,
            Escuela varchar(20),
            PRIMARY KEY (ID)
            );




            CREATE TABLE Carreras (
            ID int auto_increment not null,
            Carrera varchar(30),
            Escuela int not null ,
            primary key (ID),
            foreign key (Escuela) references Escuelas(ID)
            );




            CREATE TABLE Materias (
            ID int auto_increment not null,
            Materia varchar(50) not null unique,
            primary key (ID)
            );

            CREATE TABLE MateriasxCarrera (
            Carrera INT NOT NULL,
            Materia INT NOT NULL,
            primary key (Carrera,Materia),
            foreign key (Carrera) references Carreras(ID),
            foreign key (Materia) references Materias(ID)
            );


            CREATE TABLE Profesores (
            ID int auto_increment not null,
            Cedula varchar(20) not null unique,
            Nombre varchar(50) not null,
            FechaIngreso date not null,
            FechaNacimiento date not null,
            Escuela int not null ,
            primary key (ID),
            foreign key (Escuela) references Escuelas(ID)
            );

            CREATE TABLE Alumnos (
            ID int auto_increment not null,
            Cedula varchar(20) not null unique,
            Nombre varchar(50) not null,
            Email varchar(255) not null unique,
            Carrera int not null ,
            primary key (ID),
            foreign key (Carrera) references Carreras(ID)
            );

            CREATE TABLE ProfesorxMateria (
            ID INT NOT NULL auto_increment PRIMARY KEY,
            Profesor  int not null ,
            Materia INT NOT NULL, 
            Seccion varchar (10),
            foreign key (Profesor) references Profesores(ID),
            foreign key (Materia) references Materias(ID)
            );

            CREATE TABLE Inscripciones (
            ID INT NOT NULL auto_increment PRIMARY KEY,
            Alumno  int not null ,
            Materia Int not null,
            foreign key (Alumno) references Alumnos(ID),
            foreign key (Materia) references ProfesorxMateria(ID)
            );

            CREATE TABLE Categorias(
            ID INT NOT NULL AUTO_INCREMENT primary KEY,
            Categoria VARCHAR(45)
                
            );

            Create table Preguntas(

            ID INT NOT NULL AUTO_INCREMENT primary KEY,
            Categoria int not null,
            Pregunta varchar (150),
            foreign key (Categoria) references Categorias(ID)
            );

            Create table Respuestas(

            ID INT NOT NULL AUTO_INCREMENT primary KEY,
            Respuesta varchar (60)
            );


            Create table Encuestas(

                ID int not null auto_increment primary key,
                Materia Int not null ,
                pregunta int not null,
                respuesta int not null,

                foreign key (Materia) references ProfesorxMateria(ID),
                foreign key (pregunta) references preguntas(ID),
                foreign key (respuesta) references respuestas(ID)

            );


        
            



            alter table  profesorxmateria add encuesta  varchar (80);
            alter table profesorxmateria add FechaForm Date;
            alter table  profesorxmateria add linkEncuesta  text;
            alter table inscripciones add encuestado bool;
            

        '''
    )
   
    print("tables created succesfully");

    mycursor.close()

def insertarDatos(tabla,columnas,cantidad, info ,cursor):
    comando = "INSERT INTO  %s (%s) VALUES (%s)" %(tabla,columnas,cantidad)
    cursor.executemany(comando,info)
'''
    seedtables es la funcion para llenar las tablas de info de prueba, debe ser llamada al instalar la app o 
    al abrirla por primera vez
'''
def insertarFormID(idMateria,idForm, link):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor();
    comando = '''update profesorxmateria 
        set encuesta = %s,
        linkEncuesta = %s
        where ID = %s'''
    mycursor.execute(comando,(idForm,link,idMateria))

    mydb.commit()


def insertarFechaForm(idMateria,date):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor();
    comando = '''update profesorxmateria 
        set date = %s,
        where ID = %s'''
    mycursor.execute(comando,(date,idMateria))

    mydb.commit()



def seedF():
    #Esta funcion guarda los links de estadistica 1 y 2, Bases de datos y ingenieria de sofware
    insertarFormID(1,'1SIGXyaM0_D03ury4SmLi8e6qqKAjynT1G5dtWceKJAA', 'https://docs.google.com/forms/d/e/1FAIpQLScKQfDluYIemITOOYuk0xSsMBG2ZzIVXsRbbSGMldSpi2ZjfA/viewform')
    insertarFormID(2,'1EgxyhcttQbEKgjXctp2g3hHQHY_1KHGSBndrzoHljnQ', 'https://docs.google.com/forms/d/e/1FAIpQLSerTQkkvRf4L9jMOdBu6Uh5WVi2xXg6v3ogo_XBbUKJoVwHDA/viewform')

    insertarFormID(3,'1VelEKYWSy0YaxkaffIC2pD1NHEHlqwgA_8F3AsWSAJc', 'https://docs.google.com/forms/d/e/1FAIpQLSeQz4_GQFghW1ju7EAT4hLaDiictYY85OWBTNBXf0cKbgrs7A/viewform')
    insertarFormID(4,'1zUSDF2kjWnj-DJg3T3xRyc75NP-bG4Fu0jNmHrsKau0', 'https://docs.google.com/forms/d/e/1FAIpQLSdEvnsIRPBu5ioWcX_nw8sOFvtsm1fpBHQGWwUsz7G7e3JyfA/viewform')


def seedTables():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor()
    insertarDatos('usuarios', 'username,uPassword,nombre,apellido,escuela,telefono,correo,direccion','%s,%s,%s,%s,%s,%s,%s,%s',
                [('aura','123456789','Aura','Apellido','Ingenieria','0424-000000','aura@gmail.com','Su casa',),],mycursor)
    




    insertarDatos("categorias","Categoria","%s",[
        ("Organizacion",),
        ("Dinamica pedagogica",),
        ("Criterios de calificacion",),
        ("Rasgos Academicos",),],
        mycursor)
    
    insertarDatos("preguntas","pregunta,Categoria","%s,%s",[
        ("Inicia y termina sus clases puntualmente.",1,),
        ("Desarrolla el curso de manera ordenada y cubriendo los objetivos planteados.",1,),
        (" Prevé el uso de recursos y materiales necesarios para la clase.",1,),


        ("Explica los temas del programa y atiende dudas de manera clara y precisa.",2,),
        (" Fomenta el uso correcto de la expresión oral y escrita.",2,),
        ("Discute y relaciona ejemplos reales con los temas tratados en clase.",2,),

        ("Evalúa de acuerdo con los contenidos y criterios presentados al inicio del curso",3,),
        (" Considera y evalúa las tareas relacionadas con el programa.",3,),


        ("Muestra interés por el desempeño de los/as estudiantes.",4,),
        ("Muestra disposición para consultarlo/a, dentro y fuera de clase.",4,),
        ("Motiva y fomenta la ética, los valores y el respeto.",4,),
        ],
        mycursor)

    insertarDatos("respuestas","Respuesta", "%s",[
        ("Muy ineficiente",),
        ("Ineficiente",),
        ("Regular",),
        ("Eficiente",),
        ("Muy eficiente",),],
        mycursor)
    

    insertarDatos("Escuelas","Escuela","%s",[
        ("Ingenieria",),
        ("Derecho",),
        ("Faces",)],
        mycursor)
    mydb.commit()


    insertarDatos("Profesores", "Cedula,Nombre, FechaIngreso, FechaNacimiento,Escuela","%s,%s,%s,%s,%s",[
        (11112222,"Luis Hernandez","2016-04-23","1970-04-23",1,),
        (12355132,"Yelenia","2016-04-23","1970-04-23",1,),
        (23522158,"Adalides ","2016-04-23","1970-04-23",1,),
        (23153251,'Yumilva Fermin', "2016-04-23","1970-04-23",1),
        (9231532,'Carlos lezama', "2016-04-23","1970-04-23",1),
        (193318859,'Manuel Romero', "2016-04-23","1970-04-23",1),],
        mycursor )
    
    mydb.commit()
    insertarDatos("Carreras","Carrera,Escuela","%s,%s",[
        ('Ingenieria Informatica',1,),
        ('Ingenieria en Sistemas',1,),],
        mycursor )
    
    mydb.commit()
    insertarDatos("Alumnos", "Cedula,Nombre,Email,Carrera","%s,%s,%s,%s",[
        ('30365852','Oswald Torrealba','c@gmail.com', '1',),
        ('30453426','Frank Diaz','p1@gmail.com', '1',),
        ('28272672','Victor Rojaz ','victor.rojas17.09Q@gmail.com', '1',),
        ('56464564','Maria Rojaz ','p3@gmail.com', '2',),
        ('21315548','Juan Rojaz ','p4@gmail.com', '1',),
        ('13584532','Carlos Rojaz ','p5@gmail.com', '1',),],
        mycursor)
    
    mydb.commit()
    insertarDatos("Materias","Materia", "%s",[
        ("Estadistica 1",),
        ("Estadistica 2",),
        ("Bases de datos",),
        ("INGENIERIA DE SOFTWARE",),],
        mycursor)

    mydb.commit()
    insertarDatos("MateriasxCarrera","Carrera,Materia","%s,%s",[
        ("1","1",),
        ("1","2",),
        ("1","3",),
        ("1","4",),

        ("2","1",),
        ("2","2",),
        ("2","3",),
        ("2","4",),],
        mycursor)
    
    insertarDatos("ProfesorxMateria", "Profesor,Materia,Seccion","%s,%s,%s",[
        ('1','1', '3D1',),
        ('1','2', '3D1',),
        ('2','3', '3D1',),
        ('3','4', '3D1',),],
        mycursor)
    
    mydb.commit()
    insertarDatos("inscripciones", "Alumno,Materia","%s,%s",[
        ('1', '1',),
        ('1', '2',),
        ('2', '1',),
        ('2', '2',),
        ('3', '1',),

        ('1', '3',),
        ('2', '3',),
        ('3', '3',),

        ('1', '4',),
        ('2', '4',),
        ('3', '4',),],
        mycursor)
    
    mydb.commit()

def insertarEncuestasSinExcel():
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor()

    
    mydb.commit()
    
def insertarUna(Materia,pregunta,respuesta):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor()
    
    insertarDatos("Encuestas","Materia,pregunta,respuesta", "%s,%s,%s",[
        (Materia,pregunta,respuesta,),],mycursor)
    
    mydb.commit()

def checkLogin(username, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )
    mycursor = mydb.cursor()
    
    command = """select exists(select * from usuarios 
    where username ="%s" AND uPassword = "%s");"""%(username,password)
    mycursor.execute(command)
    result = mycursor.fetchall()

    return (result[0][0])

def registrarInscribir(cedula,nombre,email,carrera,idMateria):
    mydb = mysql.connector.connect(
        host="localhost",
        user=BDclave.db_user,
        password=BDclave.db_password,
        database = "proyectoprofes"
    )

    mycursor = mydb.cursor()

    mydb.commit()
    insertarDatos("Alumnos", "Cedula,Nombre,Email,Carrera","%s,%s,%s,%s", [
        (cedula,nombre,email, carrera,),],
        mycursor)
    
    mydb.commit()
    idEstudiante =mycursor.lastrowid

    insertarDatos("inscripciones", "Alumno,Materia","%s,%s",[
        (idEstudiante, idMateria,),],
        mycursor)
    
    mydb.commit()



# createDatabase()
# createTables()
# seedTables()
# insertarEncuestasSinExcel()
# seedF()
# registrarInscribir('3065852','Oswald Torrealba','oswaldtorrealba1@gmail.com',1,4)
# insertarUna(4,1,2)
# insertarUna(4,2,1)
# insertarUna(4,3,3)
# insertarUna(4,5,5)
# insertarUna(4,6,4)
# insertarUna(4,7,5)
# insertarUna(4,8,5)
# insertarUna(4,9,3)
# insertarUna(4,10,3)
# insertarUna(4,11,1)
# print('listo')