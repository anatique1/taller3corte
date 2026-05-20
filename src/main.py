from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorEmail, SuscriptorSMS

# Crear canal
canal = CanalNoticias("Noticias1")

# Crear suscriptores
ana = SuscriptorEmail("Ana")
maria = SuscriptorSMS("Maria")

# Suscribir
canal.suscribir(ana)
canal.suscribir(maria)

# Publicar mensaje
canal.publicar("noticia importante")

# Mostrar mensajes recibidos
print(ana.mensajes)
print(maria.mensajes)