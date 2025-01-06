import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Viagens from './components/Viagens'; 
import NovaViagemForm from './components/NovaViagemForm';
import './styles/style.css'

// app
const App: React.FC = () => {
  return (
    <Router>
      <div>
        <header>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Viagens />} />
            <Route path="/nova" element={<NovaViagemForm />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
