from app import app, db
from sqlalchemy import text

with app.app_context():
    # Attention : si ta table s'appelle "retrait" au singulier
    db.session.execute(text('ALTER TABLE "retrait" ADD COLUMN type_retrait VARCHAR(20)'))
    db.session.commit()
    print("✅ Colonne type_retrait ajoutée !")

