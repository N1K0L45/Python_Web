from django import forms
from elementos.models import *

FILTRO_CHOICES = [
                ('0','-------'),
                ('titulo','Título'),
                ('tituloAlt','Título Alternativo'),
                ('anno','Año'),
                ('director','Director'),
                ('actor','Actor'),
                ('genero','Género')
                ]

FILTRO_ACTORES = [
                ('0','-------'),
                ('nombre','Nombre'),
                ('birth','Fecha de Nacimiento'),
                ('nacion','Nacionalidad')
                ]

class tablaForm(forms.Form):
    filtro = forms.CharField(label="Filtrar por:", widget=forms.Select(choices=FILTRO_CHOICES), required=False)
    f2 = forms.CharField(label="Buscar:",required=False)

class actorForm(forms.Form):
    filtro = forms.CharField(label="Filtrar por:", widget=forms.Select(choices=FILTRO_ACTORES), required=False)
    f2 = forms.CharField(label="Buscar:",required=False)

class directorForm(forms.Form):
    filtro = forms.CharField(label="Filtrar por:", widget=forms.Select(choices=FILTRO_ACTORES), required=False)
    f2 = forms.CharField(label="Buscar:",required=False)

class nuevoForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = [
                'titulo',
                'tituloAlt',
                'anno',
                'director',
                'actor',
                'genero',
                'cover'
                ]

    def __init__(self, *args, **kwargs):
        super(nuevoForm,self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class':'form-control','placeholder':'Ej: Fight Club'})
        self.fields['tituloAlt'].widget.attrs.update({'class':'form-control','placeholder':'Ej: El Club de la Pelea'})
        self.fields['anno'].widget.attrs.update({'class':'form-control', 'value':1888, 'min':1888, 'max':2030})
        self.fields['director'].widget.attrs.update({'class':'form-control','placeholder':'Ej: David Fincher'})
        self.fields['actor'].widget.attrs.update({'class':'form-control','placeholder':'Ej: Edward Norton', 'type':'text'})
        self.fields['genero'].widget.attrs.update({'class':'form-control','placeholder':'Ej: Drama'})
        self.fields['cover'].widget.attrs.update({'class':'form-control', 'placeholder':'Copie link de la fotografía'})

class nuevoDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = [
                'nombre',
                'birth',
                'nacion'
                ]

    def __init__(self, *args, **kwargs):
        super(nuevoDirectorForm,self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class':'form-control', 'placeholder':'Ej: David Fincher'})
        self.fields['birth'].widget.attrs.update({'class':'form-control', 'placeholder':'Formato: aaaa-mm-dd'})
        self.fields['nacion'].widget.attrs.update({'class':'form-control', 'placeholder':'Ej: Mexicano'})

class nuevoActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = [
                'nombre',
                'birth',
                'nacion',
                'foto'
                ]

    def __init__(self, *args, **kwargs):
        super(nuevoActorForm,self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class':'form-control', 'placeholder':'Ej: Edward Norton'})
        self.fields['birth'].widget.attrs.update({'class':'form-control', 'placeholder':'Formato: aaaa-mm-dd'})
        self.fields['nacion'].widget.attrs.update({'class':'form-control', 'placeholder':'Ej: Estadounidense'})
        self.fields['foto'].widget.attrs.update({'class':'form-control', 'placeholder':'Copie link de la fotografía'})
