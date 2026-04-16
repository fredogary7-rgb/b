import psycopg2

DATABASE_URL = "postgresql://neondb_owner:npg_bDg56LINYFhl@ep-long-sound-ahzwwd4s-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def run_fix():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        print("Connexion à Neon... OK")

        # 1. On force le username en UNIQUE (Indispensable pour la Foreign Key)
        cur.execute('ALTER TABLE "user" ADD CONSTRAINT uq_username UNIQUE (username);')
        print("Contrainte UNIQUE ajoutée sur le username.")

        conn.commit()
        cur.close()
        conn.close()
        print("\nFix SQL terminé avec succès !")
    except Exception as e:
        print(f"Erreur (ou la contrainte existe déjà) : {e}")

if __name__ == "__main__":
    run_fix()

