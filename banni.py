from app import app, db, User

USERNAME = "finir"  # Remplace par le nom d'utilisateur à bannir

with app.app_context():
    user = User.query.filter_by(username=USERNAME).first()

    if not user:
        print(f"❌ Utilisateur '{USERNAME}' introuvable.")
    else:
        user.premier_depot = True
        db.session.commit()
        print(f"✅ L'utilisateur '{USERNAME}' a été banni avec succès.")
