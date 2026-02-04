const API_URL = "http://127.0.0.1:8000/gastos"
console.log("App cargada")

document.addEventListener("DOMContentLoaded", function() {
    cargarGastos()
})

const Total_de_gastos = 0

async function cargarGastos() {
    const tbody = document.getElementById("gastos-body")
    const errorDiv = document.getElementById("error")

    tbody.innerHTML = ""
    errorDiv.classList.add("d-none")    // Añadimos la clase para ocultar el div de error

    try{
        const response = await fetch(API_URL)

        if(!response.ok){
            throw new Error('Error HTTO: ${response.status}')
        }

        const gastos = await response.json()

        if(!Array.isArray(gastos)){
            throw new Error("La Api no devolvio un array")
        }

        if(gastos.length === 0){
            tbody.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center">No hay gastos registrados</td>
                </tr>
            `
            return
        }

        gastos.forEach(gasto => {
            const tr = document.createElement("tr")

            tr.innerHTML = `
                <td>${gasto.id}</td>
                <td>${gasto.descripcion}</td>
                <td>${gasto.monto.toFixed(2)}</td>
                <td>${gasto.categoria}</td>
                <td>${new Date(gasto.fecha).toLocaleDateString()}</td>
                <td><button class="btn btn-danger btn-sm">Eliminar</button></td>
            `
            tbody.appendChild(tr)

            const btnEliminar = tr.querySelector("button")
            btnEliminar.addEventListener("click", function(){
                console.log("Eliminar gasto con ID:", gasto.id)

                const URL_ELIMINAR = `${API_URL}/${gasto.id}`

                fetch(URL_ELIMINAR, {
                    method: "DELETE"
                })
                .then(response => {
                    if(!response.ok){
                        throw new Error("Error al eliminar el gasto")
                    }
                    return response.json()
                })
                .then(data => {
                    console.log("Gasto eliminado:", data)
                    cargarGastos()     // recargar la lista de gastos
                })
                .catch(error => {
                    console.error("Error en la solicitud de eliminación:", error)
                })
            })
        })

    }catch(error){
        console.error("Error al cargar los gastos:", error)
        errorDiv.textContent = "No se pudieron cargar los gastos"
        errorDiv.classList.remove("d-none")
    }
}

const formulario = document.getElementById("form-gasto")

formulario.addEventListener("submit", function(event) {
    event.preventDefault()
    console.log("submit capturado")

    const categoria = document.getElementById("categoria").value
    const monto = parseFloat(document.getElementById("monto").value)
    const fecha = document.getElementById("fecha").value
    const descripcion = document.getElementById("descripcion").value

    const nuevoGasto = {
        descripcion,
        categoria,
        monto,
        fecha
    }
    console.log("Nuevo gasto a enviar:", nuevoGasto)

    fetch(API_URL, {
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify(nuevoGasto)
    })
    .then(response => {
        if(!response.ok){
            throw new Error("Error al crear el gasto")
        }
        return response.json()      // devuelve al siguiente then
    })
    .then(data => {
        console.log("Gasto creado:", data)
        formulario.reset()         // limpiar el formulario
        cargarGastos()             // recargar la lista de gastos
    })
    .catch(error => {
        console.error("Error en la solicitud:", error)
    })
})

async function cargarEstadisticas() {
    try{
        const response = await fetch(`${API_URL}/estadisticas`)

        if(!response.ok){
            throw new Error("Error al obtener estadisticas")
        }

        const data = await response.json()

        pintarcard(data, Total_de_gastos)
        pintarCategorias(data.por_categoria)
        pintarMeses(data.por_mes)
        //graficas
        pintarGraficaCategorias(data.por_categoria)
        pintarGraficaMeses(data.por_mes)
    }catch(error){
        console.error("Error al cargar las estadisticas:", error)
        alert("No se pudieron cargar las estadisticas")
    }
}

function pintarcard(data, Total_de_gastos){
    document.getElementById("total-gastos").textContent = `${data.total_gastos} €`

    document.getElementById("numero-gastos").textContent = `${data.numero_gastos_mes_actual}`

}

function pintarCategorias(categorias){
    const tbody = document.getElementById("tabla-categorias")
    tbody.innerHTML = ""

    categorias.forEach(cat => {
        const tr = document.createElement("tr")

        tr.innerHTML = `
            <td>${cat.categoria}</td>
            <td>${cat.total.toFixed(2)} €</td>
        `
        tbody.appendChild(tr)
    })
}

let total_este_mes = 0

function pintarMeses(meses){
    const tbody = document.getElementById("tabla-meses")
    tbody.innerHTML = ""
    
    meses.forEach(mes => {
        const tr = document.createElement("tr")

        
        tr.innerHTML = `
            <td>${mes.mes}</td>
            <td>${mes.total.toFixed(2)} €</td>
        `
        tbody.appendChild(tr)
    })
}

async function pintarGraficaCategorias(categorias){
    const labels = categorias.map(cat => cat.categoria)
    const valores = categorias.map(cat => cat.total)

    new Chart(document.getElementById("graficoCategorias"), {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Gato por categoria (€)",
                data: valores
            }]
        }
    })
}

async function pintarGraficaMeses(meses){
    const labels = meses.map(mes => mes.mes)
    const valores = meses.map(mes => mes.total)

    new Chart(document.getElementById("graficoMeses"), {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Gastos por mes (€)",
                data: valores
            }]
        }
    })
}


document.addEventListener("DOMContentLoaded", cargarEstadisticas);
