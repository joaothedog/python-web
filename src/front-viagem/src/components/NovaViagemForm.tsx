import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { novaViagem } from '../services/api';

const NovaViagemForm: React.FC = () => {
    const navigate = useNavigate(); // Inicializa o hook para navegação
    const [formData, setFormData] = useState({
        destino: '',
        horario: '',
        nome_motorista: '',
        motorista_whatsapp: '',
        total_passageiros: 0,
        valor_por_passageiro: 0,
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        // Verifica se o horário está preenchido e formata para o padrão correto
        if (formData.horario) {
            // Substitui o 'T' por um espaço e adiciona os segundos no formato correto
            formData.horario = formData.horario.replace("T", " ") + ":00";
        }

        try {
            await novaViagem(formData);
            alert('Viagem criada com sucesso!');
            navigate('/'); // Redireciona para a página de índice
            setFormData({
                destino: '',
                horario: '',
                nome_motorista: '',
                motorista_whatsapp: '',
                total_passageiros: 0,
                valor_por_passageiro: 0,
            });
        } catch (error) {
            console.error('Erro ao criar viagem:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Criar Nova Viagem</h2>
            <div>
                <label>Destino:</label>
                <input name="destino" value={formData.destino} onChange={handleChange} required />
            </div>
            <div>
                <label>Valor por Passageiro:</label>
                <input
                    name="valor_por_passageiro"
                    type="number"
                    step="0.01"
                    value={formData.valor_por_passageiro}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label>Horário:</label>
                <input name="horario" type="datetime-local" value={formData.horario} onChange={handleChange} required />
            </div>
            <div>
                <label>Nome do Motorista:</label>
                <input name="nome_motorista" value={formData.nome_motorista} onChange={handleChange} required />
            </div>
            <div>
                <label>WhatsApp do Motorista:</label>
                <input name="motorista_whatsapp" value={formData.motorista_whatsapp} onChange={handleChange} required />
            </div>
            <div>
                <label>Total de Passageiros:</label>
                <input name="total_passageiros" type="number" value={formData.total_passageiros} onChange={handleChange} required />
            </div>
            <button type="submit">Criar Viagem</button>
        </form>
    );
};

export default NovaViagemForm;
