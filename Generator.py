import secrets
import string

intens = (string.ascii_letters + string.digits)

senha = [secrets.choice(intens)
         for i in range(8)]
senha = ''.join(senha)
print(senha)