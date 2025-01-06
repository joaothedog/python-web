import React, { useState, useEffect } from 'react';
import DetalhesViagem from './DetalhesViagem'
import { useNavigate } from 'react-router-dom';
import { listarViagens, excluirViagem, detalhesViagem } from '../services/api';
import { formatarHorario } from '../utils/formatters';

const ViagensLista: React.FC = () => {
    const [viagens, setViagens] = useState([]);
    const [viagemSelecionada, setViagemSelecionada] = useState<any | null>(null);
    const [pagina, setPagina] = useState(1);
    const [totalPaginas, setTotalPaginas] = useState(1);
    const navigate = useNavigate();

    useEffect(() => {
        carregarViagens(pagina);
    }, [pagina]);

    const carregarViagens = async (pagina: number) => {
        try {
            const response = await listarViagens({ page: pagina });
            setViagens(response.viagens_ativas);
            setTotalPaginas(response.total_pages);
        } catch (error) {
            console.error('Erro ao carregar viagens:', error);
        }
    };

    const handleExcluir = async (id: number) => {
        if (window.confirm('Tem certeza que deseja excluir esta viagem?')) {
            try {
                await excluirViagem(id);
                alert('Viagem excluída com sucesso!');
                carregarViagens(pagina);
            } catch (error) {
                console.error('Erro ao excluir viagem:', error);
            }
        }
    };

    const handleAbrirDetalhes = async (id: number) => {
        try {
            const viagemDetalhada = await detalhesViagem(id);
            console.log('Dados da viagem recebidos:', viagemDetalhada); // Verifique a resposta aqui
            setViagemSelecionada(viagemDetalhada); // Atualiza os dados da viagem
        } catch (error) {
            console.error('Erro ao carregar os detalhes da viagem:', error);
            alert('Erro ao carregar os detalhes da viagem.');
        }
    };

    const handleFecharModal = () => {
        setViagemSelecionada(null); // Fecha o modal
    };

    // const handleDetalhes = (id: number) => {
    //     navigate(`/viagem/${id}`);
    // };

    const handleNovaTarefa = () => {
        navigate(`/nova`)
    };

    return (
        <div>
            <h2>Lista de Viagens</h2>
            <ul>
                {viagens.map((viagem: any) => (
                    <li key={viagem.id}>
                        <strong>Destino:</strong> {viagem.destino} <br />
                        <strong>Horário:</strong> {formatarHorario(viagem.horario)} <br />
                        <strong>Motorista:</strong> {viagem.nome_motorista} <br />
                        <button onClick={() => handleAbrirDetalhes(viagem.id)}>Detalhes</button>
                        <button onClick={() => handleExcluir(viagem.id)}>Excluir</button>
                    </li>
                ))}
            </ul>
            {/* Modal */}
            {viagemSelecionada && (
                <div className="modal-overlay" onClick={handleFecharModal}>
                    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                        <DetalhesViagem viagem={viagemSelecionada} onClose={handleFecharModal} />
                    </div>
                </div>
            )}
            <div>
                <button disabled={pagina === 1} onClick={() => setPagina(pagina - 1)}>Anterior</button>
                <span>Página {pagina} de {totalPaginas}</span>
                <button disabled={pagina === totalPaginas} onClick={() => setPagina(pagina + 1)}>Próxima</button>
            </div>
            <button onClick={handleNovaTarefa}>Nova Tarefa</button>
        </div>
    );
};

export default ViagensLista;
