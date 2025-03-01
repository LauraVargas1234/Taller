Para poder su ejecucion siga los pasos:
1)Verifique que tenga docker y docker compose con los siguientes comandos:
  - docker --version
  - docker-compose --version
  Si las tiene instala continue el proceso.

2) Clone el respositorio ejecutando el siguiente comando:
- https://github.com/LauraVargas1234/Taller.git
  
3) Verifique la rama en la que esta con el comando "git branch",
  en este paso debe quedar en master.

3) Con el repositorio clonado ejecute el siguiente comando para levantar los contenedores:
   - docker compose up -d

Nota: Puedes vetificar que los contenedores esten corriendo con el comando: "docker ps"

5) Posteriormente se puede revisar la salida de la aplicacion en: "http://localhost:5000", ahi encontrara
   los datos de los usuarios creados

   Nota: para agregar nuevos usuarios puede usar el comando:
   curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"id": , "nombre": "", "edad": "", "": ""}'

   Recuerde ingresar todos los campos y ud id diferente a los que ya entan agregados, ya que
   el id es una llave primaria y va a generar un conflicto. Despues refresque y podra ver los usuarios nuevos
