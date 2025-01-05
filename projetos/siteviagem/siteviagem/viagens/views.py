from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import urlencode
from django.core.paginator import Paginator
from .models import Viagem, Passageiro, GastoExtra
from .forms import GastoExtraForm
from datetime import datetime


def index(request):
    viagens_ativas = Viagem.objects.filter(excluida=False)
    busca_motorista = request.GET.get("nome_motorista", "")
    data_inicio = request.GET.get("data_inicio", None)
    data_fim = request.GET.get("data_fim", None)

    viagens_ativas = Viagem.objects.all()

    if busca_motorista:
        viagens_ativas = Viagem.objects.filter(
            nome_motorista__icontains=busca_motorista, excluida=False
        )
    else:
        viagens_ativas = Viagem.objects.filter(excluida=False)

    if data_inicio:
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
        viagens_ativas = viagens_ativas.filter(horario__gte=data_inicio)
    if data_fim:
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d")
        viagens_ativas = viagens_ativas.filter(horario__lte=data_fim)

    page_number = request.GET.get("page", 1)
    paginator = Paginator(viagens_ativas, 3)
    page_obj = paginator.get_page(page_number)

    context = {
        "viagens_ativas": page_obj,
        "busca_motorista": busca_motorista,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }

    return render(request, "viagens/index.html", context)


def detalhes_viagem(request, id):
    viagem = get_object_or_404(Viagem, id=id)

    mensagem_whatsapp = (
        f"Olá *{viagem.nome_motorista}*,\n\n"
        f"Aqui estão os detalhes referente à viagem para *{viagem.destino}*:\n"
        f"*Data e hora*: {viagem.horario.strftime('%d/%m/%Y, %H:%M:%S')}\n"
        f"*Total de Passageiros*: {viagem.total_passageiros}\n"
        f"*Receita Disponível*: R$ {viagem.receita_bruta:.2f}\n"
        f"\nObrigado!"
    )

    context = {
        "viagem": viagem,
        "mensagem_whatsapp": mensagem_whatsapp,
    }

    return render(request, "viagens/detalhes.html", context)


def nova_viagem(request):
    if request.method == "POST":
        destino = request.POST.get("destino")
        horario = request.POST.get("horario")
        nome_motorista = request.POST.get("nome_motorista")
        motorista_whatsapp = request.POST.get("motorista_whatsapp")
        total_passageiros = int(request.POST.get("total_passageiros", 0))
        nova_viagem = Viagem.objects.create(
            destino=destino,
            horario=horario,
            total_passageiros=total_passageiros,
            nome_motorista=nome_motorista,
            motorista_whatsapp=motorista_whatsapp,
        )
        return redirect("index")
    return render(request, "viagens/nova.html")


def excluir_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    viagem.delete()
    return redirect("index")


def adicionar_gasto_extra(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    if request.method == "POST":
        form = GastoExtraForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.viagem = viagem
            gasto.save()
            return redirect("detalhes_viagem", id=viagem.id)
    else:
        form = GastoExtraForm()
    return render(
        request, "viagens/adicionar_gasto_extra.html", {"form": form, "viagem": viagem}
    )


def listar_viagens(request):
    viagens_ativas = Viagem.objects.filter(excluida=False).count()

    return render(request, "viagens/index.html", {"viagens_ativas": viagens_ativas})
