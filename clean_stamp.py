import psycopg2

DATABASE_URL = "postgresql://neondb_owner:npg_bDg56LINYFhl@ep-long-sound-ahzwwd4s-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def clean_alembic():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        print("Connexion à Neon... OK")

        # On vide la table qui stocke les numéros de révisions de migrations
        cur.execute('DELETE FROM alembic_version;')
        print("Historique des versions nettoyé.")

        conn.commit()
        cur.close()
        conn.close()
        print("\nPrêt pour le stamp !")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    clean_alembic()

