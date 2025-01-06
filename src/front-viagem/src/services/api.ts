import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'Content-Type': 'application/json',
    },
    timeout: 5000,
});

// listar viagens com filtros e paginação
export const listarViagens = async (params?: { nome_motorista?: string; data_inicio?: string; data_fim?: string; page?: number }) => {
    const response = await api.get('/', { params });
    return response.data;
};

// viagem específica
export const detalhesViagem = async (id: number) => {
    const response = await api.get(`/viagem/${id}/`);
    return response.data;
};

// nova viagem
export const novaViagem = async (dados: {
    destino: string;
    horario: string;
    nome_motorista: string;
    motorista_whatsapp: string;
    total_passageiros: number;
}) => {
    try {
        const response = await api.post('/viagem/nova/', dados, {
            headers: {
                'Content-Type': 'application/json',
            }
        });

        return response.data;
    } catch (error: any) {
        console.error('Erro no endpoint novaViagem:', error.response || error);

        if (error.response) {
            // debug error number
            console.error('Erro de resposta da API:', error.response.data);
        } else {

            console.error('Erro inesperado:', error.message);
        }

        throw error;
    }
};

// excluir uma viagem
export const excluirViagem = async (viagemId: number) => {
    try {
        const response = await api.delete(`/viagem/${viagemId}/excluir/`);
        console.log('Resposta da exclusão:', response);
        return response.data;
    } catch (error: any) {
        console.error('Erro ao excluir viagem:', error.response || error);
        throw error;
    }
};

export const adicionarGastoExtra = async (
    viagemId: number,
    dados: { valor: number; descricao: string }
) => {
    // debug
    console.log('Dados do gasto a serem enviados:', dados);
    const response = await api.post(`/viagem/${viagemId}/gasto/`, dados);
    return response.data; // gasto
};

export default api;
