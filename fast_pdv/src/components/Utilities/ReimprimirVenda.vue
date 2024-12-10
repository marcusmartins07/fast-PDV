<template>
    <div>
        <div class="modal fade" id="reimprimirVenda" tabindex="-1" aria-labelledby="consultaProdutoLabel"
            aria-hidden="true">
            <div class="modal-dialog modal-fullscreen">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="consultaProdutoLabel">
                            Reimprimir Venda
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col">Pedido</th>
                                    <th scope="col">Data</th>
                                    <th scope="col">ID Cliente</th>
                                    <th scope="col">Nome</th>
                                    <th scope="col">CPF</th>
                                    <th scope="col">QTD Itens</th>
                                    <th scope="col">Subtotal</th>
                                    <th scope="col">Desconto</th>
                                    <th scope="col">Total</th>
                                    <th scope="col">Troco</th>
                                    <th scope="col"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="venda in vendas_buscadas" :key="venda.pedido_id" >
                                    <th scope="row">{{ venda.pedido_id }}</th>
                                    <td>{{ formatData(venda.json_pedido.data_pedido) }}</td>
                                    <td>{{ venda.json_pedido.cliente.cliente_id }}</td>
                                    <td>{{ venda.json_pedido.cliente.nome }}</td>
                                    <td>{{ venda.json_pedido.cliente.cpf }}</td>
                                    <td>{{ venda.json_pedido.produtos.length }}</td>
                                    <td>{{ formatPreco(venda.json_pedido.valores.valor_subtotal) }}</td>
                                    <td>R$ {{ formatPreco(venda.json_pedido.valores.valor_desconto) }} / {{ venda.json_pedido.valores.desconto_porcentagem }}%</td>
                                    <td>R$ {{ formatPreco(venda.json_pedido.valores.valor_total) }}</td>
                                    <td>R$ {{ formatPreco(venda.json_pedido.valores.valor_troco) }}</td>
                                    <td><button class="btn btn-bd-primary" type="button" @click="reimprimirNota(venda.pedido_id)">Reimprimir</button></td>
                                </tr>
                            </tbody>
                            </table>
                    </div>
                    <div class="modal-footer">
                        <div class="pagination">
                            <button class="btn btn-bd-primary me-2" :disabled="!previous"
                                @click="consultarProdutos(previous)">
                                Página Anterior
                            </button>
                            <button class="btn btn-bd-primary me-2" :disabled="!next" @click="consultarProdutos(next)">
                                Próxima Página
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="modal fade" id="abrirModalPDF" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Impressão Cupom não Fiscal</h1>
                        <form @submit.prevent="retornarHome">
                            <button type="submit" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </form>
                    </div>
                    <div class="modal-body">
                        <div v-if="pdfUrl">
                            <iframe :src="pdfUrl" width="100%" height="600px"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="d-flex flex-column">
            <div class="d-grid gap-2 mt-auto">
                <div class="btn btn-bd-primary" type="button" @click="abrirModal('reimprimirVenda')">
                    Reimprimir Venda
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Spinner from "../Utilities/Spinner.vue";
    import eventBus from "@/utils/eventBus";

    export default {
        name: "ReimprimirVenda",
        components: {
            Spinner,
        },
        data() {
            return {
                vendas_buscadas: [],
                next: null,
                previous: null,
                pdfUrl: null,
            };
        },
        mounted() {
            this.consultarProdutos();
        },

        methods: {
            abrirModal(modal_id) {
                const modal = new bootstrap.Modal(
                    document.getElementById(modal_id),
                    {
                        backdrop: "static",
                        keyboard: false,
                    }
                );
                modal.show();
                document
                    .querySelectorAll(".modal-backdrop")
                    .forEach((backdrop) => backdrop.remove());
            },

            async consultarProdutos(url = "http://127.0.0.1:8000/api/v1/pedido/") {
                try {
                    const req = await this.$RequisicaoAutenticada(url);

                    if (!req.ok) {
                        eventBus.emit("show-alert", {
                            type: "danger",
                            message: `Erro HTTP: ${req.status} - ${req.statusText}`,
                        });
                    }

                    const data = await req.json();
                    this.vendas_buscadas = data.results;
                    this.next = data.next;
                    this.previous = data.previous;
                } catch (error) {
                    eventBus.emit("show-alert", {type: "danger", message: `Erro ao buscar os produtos: ${error.message}`});
                }
            },
            formatPreco(value) {
                const num = parseFloat(value);
                if (isNaN(num)) {
                    return "0,00";
                }
                return num.toFixed(2).replace(".", ",");
            },

            formatData(value) {
                const data_pedido_json = value
                const dia = data_pedido_json.substring(0, 4);
                const mes = data_pedido_json.substring(5, 7);
                const ano = data_pedido_json.substring(8, 10);
                const horas = data_pedido_json.substring(11, 13);
                const minutos = data_pedido_json.substring(14, 16);
                const segundos = data_pedido_json.substring(17, 19);
                return `${dia}/${mes}/${ano} - ${horas}:${minutos}:${segundos}`;
            },
            
            async reimprimirNota(pedido_id) {
                try {
                    const pdfResponse = await this.$RequisicaoAutenticada(`http://127.0.0.1:8000/api/v1/pedido/${pedido_id}/gerar_nota_fiscal`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/pdf',
                    }
                    });
                    
                    this.abrirModal('abrirModalPDF')
                    const pdfBlob = await pdfResponse.blob();
                    this.pdfUrl = URL.createObjectURL(pdfBlob);

                } catch (error) {
                    eventBus.emit('show-alert', { type: 'danger', message: `Erro ao reimprimir cupom não fiscal: ${error}`});
                }
            },
        },
    };
</script>

<style scoped>
    .modal-backdrop.show {
        opacity: none;
    }

    .offcanvas-backdrop {
        display: none;
    }

    .modal-header {
        justify-content: space-evenly;
    }
</style>