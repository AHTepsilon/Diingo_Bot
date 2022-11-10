def defineCategory(input):
    if input == 1:
        return 1
    else:
        return 2


class Responses:

    id = "000000"

    def response(input):
        message = input.lower()
        print(Responses.id)

        if Responses.id == "000000":

            if message == "1":
                Responses.id = "000001"
            
            elif message == "2":
                Responses.id = "000002"
            
            else:
                return '''
                Bienvenido a Semiigo, ¿deseas registrarte o acceder al banco de preguntas? (Escribe en el chat el numero relacionado con tu pregunta)\n
                1. Deseo registrarme\n
                2. Llevame al banco de preguntas'''
        
        elif Responses.id == "000001":
            Responses.id = "000003"
            return '''
            enlace \n
            Cuando hayas terminado la encuesta, escribe "listo" en el chat'''

        elif Responses.id == "000002":
            return '''Bienvenido al banco de preguntas de Semiigo, donde aprenderas lo necesario para comenzar con tus ventas en línea y llevar tu empresa a otro nivel.\n

            Introducir tu empresa a las plataformas digitales y vender por medio de ellas le permitira expansion y reconocimiento. Anímese a comenzar nuestro curso para que pueda desempeñarse en el mundo del e-commerce.\n

            Escribe el número acorde a la pregunta que tengas.\n
                
            1. ¿Como cambio mi nombre en instagram?\n
            2. ¿Como puedo publicar un anuncio en instagram?\n
            3. ¿Como puedo convertir mi cuenta en una cuenta comercial?\n
            4. ¿Como puedo agregar un link de Whatsapp a mi perfil en instagram?\n
            5. ¿Como puedo poner historias destacadas?\n
            6. ¿Como agregar la ubicación del local en mi perfil de instagram?\n
            7. ¿Como puedo aumentar seguidores en instagram?\n
            8. ¿Como ofrecer mis productos a traves de instagram shopping?\n
            9. Mostrar mas preguntas\n
            '''
        
        if point == 2:
            if message == "1":
                return '''1. Ve a tu pagina de perfil y pulsa donde dice “Editar perfil.\n
                2. Una vez en la seccion donde puedes editar tu perfil podras ver un campo llamado “nombre de usuario”. Ahi mismo te deja editarlo.\n
                3. Guarda los cambios efectuados.'''        

            elif message == "2":
                return '''1. Convierte tu perfil en una cuenta comercial. Debes configurar una cuenta comercial para publicar anuncios en Instagram. Este proceso es gratuito y solo debes seguir unos pocos pasos. \n
                2. Elige una foto o un video para tu anuncio. Puedes promocionar una publicacion o una historia que ya compartiste o crear una publicacion o una historia nueva y, luego, promocionarlas. \n
                3. Configura tu promocion. Define el destino, el publico, el presupuesto y la duracion del anuncio. Tienes diferentes opciones para personalizar la promocion a tu manera o puedes usar las opciones automaticas de Instagram para hacerlo mas rapidamente. \n
                4. Publica tu anuncio. Una vez que los anuncios esten listos, toca 'Crear promocion'. Recibiras una notificacion cuando tus anuncios se hayan aprobado y esten listos para ponerse en circulacion.'''

            elif message == "3":
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
            elif message == "4":
                return '''1. Ve a tu perfil de Instagram.\n
                2. Selecciona la opción de “Editar perfil”\n
                3. Selecciona la opción “Enlaces”\n
                4. Selecciona el botón “Agregar enlace externo”\n
                5. Pega tu link de WhatsApp\n
                '''
            
            elif message == "5":
                return '''1. Ve a tu perfil de Instagram\n
                2.Justo debajo de la opción “Editar tu perfil” encontrarás el apartado de “Historias destacadas”\n
                3. Selecciona el botón con el  + que dice “Nueva”\n
                4. A continuación te aparecerán las historias que has subido previamente a tu perfil 
                (Solo te aparecerán las que estuvieron al menos 24H publicadas)\n
                5. Seleccionas las historias que deseas destacar.\n
                '''

            elif message == "6":
                return '''1. Ingresa a tu perfil de instagram\n
                2. Entra al menú que está en la parte de debajo de tu foto de perfil.\n
                3. Haz clic en “Editar perfil”.\n
                4. Luego a “Información comercial pública” y selección “Opciones de contacto”.\n
                5. Después, selecciona el cuadro “Dirección comercial” para que puedas agregar tu ubicación.\n
                6. Completa los espacios en blanco donde te piden dirección, ciudad, código postal y mas.\n
                7. Asegúrate que sea precisa y si ya está segura, selecciona “Listo”.\n
                8. Finalmente, haz clic en “Guardar”.\n
                '''
            
            elif message == "7":
                return '''
                1. Ingresa al administrador de anuncio.s\n
                2. Elige la cuenta publicitaria con la que vas a promocionar tus anuncios.\n
                3. Presiona en la pestaña 'Campañas' y luego en 'Crear'.\n
                4. Elige el objetivo de marketing de tu campaña (alcance, interaccion, conversion, etc.).\n
                5. Define un nombre para tu campaña y haz clic en 'Continuar'.\n
                '''

            elif message == "8":
                return '''
                1. Lunes: 11 am.
                2. Martes y miercoles de 10 am a 1 pm.
                3. Jueves y viernes 10 am a 11 am.
                4. Sabados y domingos 9 am.
                '''
            

 