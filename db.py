import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def ajouter_contact(nom, numero):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (nom, numero) VALUES (%s, %s)", (nom, numero))
    conn.commit()
    conn.close()

def lister_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    result = cursor.fetchall()
    conn.close()
    return result

def get_contact(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id = %s", (id,))
    result = cursor.fetchone()
    conn.close()
    return result

def modifier_contact(id, nom, numero):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET nom = %s, numero = %s WHERE id = %s", (nom, numero, id))
    conn.commit()
    conn.close()

def supprimer_contact(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = %s", (id,))
    conn.commit()
    conn.close()

