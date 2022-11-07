import datetime , time
from datetime import datetime as pd
from django import forms


class listando_mis_forms(forms.Form):

    Escuela_Profesional = forms.CharField(label='Escuela Profesional :', max_length=80, widget=forms.TextInput(attrs={'class': 'input_Escuela_Profesional'}))

    Dni = forms.IntegerField(label='DNI :', widget=forms.NumberInput(attrs={'class': 'input_Dni'})) 

    NHC = forms.IntegerField(label='NHC :', widget=forms.NumberInput(attrs={'class': 'input_NHC'})) 
    #####################################################################################

    Apellidos_y_Nombres = forms.CharField(label="Apellidos y Nombres :", widget=forms.TextInput(attrs={'class': 'input_Apellidos_y_Nombres'}))

    Edad = forms.IntegerField(label='Edad :', widget=forms.NumberInput(attrs={'class': 'input_Edad '}))
    Sexo = forms.CharField(label='Sexo :', widget=forms.TextInput(attrs={'class': 'input_Sexo'}))
    Domicilio = forms.CharField(label='Domicilio :', widget=forms.TextInput(attrs={'class': 'input_Domicilio'}))
    Procedencia = forms.CharField(label='Procedencia :', widget=forms.TextInput(attrs={'class': 'input_Procedencia'}))
    Lugar_de_Nacimiento = forms.CharField(label='Lugar de Nacimiento :', widget=forms.TextInput(attrs={'class': 'input_Lugar_de_Nacimiento'}))
    Telefono = forms.IntegerField(label='Telefono :', widget=forms.NumberInput(attrs={'class': 'input_Telefono'}))
    Telefono_de_Familiar = forms.IntegerField(label='Telefono de Familiar :', widget=forms.NumberInput(attrs={'class': 'input_Telefono_de_Familiar'}))
    Religion = forms.CharField(label='Religión :', widget=forms.TextInput(attrs={'class': 'input_Religion'}))

    ######################## Antecedentes Personales ####################
  

   
    CHOICE_ALERGIAS = [('SI', 'SI'), ('NO', 'NO'), ('NO SE', 'NO SE')]
    Alergia_a_Medicamentos = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICE_ALERGIAS)
    CHOICES = [('SI', 'SI'), ('A VECES', 'A VECES'), ('NO', 'NO')]
    

    Habitos_Nocivos_Fuma = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Habitos_Nocivos_Toma_Licor = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Transfuciones_Sanguineas = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    Enfermedades_Infectocontagiosas = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Vacunas_Completas = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Enfermedades_Cronicas = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    Discapacidad = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Accidentes = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Intoxicaciones = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    Cirugia_Hospitalizacion = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Uso_de_Medicamentos = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    Problemas_Psicologicos = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    Especifique = forms.CharField(label='Especifique :', widget=forms.TextInput(attrs={'class': 'input_Especifique'}))
























    day = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={'class': 'inputs_seccion_uno'}))
    hora = forms.DateTimeField(initial=datetime.datetime.today, widget=forms.TextInput(attrs={'class': 'inputs_seccion_uno'}))
    
    now = pd.now()
    #otro = forms.DateField(initial=[hola.hour," : ", hola.minute," : ", hola.second])

    
    otro = forms.DateTimeField(initial=now.strftime("%H:%M:%S"))

    tercero = forms.DateField(initial=time.strftime("%H:%M:%S"))


class BuscarPreinscrito(forms.Form):
    Buscar_por_DNI = forms.IntegerField()
    Buscar_por_numero_de_historia = forms.IntegerField()
    