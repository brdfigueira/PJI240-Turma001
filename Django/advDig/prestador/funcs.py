from .models import Cliente, Demanda, Usuario
from triagem.models import Pendencia
from advDig.constante import url

def atualizarCliente(cliente):
  print(f"Mandar um email com o link avisando")

def acolherDemanda(demanda, acao):
  if acao == 1:
    print("Mandar um email avisando.")
  if acao == 0:
    print("Mandar um email avisando.")