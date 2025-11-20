# main.py -- archivo intencionalmente "problemático" para pruebas de SonarQube

import hashlib
import subprocess
import tempfile
import sqlite3

# 1) Hardcoded credential (security hotspot)
DB_USER = "admin"
DB_PASS = "P4ssw0rd123!"  # <-- hardcoded secret (Sonar should detect)

# 2) Mutable default argument (bad practice)
def append_item(item, bucket=[]):
    # Sonar marcará el argumento mutable por comportamiento inesperado
    bucket.append(item)
    return bucket

# 3) Use of eval (security hotspot)
def run_expression(expr):
    # Eval ejecuta código arbitrario: mala idea si la entrada no es confiable
    return eval(expr)

# 4) Insecure temporary filename (use of mktemp)
def create_temp_file_bad():
    tmp_name = tempfile.mktemp()  # vulnerable: race condition
    with open(tmp_name, "w") as f:
        f.write("temporary data")
    return tmp_name

# 5) Using subprocess with shell=True and unsanitized input
def run_shell(command):
    # Vulnerable a inyección si 'command' proviene de un usuario
    subprocess.run(command, shell=True)

# 6) Weak hashing for passwords (md5)
def store_password_cleartext(password):
    # MD5 is weak for storing passwords
    digest = hashlib.md5(password.encode()).hexdigest()
    return digest

# 7) SQL built by string concatenation (SQL injection)
def find_user_by_name(name):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    # CREATE a test table
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO users (name) VALUES ('alice'), ('bob')")
    # Dangerous concatenation:
    query = "SELECT id, name FROM users WHERE name = '%s'" % name
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    return result

# 8) Bare except that swallows errors
def divide(a, b):
    try:
        return a / b
    except:
        # Swallowing all exceptions is bad practice
        return None

if __name__ == "__main__":
    # generar algunos issues intencionales
    print("1) Append item (mutable default arg):", append_item("x"))
    print("2) Eval result (risky):", run_expression("1 + 2"))
    tmp = create_temp_file_bad()
    print("3) Temp file created (insecure):", tmp)
    # Ejecutar comando inseguro: cuidado al probar en entornos sensibles
    # run_shell("ls -la; echo hacked")  # opcional; comentar para seguridad
    print("4) MD5 of 'password':", store_password_cleartext("password"))
    print("5) SQL query (unsafe):", find_user_by_name("alice"))
    print("6) Division with bare except:", divide(1, 0))
