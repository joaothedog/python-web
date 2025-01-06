//funcoes
export const formatarHorario = (horario: string) => {
    const data = new Date(horario);
    const dia = String(data.getDate()).padStart(2, '0');
    const mes = String(data.getMonth() + 1).padStart(2, '0');
    const ano = data.getFullYear();
    const horas = String(data.getHours()).padStart(2, '0');
    const minutos = String(data.getMinutes()).padStart(2, '0');
    return `${dia}/${mes}/${ano} - ${horas}:${minutos}`;
};

export const formatarNumeroTelefone = (numero: number | undefined | null): string => {
    if (!numero) {
        return 'Número indisponível';
    }
    return numero.toString().replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
};

export const formatarMoeda = (valor: number | undefined): string => {
    if (valor === undefined || valor === null) {
        return 'R$ 0,00';
    }
    return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
};