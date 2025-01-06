import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'Content-Type': 'application/json',
    },
    timeout: 5000,
});

// Endpoint para listar viagens com filtros e paginação
export const listarViagens = async (params?: { nome_motorista?: string; data_inicio?: string; data_fim?: string; page?: number }) => {
    const response = await api.get('/', { params });
    return response.data;
};

// Endpoint para obter os detalhes de uma viagem específica
export const detalhesViagem = async (id: number) => {
    const response = await api.get(`/viagem/${id}/`);
    return response.data;
};

// Endpoint para criar uma nova viagem
export const novaViagem = async (dados: {
    destino: string;
    horario: string;
    nome_motorista: string;
    motorista_whatsapp: string;
    total_passageiros: number;
}) => {
    try {
        // Enviar dados para a API, verificando o tipo de conteúdo (JSON)
        const response = await api.post('/viagem/nova/', dados, {
            headers: {
                'Content-Type': 'application/json', // Certificando-se de que o tipo é JSON
            }
        });

        return response.data;
    } catch (error: any) {
        // Exibir erro detalhado para diagnóstico
        console.error('Erro no endpoint novaViagem:', error.response || error);

        if (error.response) {
            // Caso o erro venha da resposta da API (erro 400, 500, etc.), mostrar a mensagem
            console.error('Erro de resposta da API:', error.response.data);
        } else {
            // Caso o erro não seja relacionado à API
            console.error('Erro inesperado:', error.message);
        }

        throw error; // Repassar o erro para que seja tratado no componente
    }
};

// Endpoint para excluir uma viagem
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
    const response = await api.post(`/viagem/${viagemId}/gasto/`, dados);
    return response.data; // Retorna o gasto recém-criado
};

export default api;
