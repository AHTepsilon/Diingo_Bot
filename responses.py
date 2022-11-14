from user import User

class Responses:

    id = "000000"
    controlBoolean = True
    us = ""

    def response(self, input):
        message = input.lower()
        print(Responses.id)

        if Responses.id == "000004":
            message = ""

        if Responses.id == "000000":

            if "1" in message:
                Responses.id = "000001"
                Responses.us = User("user")
            
            elif "2" in message:
                Responses.id = "000002"
            
            else:
                return '''
                Bienvenido a Semiigo, para comunicarte con el bot, usaremos un sistema de codigos, en algunos casos se te pedira que respondas con numeros (1, 2, 3) o con afirmaciones y negaciones (s, n)\n
                Unicamente necesitas escribir el numero o caracter para tu solicitud y esperar la respuesta del bot \n
                ¿Que deseas hacer? \n
                1. Deseo registrarme\n
                2. Llevame al banco de preguntas'''
        
        elif Responses.id == "000001":
            Responses.id = "000003"
            return '''
            Empezaremos con las preguntas de categorizacion. De esta forma personalizaremos el curso a tu medida y te daremos la informacion que sea mas relevante para ti\n
            En esta primera etapa, se te haran 15 preguntas de estandarizacion (duracion 10 minutos) mediante las cuales ajustaremos los cursos y pildoras de informacion a tu medida \n
            Cargando preguntas, por favor espera...\n'''

        elif Responses.id == "000002":
            return '''Bienvenido al banco de preguntas de Semiigo, donde aprenderas lo necesario para comenzar con tus ventas en linea y llevar tu empresa a otro nivel.\n

            Introducir tu empresa a las plataformas digitales y vender por medio de ellas le permitira expansion y reconocimiento. Animese a comenzar nuestro curso para que pueda desempeniarse en el mundo del e-commerce.\n

            Escribe el numero acorde a la pregunta que tengas.\n
                
            1. ¿Como cambio mi nombre en instagram?\n
            2. ¿Como puedo publicar un anuncio en instagram?\n
            3. ¿Como puedo convertir mi cuenta en una cuenta comercial?\n
            4. ¿Como puedo agregar un link de Whatsapp a mi perfil en instagram?\n
            5. ¿Como puedo poner historias destacadas?\n
            6. ¿Como agregar la ubicacion del local en mi perfil de instagram?\n
            7. ¿Como puedo aumentar seguidores en instagram?\n
            8. ¿Como ofrecer mis productos a traves de instagram shopping?\n
            9. Mostrar mas preguntas\n
            '''
        
        elif Responses.id == "000003":

            if Responses.controlBoolean:
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000004"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000004"
                    Responses.controlBoolean = False
                else:
                    return '''Mis ventas son principalmente por medios fisicos (S/N) \n'''
            else:
                message = ""
                Responses.controlBoolean = True
        
        elif Responses.id == "000004":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000005"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000005"
                    Responses.controlBoolean = False
                else:
                    return '''Tengo Conocimiento sobre plataformas de venta en linea (S/N) \n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Tengo Conocimiento sobre plataformas de venta en linea (S/N) \n'''

        elif Responses.id == "000005":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000006"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000006"
                    Responses.controlBoolean = False
                else:
                    return '''Realizo facturacion por cuenta propia, no hago uso de herramientas externas de terceros (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Realizo facturacion por cuenta propia, no hago uso de herramientas externas de terceros (S/N) \n'''

        elif Responses.id == "000006":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000007"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000007"
                    Responses.controlBoolean = False
                else:
                    return '''Tengo una estrategia solida de ventas que he sido capaz de implementar por mas de 1 anio de manera constante (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Tengo una estrategia solida de ventas que he sido capaz de implementar por mas de 1 anio de manera constante (S/N) \n'''
                
            
        elif Responses.id == "000007":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000008"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000008"
                    Responses.controlBoolean = False
                else:
                    return '''Interactuo a menudo con clientes a traves de mis redes sociales (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Interactuo a menudo con clientes a traves de mis redes sociales (S/N) \n'''
            
        elif Responses.id == "000008":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000009"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000009"
                    Responses.controlBoolean = False
                else:
                    return '''Tengo conocimiento de como crear una cuenta de instagram y convertirla a modo profesional (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Tengo conocimiento de como crear una cuenta de instagram y convertirla a modo profesional (S/N) \n'''
                
        elif Responses.id == "000009":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000010"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000010"
                    Responses.controlBoolean = False
                else:
                    return '''Se como crear publicidad para mi negocio en Facebook, Instagram y Google (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Se ccmo crear publicidad para mi negocio en Facebook, Instagram y Google (S/N) \n'''

        elif Responses.id == "000010":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000011"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000011"
                    Responses.controlBoolean = False
                else:
                    return '''Se como ver las estadisticas de mis publicaciones en redes sociales para revisar el engagement de estas (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Se como ver las estadisticas de mis publicaciones en redes sociales para revisar el engagement de estas (S/N) \n'''

        elif Responses.id == "000011":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000012"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000012"
                    Responses.controlBoolean = False
                else:
                    return '''Mis ganancias provienen en su mayoria de compras en medios digitales (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Mis ganancias provienen en su mayoria de compras en medios digitales (S/N) \n'''

        elif Responses.id == "000012":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000013"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000013"
                    Responses.controlBoolean = False
                else:
                    return '''Se como cambiar mi cuenta de Whatsapp a modo Business para asi tener control de mi negocio a traves de la App de mensajeria (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Se como cambiar mi cuenta de Whatsapp a modo Business para asi tener control de mi negocio a traves de la App de mensajeria (S/N) \n'''

        elif Responses.id == "000013":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000014"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000014"
                    Responses.controlBoolean = False
                else:
                    return '''Manejo un catalogo de mis productos en Whatsapp e Instagram (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Manejo un catalogo de mis productos en Whatsapp e Instagram (S/N) \n'''
                
        elif Responses.id == "000014":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000015"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000015"
                    Responses.controlBoolean = False
                else:
                    return '''Tengo conocimientos en el area de ventas y administracion de negocios  (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Tengo conocimientos en el area de ventas y administracion de negocios (S/N) \n'''

        elif Responses.id == "000015":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000016"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000016"
                    Responses.controlBoolean = False
                else:
                    return '''Tengo mi propia pagina web para realizar ventas ademas de mis redes sociales  (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Tengo mi propia pagina web para realizar ventas ademas de mis redes sociales (S/N) \n'''

        elif Responses.id == "000016":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000017"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000017"
                    Responses.controlBoolean = False
                else:
                    return '''Manejo envios para mis productos de manera organizada y efectiva (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Manejo envios para mis productos de manera organizada y efectiva (S/N) \n'''

        elif Responses.id == "000017":

            if Responses.controlBoolean:
                message = input.lower()
                if message == "s" or message == "si" or message == "si":
                    Responses.id = "000018"
                    Responses.controlBoolean = False
                elif message == "n" or message == "no":
                    Responses.id = "000018"
                    Responses.controlBoolean = False
                else:
                    return '''Me considero una persona activa en redes sociales, constantemente gano seguidores (S/N)\n'''
            else:
                message = ""
                Responses.controlBoolean = True  
                return '''Me considero una persona activa en redes sociales, constantemente gano seguidores (S/N) \n'''

        elif Responses.id == "000018":
            Responses.id = "000020"
            return '''Gracias por tus respuestas, tu perfil ha sido guardado en nuestra base de datos \n
            Segun la base de datos, has sido clasificado en el nivel bronce, por lo cual ajustaremos tus condiciones y personalizaremos las lecciones que recibes de tal forma que sea acordes a ti \n
            Estas listo para empezar el curso, puedes elegir cuando desees iniciar \n
            Puedes empezar el curso ahora, o puedes volver luego para empezar\n
            ¿Que te gustaria hacer? \n
            1. Empezar ahora
            2. Empezar despues'''
        
        elif Responses.id == "000020":
            if message == "1":
                Responses.id = "000021"
            elif message == "2":
                Responses.id = "999999"
        
        elif Responses.id == "000021":
            return '''
            Ya ha pasado aquel momento en que Instagram era solo una red para publicar fotos de viajes en la playa, un cafe delicioso en un bar o una selfie con un paisaje de fondo. Hoy Instagram se ha transformado en una plataforma de negocios donde puedes vender diversos productos y servicios. \n
            
            Con mas de mil millones de usuarios activos cada mes, era de esperar que Instagram se convirtiera en el lugar perfecto para promocionar y vender productos. \n
            
            De hecho, 15 millones de empresas latinoamericanas tienen un perfil en instagram y el 80% de los usuarios sigue por lo menos a una de estas marcas. \n
            
            Estos datos no dejan lugar a dudas: vender en Instagram puede hacer despegar tu negocio. Y ademas de aumentar las ventas, tambien puedes acercarte a tu publico objetivo. \n
            
            Sin embargo, aun siendo un canal tan eficiente y atractivo, muchas personas y marcas aun no saben como vender a traves de la red social.\n
            
            Te presentamos un video que te puede ayudar: https://www.instagram.com/reel/CkwMOTvv0mt/?igshid=MDJmNzVkMjY= \n'''
        
        elif Responses.id == "000022":
            return '''
            Un reel en Instagram es una herramienta propia de la plataforma social que permite a los usuarios crear videos cortos. Contiene funciones de grabacion y edicion, asi como efectos, stickers, audio, musica, entre otras mas. La duracion de los contenidos puede ir desde 15 a 60 segundos.  \n
            
            Reel en Instagram no solo es una herramienta de grabacion y edicion de videos, sino que tambien funge como un espacio de descubrimiento dentro de la misma red social para encontrar contenido afin a los gustos e intereses de cada usuario.\n
            
            Te presentamos un video que te puede ayudar: https://www.instagram.com/reel/CQjTZTppxay/?utm_source=ig_web_copy_link \n'''
        
        elif Responses.id == "000023":
            return '''
            En pocas palabras: si tu publico objetivo esta ya en Instagram y tienes la disposicion de invertir algo de tiempo y recursos en crear un contenido especialmente para ellos, entonces la respuesta es si. Aprender como manejar Instagram puede ayudarte a expandir tu negocio.\n
            
            Vamos a analizarlo mas detenidamente. Lo primero es saber que Instagram es un canal visual. Si te pasas el dia haciendo fotos interesantes o tus fantasticos productos son aptos para Instagram, es decir, de los que entran por los ojos, esta es la plataforma idonea para ti. Piensalo de la siguiente manera: si eres una marca que vende directamente al usuario, te dedicas a la fotografia, eres artista, blogger o un genio de las manualidades, significa que ya tienes un monton de material para enseniar. Con Instagram, puedes aprovecharte del contenido visual que ya tienes para ampliar tu clientela y conectar con mas clientes potenciales online.\n
            
            Te presentamos un video que te puede ayudar: https://www.instagram.com/reel/CkzDDz1p89g/?igshid=YmMyMTA2M2Y= \n'''
        
        elif Responses.id == "000024":
            return '''
            Aunque Instagram es todo visual, seria imprudente no utilizar su funcionalidad de texto. Puedes acompaniar unas buenas fotos o videos con storytelling, contando una historia sobre como decidiste crear tu producto o lanzar el negocio. Tambien puedes responder las preguntas mas frecuentes de tu publico o hablar de los procesos internos de tu negocio.\n
            
            La gente le compra a la gente. Cuenta a tu audiencia las historias que les permitiran conocer a tu marca y tal vez a ti. No te limites a la descripcion dura del producto y el precio.\n
            
            Te presentamos un video que te puede ayudar: https://www.instagram.com/reel/Ckq0nE8M0vl/?igshid=YmMyMTA2M2Y= \n'''


        elif Responses.id == "999999":
            return '''Te esperamos en tu proxima leccion. Nos vemos! \n'''

        elif Responses.id == "900000":
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
                3. En el caso de algunas cuentas, la opcion Cambiar a cuenta profesional aparecera en la lista debajo de Configuracion.\n
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
                2. Selecciona la opcion de “Editar perfil”\n
                3. Selecciona la opcion “Enlaces”\n
                4. Selecciona el boton “Agregar enlace externo”\n
                5. Pega tu link de WhatsApp\n
                '''
            
            elif message == "5":
                return '''1. Ve a tu perfil de Instagram\n
                2.Justo debajo de la opcion “Editar tu perfil” encontraras el apartado de “Historias destacadas”\n
                3. Selecciona el boton con el  + que dice “Nueva”\n
                4. A continuacion te apareceran las historias que has subido previamente a tu perfil 
                (Solo te apareceran las que estuvieron al menos 24H publicadas)\n
                5. Seleccionas las historias que deseas destacar.\n
                '''

            elif message == "6":
                return '''1. Ingresa a tu perfil de instagram\n
                2. Entra al menu que esta en la parte de debajo de tu foto de perfil.\n
                3. Haz clic en “Editar perfil”.\n
                4. Luego a “Informacion comercial publica” y seleccion “Opciones de contacto”.\n
                5. Despues, selecciona el cuadro “Direccion comercial” para que puedas agregar tu ubicacion.\n
                6. Completa los espacios en blanco donde te piden direccion, ciudad, codigo postal y mas.\n
                7. Asegurate que sea precisa y si ya esta segura, selecciona “Listo”.\n
                8. Finalmente, haz clic en “Guardar”.\n
                '''
            
            elif message == "7":
                return '''
                1. Ingresa al administrador de anuncio.s\n
                2. Elige la cuenta publicitaria con la que vas a promocionar tus anuncios.\n
                3. Presiona en la pestania 'Campanias' y luego en 'Crear'.\n
                4. Elige el objetivo de marketing de tu campania (alcance, interaccion, conversion, etc.).\n
                5. Define un nombre para tu campania y haz clic en 'Continuar'.\n
                '''

            elif message == "8":
                return '''
                1. Lunes: 11 am.
                2. Martes y miercoles de 10 am a 1 pm.
                3. Jueves y viernes 10 am a 11 am.
                4. Sabados y domingos 9 am.
                '''
            

 