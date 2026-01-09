document.addEventListener('DOMContentLoaded', () => {
    const calcForm = document.getElementById('calcForm');
    const resultsDiv = document.getElementById('results');
    const errorDiv = document.getElementById('errorMessage');
    const errorText = document.getElementById('errorText');
    const btnCalcular = document.getElementById('btnCalcular');
    const loader = document.getElementById('loader');
    const suggestionBox = document.getElementById('suggestionBox');

    // Switch button logic data
    let currentSuggestion = null;
    let currentMonto = 0;
    let currentSeguroTotal = 0;

    // Real-time formatting for Amount
    const montoInput = document.getElementById('monto');
    montoInput.addEventListener('input', (e) => {
        // Remove existing commas and non-numeric chars (except empty string)
        let value = e.target.value.replace(/,/g, '').replace(/\D/g, '');

        if (value) {
            // Format with commas
            value = new Intl.NumberFormat('en-US').format(value);
            e.target.value = value;
        }
    });

    // Real-time formatting for Seguro
    const seguroInput = document.getElementById('seguro');
    seguroInput.addEventListener('input', (e) => {
        let value = e.target.value.replace(/,/g, '').replace(/\D/g, '');

        if (value) {
            value = new Intl.NumberFormat('en-US').format(value);
            e.target.value = value;
        }
    });

    calcForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // UI Reset
        resultsDiv.classList.add('hidden');
        errorDiv.classList.add('hidden');
        suggestionBox.classList.add('hidden');
        btnCalcular.classList.add('loading');

        // Get values
        // Remove commas before parsing
        const rawMonto = document.getElementById('monto').value.replace(/,/g, '');
        const monto = parseFloat(rawMonto);
        const plazo = parseInt(document.getElementById('plazo').value);

        const rawSeguro = document.getElementById('seguro').value.replace(/,/g, '');
        const seguro = parseFloat(rawSeguro);

        currentMonto = monto;

        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ monto, plazo, seguro })
            });

            const data = await response.json();

            if (response.ok) {
                // Update Results
                displayResults(data);

                // Handle Suggestion
                if (data.sugerencia) {
                    currentSuggestion = data.sugerencia;
                    currentSeguroTotal = data.seguro_total;
                    showSuggestion(data.sugerencia);
                }

                resultsDiv.classList.remove('hidden');
            } else {
                throw new Error(data.error || 'Error desconocido');
            }
        } catch (error) {
            errorText.textContent = error.message;
            errorDiv.classList.remove('hidden');
        } finally {
            btnCalcular.classList.remove('loading');
        }
    });

    // Handle Switch Button to EMP023
    document.getElementById('btnSwitch').addEventListener('click', async () => {
        if (!currentSuggestion) return;

        const alt = currentSuggestion.alternativa;

        try {
            const response = await fetch('/recalculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    monto: currentMonto,
                    seguro_total: currentSeguroTotal,
                    tasa: alt.tasa
                })
            });

            const data = await response.json();

            if (response.ok) {
                // Update UI to show EMP023
                updateDisplayForSwitch(alt, data);
            } else {
                alert(data.error);
            }
        } catch (error) {
            alert(error.message);
        }
    });

    // Format helpers
    const formatCurrency = (val) => {
        return new Intl.NumberFormat('es-CO', {
            style: 'currency',
            currency: 'COP',
            maximumFractionDigits: 0
        }).format(val);
    };

    const formatPercent = (val) => {
        return (val * 100).toFixed(4) + '%';
    };

    function displayResults(data) {
        document.getElementById('fundName').textContent = data.seleccion.nombre;
        document.getElementById('resMonto').textContent = formatCurrency(data.monto);
        document.getElementById('resPlazo').textContent = data.plazo + ' meses';
        document.getElementById('resSeguro').textContent = formatCurrency(data.seguro_total);
        document.getElementById('resTasa').textContent = formatPercent(data.seleccion.tasa);
        document.getElementById('resComisionValor').textContent = formatCurrency(data.comision_valor);
        document.getElementById('resCreditoTotal').textContent = formatCurrency(data.credito_total);
    }

    function showSuggestion(sug) {
        document.getElementById('sugAltRate').textContent = (sug.alternativa.tasa * 100).toFixed(4);
        suggestionBox.classList.remove('hidden');
    }

    function updateDisplayForSwitch(alt, data) {
        // Update badge and values
        document.getElementById('fundName').textContent = alt.nombre;
        document.getElementById('resTasa').textContent = formatPercent(alt.tasa);
        document.getElementById('resComisionValor').textContent = formatCurrency(data.comision_valor);
        document.getElementById('resCreditoTotal').textContent = formatCurrency(data.credito_total);

        // Hide suggestion box since we took it
        suggestionBox.classList.add('hidden');
    }
});
