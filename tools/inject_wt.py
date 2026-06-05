import json

with open('F:/Proyectos/tool/main_save.json', encoding='utf-8') as f:
    data = json.load(f)

wt = {
  # Localizar Balcon A
  'arrow_1779768017045_j3nr': 'Cinematica de apertura. Bajar por las escaleras y usar la unica puerta disponible para acceder al pasillo exterior.',
  'arrow_1779768176130_yosd': 'Recorrer el pasillo exterior. Hay una puerta bloqueada desde este lado. Al otro lado, una nota explica la conexion entre zonas exteriores y decks principales.',
  'arrow_1779768284615_nwki': 'Segunda puerta bloqueada sin posibilidad de apertura. La unica salida disponible es la puerta hacia el Balcon.',
  'arrow_1779768381391_fbfd': 'Al final del pasillo: latas de comida y rastro de sangre. Puerta de acceso al Balcon A.',
  'arrow_1779931743989_6o21': 'Llegar al Balcon A. Escalera angosta hacia la zona inferior. Interaccion con el horizonte disponible. Transit al Balcon A del Deck C.',
  'arrow_1779931798987_ed14': 'Mancha de sangre antes de la puerta. Entrar al HallWay A — a partir de aca no hay vuelta atras.',

  # 1ER ENEMIGO y Hallway A
  'arrow_1779768883418_xfdq': 'Primer enemigo al cruzar el umbral: figura en cuclillas, rodeada de sangre y latas. Se abalanza al hacer contacto visual.',
  'arrow_1779768953758_u01x': 'Dos puertas cerradas en el pasillo, senalizadas con carteles de colores y simbolos.',
  'arrow_1779769003484_nh8k': 'Segundo enemigo bloqueando el camino. Ataca directamente al detectar al jugador.',
  'arrow_1779769100753_i76x': 'Al final del pasillo: barricada improvisada como causa del bloqueo.',
  'arrow_1779769178937_su65': 'Primera habitacion cerrada (requiere ganzua). Interior: enemigo comiendo a otro marinero.',

  # Biper y Portafolios
  'arrow_1779926536672_va14': 'Salir de la habitacion de marineros. Recorrer el pasillo despejado hacia la habitacion grande.',
  'arrow_1779771464584_yy7m': 'Habitacion grande: cajonera con cajon bloqueado por candado, escritorio con portafolios (requiere llave), Biper, nota del Biper, muneco. Estado general: caotico.',
  'arrow_1779771618348_8rtl': 'Zona ordenada con cajas de raciones M.E.R.I. Abiertas pero no utilizadas.',

  # SAVE ROOM
  'arrow_1779928029682_265l': 'Nota "Conoce tu rol": explica la distribucion de rangos y accesos dentro del barco.',
  'arrow_1779770722951_e5g4': 'Sala al fondo del pasillo: telegrafo (guardar partida), cajon de almacenamiento, mini-puzzle de caja fuerte, llave de seguridad.',

  # Localizar Deck C
  'arrow_1779929224224_kmoj': 'Todos los elementos necesarios obtenidos. Descender al siguiente piso.',
  'arrow_1779809904422_6zep': 'Bajar al Deck C por la escalera. Usar la llave de seguridad en la puerta de entrada.',
  'arrow_1779810011820_d4ob': 'Primer enemigo estatico en el pasillo central. Se puede esquivar. Puerta lateral bloqueada (requiere llave de mantenimiento).',
  'arrow_1779810079200_8o3f': 'Puerta al fondo del pasillo tambien bloqueada (requiere llave de mantenimiento). Volver mas tarde.',
  'arrow_1779810205539_23a3': 'Unica puerta disponible: lleva al pasillo inundado (Lab Hallway).',

  # Explorar Pasillo inundado
  'arrow_1779810303535_wdhj': 'Pasillo completamente inundado. Puerta doble de laboratorio bloqueada (requiere luz y USB). Enemigo emerge del agua al pasar.',
  'arrow_1779810497793_wogr': 'Segunda puerta bloqueada (requiere luz y tarjeta de acceso).',
  'arrow_1779810568310_uvrq': 'Tercera puerta bloqueada (requiere energia y USB). Otro enemigo emerge del agua.',
  'arrow_1779810626932_j58a': 'Final del pasillo inundado. Continuar hacia el Hallway B.',

  # Visita a la energia
  'arrow_1779810728221_04fo': 'Enemigo distraido en el pasillo. Se activa ante el menor ruido o movimiento.',
  'arrow_1779810912531_uqkt': 'Grupo de cuerpos: marineros y un cientifico. Puerta bloqueada por falta de energia.',
  'arrow_1779811065711_mf2h': 'Nota "El poder de la maquina". Sala de energia bloqueada (requiere ganzua).',
  'arrow_1779811184369_42e9': 'Sala de energia en oscuridad. Enemigo en el interior. Caja de luz saboteada: fusible extraido.',
  'arrow_1779931894044_iore': 'Enemigo golpeandose contra una puerta. Puerta bloqueada (requiere llave de seguridad). Salir al balcon del ala opuesta.',
  'arrow_1779931954059_v0mm': 'Escaleras de regreso al Deck B, ala opuesta.',

  # Storage y Banos
  'arrow_1779812047303_d6k3': 'Cruzar los balcones al Deck B, zona nueva (requiere llave de seguridad). Dos enemigos al entrar: uno comiendo latas, otro estatico.',
  'arrow_1779812167290_rb2i': 'Varias puertas cerradas. Detras de las cajas: puerta al Storage. Cajas M.E.R.I en el ambiente.',
  'arrow_1779812369156_ij3p': 'Almacen casi vacio. Enemigo sentado comiendo de una lata. Nota "Raciones M.E.R.I".',
  'arrow_1779812467143_a3ph': 'Nota "Mapa del Marinera": plano completo del Deck B con distribucion de habitaciones.',
  'arrow_1779812569346_h7l1': 'Bano bloqueado (requiere ganzua), levemente inundado. Enemigo llorando en el interior.',
  'arrow_1779813163582_wazx': 'Dos marineros muertos junto a barricada improvisada. Puerta abierta del otro lado.',

  # El Chef
  'arrow_1779813391661_n1wa': 'Entrar al camarote desde la puerta abierta. Huecos en la pared entre habitaciones. Muralla de muebles improvisada. Enemigo trampa atrapado en ella.',
  'arrow_1779813504926_dqku': 'Pasillo alternativo por los camarotes conecta extremo a extremo, evitando el pasillo principal bloqueado.',
  'arrow_1779813817346_ydpu': 'NPC Adrian (el Chef): herido gravemente. Solicita escapar y activar el scuttle. Decision: dejarlo morir o ejecutarlo. Drop: fusible de la sala electrica + nota con codigo en morse.',

  # PUZZLE MENTE y SAVE ZONE
  'arrow_1779814129482_h00e': 'Regresar por el ala B completa hasta la sala de energia en el Deck C.',
  'arrow_1779814372007_t8cs': 'Insertar el fusible en la caja de luz. Resolver puzzle de palancas para restaurar la energia.',
  'arrow_1779817028477_jqhg': 'Sala desbloqueada por la energia: telegrafo (guardar partida), cajon de almacenamiento, llave de mantenimiento.',

  # GATO y TARJETA
  'arrow_1779817447680_xw4j': 'Sala de bombas de agua (llave de mantenimiento). Sistema de manivelas en orden desconocido. Tarjeta de acceso encontrada en la sala.',
  'arrow_1779817575851_cfe8': 'Sala "Santuario" (requiere ganzua). Interior: altar dedicado a un gato.',
  'arrow_1779817704951_8jtu': 'Oficina (llave de mantenimiento). Escritorios y archiveros. Contenido pendiente de definir.',
  'arrow_1779817834836_ne63': 'Sin mas para explorar en el Deck C. Subir al Deck B.',
  'arrow_1779817956150_9lcv': 'De regreso en el Deck B: uno de los enemigos eliminados antes ha revivido.',

  # Diario y Muneco
  'arrow_1779986017999_1wpk': 'Lavadero (llave de mantenimiento). Hueco en el piso inundado por caneria rota. Diario del ingeniero con instrucciones sobre el orden de las manivelas.',
  'arrow_1779986064418_5u4q': 'Cajon del chef bloqueado por candado (resolver codigo del morse). Dentro: muneco de forma peculiar.',
  'arrow_1779986101567_dkou': 'Sin mas para explorar en el ala. Bajar al Deck C para activar la bomba de agua.',

  # PUZZLE CUERPO y DIORAMA
  'arrow_1779818683143_0w2k': 'Enemigo revivido bloqueando el camino.',
  'arrow_1779818829987_nhid': 'Resolver el puzzle de manivelas usando el diario del ingeniero. Las canerias se normalizan y el agua del pasillo se drena.',
  'arrow_1779819010157_gk3d': 'Pasillo drenado. Porton accesible con tarjeta de acceso. Sala interior con diorama incompleto. Enemigo revivido en la zona.',

  # CAMAROTES y RADIO
  'arrow_1779987377117_zc96': 'Volver al Deck C. Varios enemigos revividos en el camino.',
  'arrow_1779819320440_iydv': 'Bano del ala B: ya sin agua. Llave encontrada dentro de un inodoro.',
  'arrow_1779819432059_j9d7': 'Sala de radio (llave de mantenimiento). Recibe mensajes, no los envia. Reproducir grabaciones guardadas. Nota "Registro de Radio".',
  'arrow_1779819594229_p79h': 'Camarote del capitan (llavero de camarotes). Enemigo en la cama. Llave pequena (para candado del portafolios). Ropa interior femenina en el piso.',

  # Bloqueo y Atajo
  'arrow_1779819667610_uff0': 'Puerta de salida atascada permanentemente. Usar el llavero de camarotes para continuar.',
  'arrow_1779819784752_qjfy': 'Comedor (llavero de camarotes): cuerpos, muebles volteados, comida desperdigada. Dos enemigos en el interior.',
  'arrow_1779819917212_8jys': 'Cocina: dos enemigos cocineros. Un enemigo sentado. Puerta interna bloqueada (llavero de camarotes).',
  'arrow_1779819999580_6rta': 'Almacen de cocina: bloque de cuchillos vacio, los cuchillos fueron retirados.',
  'arrow_1779820059450_cx6e': 'Abrir la puerta del inicio del Deck B (antes bloqueada de un lado). Atajo habilitado de regreso al inicio.',

  # Crimson Draft
  'arrow_1779820234926_3dge': 'Dormitorio de marineros (llavero de camarotes). Dos enemigos: uno estatico al centro, uno trampa dentro del armario.',
  'arrow_1779820282373_psqm': 'Reunir los componentes del diorama. Descender al Deck C.',
  'arrow_1779820413497_50e1': 'Completar el diorama. Obtener documento sobre los sucesos + USB. Boss: Vanessa. Puerta final desbloqueada con USB.',
}

count = 0
for step in data['steps']['steps']:
    for arrow in step.get('arrows', []):
        if arrow['id'] in wt:
            arrow['walkthrough_text'] = wt[arrow['id']]
            count += 1

with open('F:/Proyectos/tool/main_save.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Done. {count} arrows updated.')
