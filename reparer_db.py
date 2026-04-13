from app import app, db
from sqlalchemy import text

def fix_constraints():
    with app.app_context():
        try:
            print("🚀 Tentative de suppression des contraintes bloquantes...")
            
            # Commande SQL pour faire sauter la contrainte username avec CASCADE
            # Cela permet de supprimer les liens qui empêchent Alembic de travailler
            query = text('ALTER TABLE "user" DROP CONSTRAINT IF EXISTS user_username_key CASCADE;')
            
            db.session.execute(query)
            db.session.commit()
            
            print("✅ Contrainte supprimée avec succès (CASCADE).")
            print("👉 Tu peux maintenant relancer : flask db upgrade")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Erreur : {str(e)}")

if __name__ == "__main__":
    fix_constraints()

