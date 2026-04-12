from app import app, db
from sqlalchemy import text

def create_indexes():
    with app.app_context():
        # Liste des commandes SQL à exécuter
        commands = [
            'CREATE INDEX IF NOT EXISTS ix_user_username ON "user" (username)',
            'CREATE INDEX IF NOT EXISTS ix_user_phone ON "user" (phone)',
            'CREATE INDEX IF NOT EXISTS ix_user_email ON "user" (email)',
            'CREATE INDEX IF NOT EXISTS ix_user_solde_revenu ON "user" (solde_revenu)'
        ]
        
        for cmd in commands:
            try:
                db.session.execute(text(cmd))
                print(f"Succès : {cmd}")
            except Exception as e:
                print(f"Erreur sur {cmd} : {e}")
        
        db.session.commit()
        print("Terminé !")

if __name__ == "__main__":
    create_indexes()

