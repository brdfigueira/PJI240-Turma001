from .models import Cliente, Demanda, Usuario
from .models import Solicitacao, Anexo
from triagem.models import Pendencia
from advDig.constante import url

def atualizarCliente(cliente):
  print(f"Mandar um email com o link avisando")

def acolherDemanda(demanda, acao):
  if acao == 1:
    print("Mandar um email avisando.")
  if acao == 0:
    print("Mandar um email avisando.")

def solicitaNotificar(solicita_id):
  print(f"Mandar um email com o link avisando.")

def anexoValidado(anexo_id):
  anexo = Anexo.objects.get(pk = anexo_id)
  solicita = anexo.solicitacao
  if not solicita.anexo_set.filter(validado=False).exists():
    solicita.concluida = True
    solicita.save()

def anexoRejeitado(anexo_id):
  print(f"Mandar um email com o link avisando")
