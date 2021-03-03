import psycopg2

#def Conectar():
    #Función para cambiar datos de la Base de Datos
    #conn = psycopg2.connect(
        #host="localhost",
        #port="5432",
        #user="postgres",
        #database="postgres",
        #password="aterre_1926")
    #return conn

def Crear_tablas():
    comandos = (
        """CREATE TABLE vendedores(
            vendedor VARCHAR (10) PRIMARY KEY,
            contraseña VARCHAR (6) NOT NULL,
            monto_venta DECIMAL NOT NULL,
            monto_comision DECIMAL NOT NULL)
        """,
        """CREATE TABLE inventario(
            producto VARCHAR (15) PRIMARY KEY,
            cantidad INTEGER NOT NULL,
            precio_unitario DECIMAL NOT NULL)
        """
    )
    
    conn = None
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        cur = conn.cursor()
        
        for comando in comandos:
            cur.execute(comando)
        
        cur.close()
        conn.commit()

        if conn is not None:
            conn.close()
        
        print('Conexión lograda')
               
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()

def insert_productos(producto, cantidad, precio):
    sql = """INSERT INTO inventario (producto, cantidad, precio_unitario)
             VALUES(%s, %s, %s);"""
             
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        cur = conn.cursor() 
        cur.execute(sql, (producto, cantidad, precio))

        conn.commit()
        cur.close()
        
        print(f'Producto {producto} agregado')
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insert_vendedores(vendedor, venta, comision):
    sql = """INSERT INTO vendedores (vendedor, monto_venta, monto_comision)
             VALUES(%s, %s, %s);"""
             
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        cur = conn.cursor()
        cur.execute(sql, (vendedor, venta, comision))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
    
    print(f'Vendedor {vendedor} agregado')
    
def visualizar_productos():
    sql = """ SELECT producto, cantidad, precio_unitario FROM inventario;"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                
                if cur is not None:
                    fila = cur.fetchall()
                    return fila
        
        if conn is not None:
            conn.close()
               
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()

def extraer_vendedor():
    sql = """ SELECT vendedor, contraseña FROM vendedores;"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                
                if cur is not None:
                    fila = cur.fetchall()
                    return fila
        
        if conn is not None:
            conn.close()
               
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()

def extraer_ventaycomision(vendedor):
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        cur = conn.cursor()
        
        cur.execute("SELECT monto_venta,monto_comision FROM vendedores WHERE vendedor=%s", (vendedor,))  
        codigo_curso = cur.fetchone()       
        cur.close()
        
        if conn is not None:
            conn.close()
            
        return codigo_curso
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def update_cantidad(producto, cantidad):
    sql = """ UPDATE inventario SET cantidad=%s WHERE producto=%s;"""
    
    conn = None
    
    #PARA DETECTAR ERRORES
    p = ['Arduino UNO','Capacitor','LED','LDR','Potenciometro','Resistor','Servomotor','Transistor','Triac']
    for i in p:
        if producto == i:
            break
    else:
        b=0
        print(1/b)
    a = len(producto)
    print(1/a)
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (cantidad,producto))

        if conn is not None:
            conn.close()
    
    finally:
        if conn is not None:
            conn.close()
    
def update_precio(producto, precio):
    sql = """ UPDATE inventario SET precio_unitario=%s WHERE producto=%s;"""
    
    conn = None
    
    #PARA DETECTAR ERRORES
    p = ['Arduino UNO','Capacitor','LED','LDR','Potenciometro','Resistor','Servomotor','Transistor','Triac']
    for i in p:
        if producto == i:
            break
    else:
        b=0
        print(1/b)
    a = len(producto)
    print(1/a)
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (precio,producto))

        if conn is not None:
            conn.close()
               
    finally:
        if conn is not None:
            conn.close()

def add_vendedores(vendedor,contraseña,venta,comision):
    sql = """ INSERT INTO vendedores (vendedor,contraseña,monto_venta,monto_comision) VALUES (%s, %s, %s, %s);"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        cur = conn.cursor()
        
        cur.execute(sql, (vendedor,contraseña,venta,comision))
        
        conn.commit()
        cur.close()

        if conn is not None:
            conn.close()
    
    finally:
        if conn is not None:
            conn.close()

def delete_vendedores(vendedor):
    sql = """ DELETE FROM vendedores WHERE vendedor = %s;"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendedor,))
                filas_borradas = cur.rowcount  
                #PARA DETECTAR ERRORES
                a = 1/filas_borradas
                print(a)
                print("Se eliminó %s filas."%filas_borradas)    
        
        if conn is not None:
            conn.close()
    
    finally:
        if conn is not None:
            conn.close()

def update_ventaycomision(vendedor, venta,comision):
    sql = """ UPDATE vendedores SET monto_venta=%s, monto_comision=%s WHERE vendedor=%s;"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="aterre_1926")
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (venta,comision,vendedor))

        if conn is not None:
            conn.close()
    
    finally:
        if conn is not None:
            conn.close()