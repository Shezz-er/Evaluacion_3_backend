from django.shortcuts import render
from administracion.models import Certificados

def inicio(request):
    return render(request,"index.html")

def ingresar(request):
    return render(request,"ingresar.html")

def registroV(request):

    # Listop
    try:
        id_certE = request.POST['id_certificado']
        nombreE= request.POST['nombre']
        fechaE=request.POST['fecha']
        cursoE=request.POST['curso']
        versionE= request.POST['version']
        id_verE=request.POST['id_verificacion']    

        cert=Certificados.objects.create(id_certificado = id_certE, nombre = nombreE, fecha = fechaE, curso = cursoE, version = versionE, id_verificacion = id_verE)
        return render(request, "respuesta.html",{"msj":f" Se ingresó el certificado con id: {id_certE}, correspondiente a: {nombreE}."})

    except:
        return render(request, "respuesta.html",{"msj":f" Ha ocurrido un error, intente nuevamente."})



def actualizar(request):
    return render(request,"actualizar.html", {"formita": "hidden"})

def editar(request):
    cert = None
    msj = ""
    visibilidad =""
    try:
        id_certE = request.GET['id_certificado']
        cert = Certificados.objects.get(id_certificado = id_certE)
        if id_certE!=None:
            visibilidad = "visible"
            return render(request, "actualizar.html", {"formita":visibilidad, "cert":cert})

        else:
            visibilidad="hidden"
            return render(request, "actualizar.html", {"formita":visibilidad, "cert":cert})

    except:
        cert = None

    if cert==None:
        id_certE = None

        try:
            id_certE = request.POST["id_certificado"]
        except:
            id_certE = None


        if id_certE != None:
            cert = Certificados.objects.get(id_certificado = id_certE)
            nombreE= request.POST['nombre']
            fechaE= request.POST['fecha']
            cursoE = request.POST['curso']
            verE=request.POST['version']
            
            try:
                cert = Certificados.objects.filter(id_certificado = id_certE).update(nombre = nombreE,fecha = fechaE,curso = cursoE, version = verE)
                msj="Se ha actualizado"

            except:
                msj = "Ha ocurrido un error al actualizar"
            
            
            visibilidad="visible"
            return render(request, "actualizar.html", {"msj":msj, "formita":visibilidad})

        else:
            msj = "No se ha encontrado el certificado"
            visibilidad="hidden"
            return render(request, "actualizar.html", {"msj":msj, "formita":visibilidad})
    else:
        msj = 'Error: "No se encontró el Certificado"'
        visibilidad = "hidden"
        return render(request, "actualizar.html", {"msj":msj, "formita":visibilidad})
            
def listarCertificados(request):
    # Listo
    cert = Certificados.objects.all()
    return render(request,"listar.html",{"certificados":cert})

def validar(request):
    return render(request,"validar.html")

def valida(request):
    # Listo
    id_certE = request.POST['id_certificado']
    id_verE=request.POST['id_verificacion'] 
    try:
        c1=Certificados.objects.get(id_certificado=id_certE)
        c2=Certificados.objects.get(id_verificacion=id_verE)
        if c1.id_verificacion==c2.id_verificacion:
            if c1.id_certificado==c2.id_certificado:
                msj='"Credenciales válidas"'
        else:
            msj='Error: "Credenciales inválidas"'

    except:
        msj = 'Error: "Las credenciales no corresponden" '

    return render(request, "respuesta.html",{"msj":msj})

def eliminar(request):
    return render(request,"eliminar.html")

def elimina(request):
    # Listo

    try:
        id_certE = request.POST['id_certificado']
        cert = Certificados.objects.get(id_certificado = id_certE)
        cert.delete()
        msj = "Se ha eliminado exitosamente el certificado"
    except:
         msj = 'Error: "Ingrese credenciales válidas"'
    return render(request, "respuesta.html",{"msj":msj})

