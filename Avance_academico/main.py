##Menu
def main():
    main_menu_options = int(input("Quieres acceder a:\n1. Avance de carrera.\n2. Materias Disponibles.\n3. Anadir materia de avance.\n4. Editar Malla.\n"))
    return main_menu_options

## Crear lista de codigos para revisar que no se repitan si su length es 2.

##Confirmar si la lista de materias fue ingresada correctamente. si no, preguntar por la materia que se puso mal y registrarla de nuevo.

def plan_curricular(value):

    if value == 1:
        with open("materias_semestre.csv", "w") as writer:
            for i in range(1,num_semestres+1):
                count = 0
                number_mat = int(input("Cuantas materias vas a ver?"))
                while count < number_mat:
                    name_ = input("Nombre:\n")
                    id_ = input("Id:\n")
                    credits_ = input("Creditos:\n")
                    writer.write(str(i)+","+name_+","+id_+","+credits_+"\n")
                    count += 1
        writer.close()

    else:
        with open("requisitos_.csv", "w") as writer:
            for i in range (1,9):
                id_faltante = 1
                req_semestre = int(input(f"Para el semestre {i} hay requisitos?\n1. Si.\n2. No.\n"))
                if req_semestre == 1:
                    while id_faltante != 0:
                        id_base = input("Id:\n")
                        id_faltante = int(input("Id requerida:\n"))
                        writer.write(id_base+","+str(id_faltante)+"\n")
        writer.close()


if main() == 4:
    plan_curricular_menu = int(input("1. Asignacion de materias\n2. Asignacion de requisitos.\n"))
    plan_curricular(plan_curricular_menu)



##Funcion Avance.

##Lista que contiene los id_ cursados.

##Funcion Materias Disponibles.

##Se toma la lista de requisitos y la lista de id_ cursados para saber que materias pueden estar disponibles.

##Funcion Plan_curricular

##Vamos a crear por semestre un bloque.

##Edicion por semestre.

##Funcion Edicion avance.