from django.shortcuts import render, redirect
from .forms import listando_mis_forms, BuscarPreinscrito
from .models import pre_registro_paciente
from django.contrib import messages

# Create your views here.



def index_dos(request):
    if request.method == 'GET':
        
        """
        print(request.GET['Escuela_Profesional'])
        print(request.GET["Dni"])
        print(request.GET["NHC"])
        print(request.GET["Apellidos_y_Nombres"])
        print(request.GET["Edad"])
        print(request.GET["Sexo"])
        print(request.GET["Domicilio"])
        print(request.GET["Procedencia"])
        
        print(request.GET["Lugar_de_Nacimiento"])
        print(request.GET["Telefono"])
        print(request.GET["Telefono_de_Familiar"])
        print(request.GET["Religion"])

        """


        return render(request, "index.html",{
            "form": listando_mis_forms()
        })
    else:
        #print("hola")

        array_a = []
        array_b = []

    ########### a insertar en la columna DatosGenerales ###########

        print(request.POST['Escuela_Profesional'])
        print(request.POST["Dni"])
        print(request.POST["NHC"])
        print(request.POST["Apellidos_y_Nombres"])
        print(request.POST["Edad"])
        print(request.POST["Sexo"])
        print(request.POST["Domicilio"])
        print(request.POST["Procedencia"])
        print(request.POST["Lugar_de_Nacimiento"])
        print(request.POST["Telefono"])
        print(request.POST["Telefono_de_Familiar"])
        print(request.POST["Religion"])

        array_a.append([request.POST['Escuela_Profesional'], 
                        request.POST["Dni"],
                        request.POST["NHC"],
                        request.POST["Apellidos_y_Nombres"],
                        request.POST["Edad"],
                        request.POST["Sexo"],
                        request.POST["Domicilio"],
                        request.POST["Procedencia"],
                        request.POST["Lugar_de_Nacimiento"],
                        request.POST["Telefono"],
                        request.POST["Telefono_de_Familiar"],
                        request.POST["Religion"]                   
                        ])
        print("el array_a es :",array_a )

        array_b.append([request.POST['Alergia_a_Medicamentos'],
                        request.POST['Habitos_Nocivos_Fuma'],
                        request.POST['Habitos_Nocivos_Toma_Licor'],
                        request.POST['Transfuciones_Sanguineas'],
                        request.POST['Enfermedades_Infectocontagiosas'],
                        request.POST['Vacunas_Completas'],
                        request.POST['Enfermedades_Cronicas'],
                        request.POST['Discapacidad'],
                        request.POST['Accidentes'],

                        request.POST['Intoxicaciones'],
                        request.POST['Cirugia_Hospitalizacion'],
                        request.POST['Uso_de_Medicamentos'],
                        request.POST['Problemas_Psicologicos'],
                        request.POST['Especifique'],
        ])
        print("el array_b es :",array_b )
# inserto el array en la primera columana
        

        # inserto el segundo array(array_b) en la segunda columna de la tabla 
        pre_registro_paciente.objects.create(AntecedentesPersonales = array_b, DatosGenerales = array_a ) 

        #pre_registro_paciente.objects.create()
        return redirect('/')


def Buscar_preinscrito(request):
    if request.method == 'GET':

        

        return render(request, "buscar_preinscritos.html",{
            "form": BuscarPreinscrito()
        })
        
    else:
        print(request.POST['Buscar_por_DNI'])
        print(request.POST['Buscar_por_numero_de_historia'])

        if (int(request.POST['Buscar_por_DNI']) > 1 and int(request.POST['Buscar_por_numero_de_historia']) > 1):
            messages.error(request, "No puede buscar con ambos a la vez, utilice solo un campo a la vez")
        
        return redirect('/')
        
        
        


    



    pass

     
    
 
