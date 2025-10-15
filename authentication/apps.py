from django.apps import AppConfig
import os

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self):
        from django.contrib.auth import get_user_model
        try:
            if os.environ.get("CREATE_SUPERUSER") == "True":
                User = get_user_model()
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser(
                        username="admin",
                        email="admin@example.com",
                        password="Admin@123"
                    )
                    print("✅ Superuser 'admin' created successfully.")
        except Exception as e:
            print(f"⚠️ Superuser creation skipped: {e}")
