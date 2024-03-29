START_CMD_USER = "Hola! Te puedo ayudar a tomar responsablemente con tu grupo de amigos, " \
                 "por favor añádeme a un grupo para comenzar"
START_CMD_GROUP = "Hola! Los voy a ayudar a tomar responsablemente :D"
START_CMD_CHANNEL = "Hola! De verdad no sé como me añadiste a un canal, " \
                    "pero necesito estar en un grupo para funcionar"
START_REPEATED = "Ya me han empezado en este grupo c:"
HELP_CMD = 'Hola, soy BotRacho Responsable y los ayudaré a ser responsables al volante, ' \
           'conmigo pueden usar éstos comandos:' \
           '/help: Muestra este diálogo de información' \
           '/gradosInfluencia: Muestra cuántos grados son "estar bajo la influencia del alcohol"' \
           ' y cuántos tragos también' \
           '/gradosEbriedad: Muestra cuántos grados son "estar en estado de ebriedad"' \
           ' y cuántos tragos también' \
           '/sanciones: Muestra las sanciones por conducir con alcohol en la sangre' \
           '/datoCurioso: Entrega un dato curioso sobre el alcohol por minuto' \
           'Los siguientes comandos solo pueden ser usados en grupos:' \
           '/designarConductor: Empieza un sorteo para elegir un conductor designado' \
           '/yoManejo: Te añade al sorteo de conductor designado' \
           '/elegirConductor: Define el conductor designado entre los que se añadieron, ' \
           'solo lo puede usar quién partió el sorteo' \
           '/reclamosALaFifa: Muestra la información del último sorteo, por si quieren verificarlo independientemente'

ESTADO_INFLUENCIA = "Bajo la influencia del Alcohol:\n" \
                    "0,3 e inferior a 0,8 g/ml.\n" \
                    "Equivalencia en Tragos:\n" \
                    "150 ml de Vino o Champaña de 12° (1 copa)\n" \
                    "350 ml de Cerveza (1 Lata)\n" \
                    "75 ml de Piscola (0.5 Vasos)\n" \
                    "400 ml de Terremoto (2 vasos)*\n" \
                    "45 ml de Brandy de 38°\n" \
                    "* Valor válido para mujer\n" \
                    "** Equivalencia calculada para una mujer de 55Kg y un hombre de 70Kg.\n" \
                    "*** 1 vaso equivale a 200 ml"

ESTADO_EBRIEDAD = "Estado de ebriedad:\n" \
                  "Mayor a 0,8 g/ml\n" \
                  "Equivalencia en Tragos:\n" \
                  "300 ml de Vino o Champaña de 12° (1 copa)\n" \
                  "600 ml de Cerveza (1 Lata)\n" \
                  "150 ml de Piscola (0.5 Vasos)\n" \
                  "800 ml de Terremoto (2 vasos)*\n" \
                  "90 ml de Brandy de 38°\n" \
                  "* Valor valido para mujer\n" \
                  "** Equivalencia calculada para una mujer de 55Kg y un hombre de 70Kg.\n" \
                  "*** 1 vaso equivale a 200 ml"

SANCIONES_MSG = "Éstas son las sanciones por manejar con alcohol, por favor sean responsables"
SANCIONES_URI = "/resources/SancionesLeyToleranciaCero.jpg"

CURIOUS_FACT_MSG = "Dato curioso del minuto:"

REQUEST_DRIVERS_MSG = "Vamos a designar conductor: los que manejen digan /yoManejo\n" \
                      "Cuando todos los conductores estén, que {0} diga /elegirConductor\n" \
                      "Conductores anotados:"
ADDED_DRIVER_MSG = "{0} puede conducir"

DESIGNATED_DRIVER_MSG = "Y el conductor designado es {0}"
