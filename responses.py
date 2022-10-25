def response(input):
    message = input.lower()
    
    if "cambio" in message:
        return '''1. Ve a tu pagina de perfil y pulsa donde dice “Editar perfil.\n
        2. Una vez en la seccion donde puedes editar tu perfil podras ver un campo llamado “nombre de usuario”. Ahi mismo te deja editarlo.\n
        3. Guarda los cambios efectuados.'''        

    elif "anuncio" in message:
        return '''1. Convierte tu perfil en una cuenta comercial. Debes configurar una cuenta comercial para publicar anuncios en Instagram. Este proceso es gratuito y solo debes seguir unos pocos pasos. \n
        2. Elige una foto o un video para tu anuncio. Puedes promocionar una publicacion o una historia que ya compartiste o crear una publicacion o una historia nueva y, luego, promocionarlas. \n
        3. Configura tu promocion. Define el destino, el publico, el presupuesto y la duracion del anuncio. Tienes diferentes opciones para personalizar la promocion a tu manera o puedes usar las opciones automaticas de Instagram para hacerlo mas rapidamente. \n
        4. Publica tu anuncio. Una vez que los anuncios esten listos, toca 'Crear promocion'. Recibiras una notificacion cuando tus anuncios se hayan aprobado y esten listos para ponerse en circulacion.'''

    elif "cuenta comercial" in message:
        return '''1. Ve a tu perfil y toca Menu en la esquina superior derecha.\n
        2. Toca Configuracion.\n
        3. En el caso de algunas cuentas, la opcion Cambiar a cuenta profesional aparecerá en la lista debajo de Configuracion.\n
        4. Toca Cuenta.\n
        5. Toca Cambiar a cuenta profesional.\n
        6. Toca Continuar.\n
        7. Selecciona una categoria para tu empresa y toca Listo.\n
        8. Toca Aceptar para confirmar.\n
        9. Toca Empresa.\n
        10. Toca Siguiente.\n
        11. Agrega tu informacion de contacto y, luego, toca Siguiente. O toca No usar mi informacion de contacto para omitir este paso.\n
        12. Si lo deseas, puedes seguir estas instrucciones para conectar tu cuenta comercial a una pagina de Facebook asociada a tu empresa. Este paso, que es opcional, facilita el uso de todas las funciones disponibles para las empresas en la familia de apps de Facebook. Por el momento, solo es posible conectar una pagina de Facebook a una cuenta comercial.\n
        13. Pulsa la X en la esquina superior derecha para regresar a tu perfil.\n
        '''
 