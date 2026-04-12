from app import app, db
from sqlalchemy import text

def add_column():
    with app.app_context():
        try:
            # Utilisation de "user" avec des guillemets pour éviter l'erreur de syntaxe
            # Note : On utilise des doubles guillemets pour le nom de la table
            query = text('ALTER TABLE "user" ADD COLUMN profile_image VARCHAR(255) DEFAULT \'default.png\'')
            db.session.execute(query)
            db.session.commit()
            print("✅ Colonne 'profile_image' ajoutée avec succès !")
        except Exception as e:
            db.session.rollback()
            print(f"⚠️ Erreur : {e}")

if __name__ == "__main__":
    add_column()

