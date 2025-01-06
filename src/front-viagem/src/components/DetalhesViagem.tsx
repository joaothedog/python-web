import React, { useState, useEffect } from 'react';
import { adicionarGastoExtra } from '../services/api';
import { formatarHorario, formatarNumeroTelefone } from '../utils/formatters';

interface DetalhesViagemProps {
    viagem: any;
    onClose: () => void; // Callback para fechar o modal
}

interface Gasto {
    descricao: string;
    valor: number;
}

const DetalhesViagem: React.FC<DetalhesViagemProps> = ({ viagem, onClose }: { viagem: any; onClose: () => void }) => {
    const [gastos, setGastos] = useState<Gasto[]>([]);
    const [gastoDescricao, setGastoDescricao] = useState('');
    const [gastoValor, setGastoValor] = useState<string>(''); // Iniciar como string vazia

    const viagemDetalhes = viagem?.viagem;
    
    useEffect(() => {
        if (viagemDetalhes) {
            setGastos(viagemDetalhes.gastos || []);
        }
    }, [viagemDetalhes]);

    const handleAdicionarGasto = async () => {
        if (!viagemDetalhes?.id || !gastoDescricao || isNaN(parseFloat(gastoValor)) || parseFloat(gastoValor) <= 0) {
            alert('Preencha todos os campos com valores válidos.');
            return;
        }
    
        const valorNumerico = parseFloat(gastoValor);
    
        try {
            // Envia o gasto extra para a API com o valor garantido como número
            const novoGasto = await adicionarGastoExtra(viagemDetalhes.id, {
                descricao: gastoDescricao,
                valor: valorNumerico,
            });
    
            setGastos((prevGastos) => [...prevGastos, novoGasto]);
    
            alert('Gasto extra adicionado com sucesso!');
            setGastoDescricao('');
            setGastoValor('');
        } catch (error) {
            console.error('Erro ao adicionar gasto extra:', error);
            alert('Não foi possível adicionar o gasto extra.');
        }
    };

    const handleWhatsAppMessage = () => {
        if (viagemDetalhes?.mensagem_whatsapp && viagemDetalhes?.motorista_whatsapp) {
            const url = `https://wa.me/${viagemDetalhes.motorista_whatsapp}?text=${encodeURIComponent(viagemDetalhes.mensagem_whatsapp)}`;
            window.open(url, '_blank');
        } else {
            alert('Número do motorista ou mensagem indisponível.');
        }
    };

    if (!viagemDetalhes) {
        return <p>Carregando detalhes da viagem...</p>;
    }

    const {
        destino,
        horario,
        nome_motorista,
        total_passageiros,
        receita_bruta,
        motorista_whatsapp,
    } = viagemDetalhes;

    return (
        <div>
            <h2>Detalhes da Viagem</h2>
            <p><strong>Destino:</strong> {destino}</p>
            <p><strong>Horário:</strong> {formatarHorario(horario)}</p>
            <p><strong>Motorista:</strong> {nome_motorista}</p>
            <p><strong>Total de Passageiros:</strong> {total_passageiros}</p>
            <p><strong>Receita Bruta:</strong> R$ {parseFloat(receita_bruta).toFixed(2)}</p>
            <p><strong>Contato Motorista:</strong> {formatarNumeroTelefone(motorista_whatsapp) || 'Número indisponível'}</p>

            <h3>Gastos Extras</h3>
            {gastos.length === 0 ? (
                <p>Sem gastos extras registrados.</p>
            ) : (
                gastos.map((gasto: any, index: number) => {
                    const valor = parseFloat(gasto.valor);  // Converte para número, caso seja uma string
                    return (
                        <p key={index}>
                            {gasto.descricao}: R$ {isNaN(valor) ? 'Valor inválido' : valor.toFixed(2)}
                        </p>
                    );
                })
            )}

            <h3>Adicionar Gasto Extra</h3>
            <input
                type="text"
                placeholder="Descrição"
                value={gastoDescricao}
                onChange={(e) => setGastoDescricao(e.target.value)}
            />
            <input
                type="number"
                value={gastoValor}
                onChange={(e) => setGastoValor(e.target.value)}
                placeholder="Valor"
                min="0"
                step="any" // Permite valores decimais
            />

            <button onClick={handleAdicionarGasto}>Adicionar Gasto</button>

            <h3>Mensagem para WhatsApp</h3>
            <button onClick={handleWhatsAppMessage}>
                Enviar Detalhes pelo WhatsApp
            </button>

            <br />
            <button onClick={onClose}>Fechar</button>
        </div>
    );
};

export default DetalhesViagem;
