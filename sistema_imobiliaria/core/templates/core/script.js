document.addEventListener("DOMContentLoaded", function () {
    // Controle de Seções
    const sections = {
        dashboard: document.getElementById("dashboard-section"),
        residenciais: document.getElementById("residenciais-section"),
        moradores: document.getElementById("moradores-section")
    };

    // Navegação
    document.getElementById("home-link").addEventListener("click", () => showSection('dashboard'));
    document.getElementById("toggleResidenciais").addEventListener("click", () => showSection('residenciais'));
    document.getElementById("toggleMoradores").addEventListener("click", () => showSection('moradores'));

    function showSection(section) {
        Object.values(sections).forEach(sec => sec.style.display = 'none');
        sections[section].style.display = 'block';
        if (section === 'dashboard') updateDashboard();
    }

    // Dados
    const DB_KEY = 'imobiliaria_moradores';
    let moradores = JSON.parse(localStorage.getItem(DB_KEY)) || [];

    // Elementos
    const form = document.getElementById("form-morador");
    const listaGeral = document.getElementById("lista-geral");
    const listasResidenciais = {
        ip1: document.getElementById("lista-moradores-ip1"),
        // Adicione outros residenciais
    };

    // Formulário
    form.addEventListener("submit", function(e) {
        e.preventDefault();
        
        const morador = {
            residencial: form.residencial.value,
            apartamento: form.apartamento.value.trim(),
            nome: form.nome.value.trim(),
            // Adicione outros campos
            timestamp: new Date().toISOString()
        };

        if (Object.values(morador).some(v => !v)) {
            alert('Preencha todos os campos!');
            return;
        }

        moradores.push(morador);
        saveData();
        form.reset();
        bootstrap.Modal.getInstance(document.getElementById('modalMorador')).hide();
    });

    // Funções
    function saveData() {
        moradores.sort((a, b) => a.nome.localeCompare(b.nome));
        localStorage.setItem(DB_KEY, JSON.stringify(moradores));
        updateLists();
    }

    function updateLists() {
        // Limpar listas
        listaGeral.innerHTML = '';
        Object.values(listasResidenciais).forEach(list => list.innerHTML = '');

        // Popular listas
        moradores.forEach(morador => {
            // Lista Geral
            const liGeral = document.createElement('li');
            liGeral.className = 'list-group-item';
            liGeral.innerHTML = `
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <strong>${morador.nome}</strong> - 
                        Apto ${morador.apartamento} | ${morador.residencial.toUpperCase()}
                    </div>
                    <button class="btn btn-sm btn-danger" data-id="${morador.timestamp}">
                        Remover
                    </button>
                </div>
            `;
            listaGeral.appendChild(liGeral);

            // Lista por Residencial
            if (listasResidenciais[morador.residencial]) {
                const liResidencial = document.createElement('li');
                liResidencial.className = 'list-group-item';
                liResidencial.textContent = `${morador.nome} (Apto ${morador.apartamento})`;
                listasResidenciais[morador.residencial].appendChild(liResidencial);
            }
        });

        // Eventos de remoção
        document.querySelectorAll('.btn-danger').forEach(btn => {
            btn.addEventListener('click', function() {
                if (confirm('Remover este morador?')) {
                    moradores = moradores.filter(m => m.timestamp !== this.dataset.id);
                    saveData();
                }
            });
        });
    }

    function updateDashboard() {
        document.getElementById('ocupacao').textContent = `${moradores.length} unidades ocupadas`;
        // Adicione mais métricas conforme necessário
    }

    // Inicialização
    showSection('dashboard');
    updateLists();
});