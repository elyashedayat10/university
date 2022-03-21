from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, family, national_code, password):
        if not national_code:
            raise ValueError("This Field Is Required")
        user = self.model(name=name, family=family, national_code=national_code)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, family, national_code, password):
        user = self.create_user(name=name, family=family, national_code=national_code, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
