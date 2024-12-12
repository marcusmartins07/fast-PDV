<template>
  <div class="mt-5">
    <Alert />
    <Navbar/>
    <div class="container">
      <div class="row">
        <div class="col mt-4">
          <div class="card">
            <div class="card-header text-center">Formas de Pagamento</div>
            <div class="card-body">
              <div class="d-flex justify-content-start">
                <button 
                  type="button" 
                  class="btn btn-bd-primary mx-2" 
                  v-for="forma in formas" 
                  :key="forma.forma_pagamento_id"
                  data-bs-toggle="modal" 
                  :data-bs-target="'#abrirModalPagamento-'+forma.forma_pagamento_id"
                  :disabled="valores_pagos_pedidos.valor_restante === 0">
                  {{ forma.descricao_forma }}
                </button>
              </div>
              
              <div v-for="forma in formas" :key="forma.forma_pagamento_id">
                <div class="modal fade" :id="'abrirModalPagamento-'+forma.forma_pagamento_id" tabindex="-1" aria-labelledby="modalPagamentoLabel" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
                  <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="modalPagamentoLabel">{{ forma.descricao_forma }}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        <form @submit.prevent>
                            <h6 class="modal-title mb-3">Confirme o pagamento com {{ forma.descricao_forma }}.</h6>
                            <div class="input-group my-2">
                              <div class="input-group-prepend">
                                <span class="input-group-text">R$</span>
                              </div>
                              <input type="number" class="form-control" v-model="valor_pagamento_modal">
                            </div>


                          <div v-if="forma.numero_parcela > 1">
                            <label for="parcelas">Escolha o número de parcelas:</label>
                            <select v-model="forma.numero_parcelas_selecionada" class="form-control">
                              <option v-for="n in forma.numero_parcela" :key="n" :value="n">{{ n }}x</option>
                            </select>
                          </div>
                        </form>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="button" class="btn btn-success" @click="adicionarFormaPagamento(forma.forma_pagamento_id, forma.descricao_forma, forma)">Confirmar</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="card mt-3">
            <div class="card-header text-center">Formas de pagamento selecionadas:</div>
            <div class="card-body overflow-auto">
              <div v-if="forma_pagamento_pedido.length > 0">
                <div class="d-flex flex-row row row-cols-2 row-cols-md-3 g-3">

                    <div class="col" v-for="(forma, index) in forma_pagamento_pedido" :key="index">
                      <div class="card h-100" style="width: 12rem;">
                        <div class="card-body">
                          <h4 class="card-title text-center">{{ forma.descricao_forma }}</h4>
                            <button type="button" class="btn-close position-absolute top-0 end-0 p-2" @click="abrirModalExcluirPagamento(index)"></button>
                            
                            <div class="modal fade" :id="'excluirFormaPagamentoModal-'+index" tabindex="-1" aria-labelledby="excluirFormaPagamentoLabel" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
                              <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                  <div class="modal-header">
                                    <h5 class="modal-title" id="excluirFormaPagamentoLabel">Excluir Forma de Pagamento</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                  </div>
                                  <form @submit.prevent="excluirFormaPagamento(index)">
                                    <div class="modal-body">
                                      <p class="mx-1">Tem certeza que deseja cancelar forma de pagamento em {{ forma.descricao_forma }} no valor de R$ {{ formatPreco(forma.valor_forma) }}?</p>
                                      <div class="form-floating mx-1">
                                        <input type="password" class="form-control col" id="floatingPassword" v-model="senha" required/>
                                        <label for="floatingPassword">Digite a senha para confirmar</label>
                                      </div>
                                    </div>
                                    <div class="modal-footer">
                                      <button type="submit" class="btn btn-bd-primary">Confirmar</button> 
                                    </div>
                                  </form>
                                </div>
                              </div>
                            </div>

                          <h6 class="card-text text-center">Parc.: {{ forma.numero_parcela }}x</h6>
                          <h6 class="card-text text-center">R$ {{ formatPreco(forma.valor_forma) }}</h6>
                        </div>
                      </div>
                    </div>

                    <div class="col" v-if="valores_pagos_pedidos.troco > 0">
                      <div class="card h-100" style="width: 12rem;">
                        <div class="card-body">
                          <h4 class="card-title text-center my-2">Troco</h4>
                          <h5 class="card-text text-center">R$ {{ formatPreco(valores_pagos_pedidos.troco) }}</h5>
                        </div>
                      </div>
                    </div>
                  
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col mt-4">
          <div class="card">
            <div class="card-header text-center">Cliente</div>
            <div class="card-body">
              <div class="row g-1 mb-3">
                <div class="col col-lg-3">
                  <div class="form-floating mx-1 row">
                    <input type="text" v-model="cliente.cliente_id" class="form-control" id="codigo_cliente" placeholder="Código" disabled/>
                    <label for="codigo_cliente">Código</label>
                  </div>
                </div>
                <div class="col-md">
                  <div class="form-floating mx-1 row">
                    <input type="text" v-model="cliente.cpf" class="form-control col" id="cpf_cliente" v-mask="'###.###.###-##'" placeholder="CPF" disabled/>
                    <label for="cpf_cliente">CPF</label>
                  </div>
                </div>
              </div>
              <div class="form-floating mb-1">
                <input type="text" class="form-control" id="nome_cliente" placeholder="Fulano de Ciclano" v-model="cliente.nome" disabled/>
                <label for="nome_cliente">Nome Completo</label>
              </div>
            </div>
          </div>

          <div class="card mt-3">
            <div class="card-header text-center">Total</div>
            <div class="card-body">
              <div class="row">
                <div class="col">Desconto: R$ {{ formatPreco(valores_pagos_pedidos.valor_desconto) }}</div>
                <div class="col">% Desconto = {{ calcularPercentualDesconto(valores_pagos_pedidos.valor_total, valores_pagos_pedidos.valor_desconto) }}%</div>
                <div class="col">SubTotal: R$ {{ formatPreco(valores_pagos_pedidos.valor_subtotal)  }}</div>
              </div>
              <div class="row mt-3">
                <div class="col">Quantidade: {{ quantidade_total }}</div>
                <div class="col">Total: R$ {{ formatPreco(valores_pagos_pedidos.valor_total) }}</div>
                <div class="col">Valor Restante: R$ {{ formatPreco(valores_pagos_pedidos.valor_restante) }}</div>
                <form @submit.prevent="enviarPedido">
                  <button type="submit" class="btn btn-bd-primary mt-3" data-bs-toggle="modal" data-bs-target="#ModalPDF" :disabled="valores_pagos_pedidos.valor_restante > 0">Finalizar Venda</button>
                </form>


  
                <div class="modal fade" id="ModalPDF" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="ModalPDF" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Impressão Cupom não Fiscal</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="retornarHome"></button>
                      </div>
                      <div class="modal-body">
                        <div v-if="pdf_url">
                          <iframe :src="pdf_url" width="100%" height="600px"></iframe>
                        </div>
                      </div>
                      <div class="modal-footer">
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    
  </div>

</template>

<script>
import Spinner from "../components/Utilities/Spinner.vue";
import Alert from "../components/Utilities/Alert.vue";
import Navbar from "@/components/Utilities/Navbar.vue";
import eventBus from '@/utils/eventBus.js';


export default {
  name: "Pedido",
    components: {
      Spinner,
      Alert,
      Navbar,    
  },
  data() {
    return {
      cliente: {},
      produtos_pedido: [],
      formas: [],
      forma_pagamento_pedido: [],
      forma_pagamento_excluir: null,
      quantidade_total: 0,
      valor_pago: 0,
      valor_pagamento_modal: 0,
      pedido_dados: {},
      pdf_url: null,
      senha: '',
      valores_pagos_pedidos: {
        valor_subtotal: 0,
        valor_total: 0,
        valor_desconto: 0, 
        desconto_porcentagem: 0,
        troco: 0,
        valor_restante: 0,
      },
    };
  },
  mounted() {
    this.buscarFormasPagamento();
    // Recupera localStorage
    const clienteStorage = localStorage.getItem('cliente_selecionado');
    const produtosStorage = localStorage.getItem('produtos_pedido');
    const forma_pagamento_pedido_storage = localStorage.getItem('forma_pagamento_pedido');

    if (produtosStorage) {
      const produtos_pedido = JSON.parse(produtosStorage);

      if (clienteStorage) {
        const cliente = JSON.parse(clienteStorage);
        this.carregarDados(cliente, produtos_pedido); 
        if (forma_pagamento_pedido_storage) {
          const pagamento = JSON.parse(forma_pagamento_pedido_storage)
          this.carregarDadosPagamentoPedido(pagamento)
        }
      } else {
        this.carregarDados(null, produtos_pedido); 
        if (forma_pagamento_pedido_storage) {
          const pagamento = JSON.parse(forma_pagamento_pedido_storage)
          this.carregarDadosPagamentoPedido(pagamento)
        }
      }
    } else {
      alert('Os dados de produtos não foram encontrados. Adicione produtos ao pedido para continuar.');
    }
    
  },

  methods: {
    carregarDados(cliente, produtos_pedido) {
      if (cliente) {
        this.cliente = cliente;
      } else {
        eventBus.emit('show-alert', { type: 'warning', message: 'Nenhum cliente selecionado. Prosseguindo sem cliente.' });
      }
      this.produtos_pedido = produtos_pedido;
      this.somaProduto();
    },

    carregarDadosPagamentoPedido(pagamento) {
      if (pagamento){
        this.forma_pagamento_pedido = pagamento
        this.somaProduto();
      }
    },

    async somaProduto() {
      let subtotal = 0;
      let total = 0;
      let desconto = 0;
      this.valores_pagos_pedidos.troco = 0;

      // Calcular o total
      this.produtos_pedido.forEach(produto => {
        subtotal += parseFloat(produto.preco_venda);
        total += parseFloat(produto.preco_venda);
        const precoDesconto = parseFloat(produto.preco_desconto);
        if (!isNaN(precoDesconto)) {
          desconto += precoDesconto;
        }
      });

      total = total - desconto;
      this.quantidade_total = this.produtos_pedido.length;
      this.valores_pagos_pedidos.valor_subtotal = subtotal;
      this.valores_pagos_pedidos.valor_total = total;
      this.valores_pagos_pedidos.valor_desconto = desconto;
      this.valores_pagos_pedidos.valor_restante = total;

      if (this.forma_pagamento_pedido){
        this.forma_pagamento_pedido.forEach(forma => {
          this.valores_pagos_pedidos.valor_restante -= forma.valor_forma
          if (forma.descricao_forma=="Dinheiro"){
            this.valores_pagos_pedidos.troco = forma.valor_troco 
            this.valores_pagos_pedidos.valor_restante += forma.valor_troco
          }
        })
      }


    },

    adicionarFormaPagamento(formaId, formaDescricao, forma) {
      const valorPagamento = parseFloat(this.valor_pagamento_modal);

      // Validar valor
      if (isNaN(valorPagamento) || valorPagamento <= 0) {
          eventBus.emit('show-alert', { type: 'danger', message:"Por favor, insira um valor válido para o pagamento."});
          return;
      }

      if (formaDescricao === 'Dinheiro') {
          const dinheiroSelecionado = this.forma_pagamento_pedido.some(
              pagamento => pagamento.descricao_forma === 'Dinheiro'
          );
          if (dinheiroSelecionado) {
              eventBus.emit('show-alert', { type: 'danger', message:"Apenas uma forma de pagamento em dinheiro é permitida." });
              return;
          }

          if (valorPagamento >= this.valores_pagos_pedidos.valor_restante) {
              this.valores_pagos_pedidos.troco = valorPagamento - this.valores_pagos_pedidos.valor_restante;
              this.valor_pago += this.valores_pagos_pedidos.valor_restante;
              this.valores_pagos_pedidos.valor_restante = 0;
          } else {
              this.valor_pago += valorPagamento;
              this.valores_pagos_pedidos.valor_restante -= valorPagamento;
          }
        } else {
            if (valorPagamento > this.valores_pagos_pedidos.valor_restante) {
                eventBus.emit('show-alert', { type: 'danger', message:`Valor excede o total a ser pago. Valor restante: R$ ${this.formatPreco(this.valores_pagos_pedidos.valor_restante)}` });
                return;
            }
            this.valor_pago += valorPagamento;
            this.valores_pagos_pedidos.valor_restante -= valorPagamento;
        }

        
        const numero_parcela_selecionada = forma.numero_parcelas_selecionada || 1; 
        this.forma_pagamento_pedido.push({
            forma_pagamento_id: forma.forma_pagamento_id,
            descricao_forma: forma.descricao_forma,
            numero_parcela: numero_parcela_selecionada,
            valor_forma: valorPagamento,
            valor_troco: this.valores_pagos_pedidos.troco
        });

        localStorage.setItem('forma_pagamento_pedido', JSON.stringify(this.forma_pagamento_pedido));
        localStorage.setItem('valores_pagos_pedidos', JSON.stringify(this.valores_pagos_pedidos));

        this.valor_pagamento_modal = 0;
        const modalId = '#abrirModalPagamento-' + formaId;
        const modalElement = document.querySelector(modalId);
        const modalInstance = bootstrap.Modal.getInstance(modalElement);
        modalInstance.hide();
    },

    abrirModalExcluirPagamento(index) {
      this.forma_pagamento_excluir = index;
      this.senha = '';

      const modalElement = document.getElementById(`excluirFormaPagamentoModal-${index}`);
      this.ModalExcluirPagamento = new bootstrap.Modal(modalElement);
      this.ModalExcluirPagamento.show();
    },

    async excluirFormaPagamento() {
      const resultado = await this.$ValidarSenha(this.senha);
      
      if (resultado.success) {
        eventBus.emit('show-alert', { type: 'success', message: resultado.message });
        this.forma_pagamento_pedido.splice(this.forma_pagamento_excluir, 1);
        this.forma_pagamento_excluir = null;
        localStorage.setItem('forma_pagamento_pedido', JSON.stringify(this.forma_pagamento_pedido));
        this.somaProduto();

        if (this.ModalExcluirPagamento) {
          this.ModalExcluirPagamento.hide();
        }
        document.querySelectorAll('.modal-backdrop').forEach(backdrop => backdrop.remove());

        eventBus.emit('show-alert', { type: 'warning', message: 'Forma de pagamento excluída' });
      } else {
        eventBus.emit('show-alert', { type: 'danger', message: resultado.message });
      }
    },

    formatPreco(valor) {
      return parseFloat(valor).toFixed(2).replace('.', ',');
    },

    calcularPercentualDesconto(valorTotal, valorDesconto) {
      this.valores_pagos_pedidos.desconto_porcentagem = ((valorDesconto / valorTotal) * 100).toFixed(2);
      return ((valorDesconto / valorTotal) * 100).toFixed(2);
    },

    async enviarPedido() {
      const date_time_now = new Date();

      const offset = -3;
      const data_pedido = new Date(date_time_now.getTime() + offset * 60 * 60 * 1000);

      this.pedido_dados = {
        data_pedido: data_pedido,
        cliente: this.cliente,
        produtos: this.produtos_pedido,
        formas_pagamento: this.forma_pagamento_pedido,
        valores: {
          valor_subtotal: parseFloat(this.valores_pagos_pedidos.valor_subtotal.toFixed(2)),
          valor_total: parseFloat(this.valores_pagos_pedidos.valor_total.toFixed(2)),
          valor_desconto: parseFloat(this.valores_pagos_pedidos.valor_desconto.toFixed(2)),
          desconto_porcentagem: this.valores_pagos_pedidos.desconto_porcentagem,
          valor_troco: parseFloat(this.valores_pagos_pedidos.troco.toFixed(2))
        }
      }

      try {
        // Envia o pedido
        const response = await this.$RequisicaoAutenticada('http://127.0.0.1:8000/api/v1/pedido/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.pedido_dados),
        });


        if (!response.ok) {
          eventBus.emit('show-alert', { type: 'danger', message: `Erro ao criar o pedido:` });
        }
        const responseData = await response.json();
        const pedidoId = responseData.pedido_id;
        const pdfResponse = await this.$RequisicaoAutenticada(`http://127.0.0.1:8000/api/v1/pedido/${pedidoId}/gerar_nota_fiscal`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/pdf',
          }
        });

        if (!pdfResponse.ok) {
          eventBus.emit('show-alert', { type: 'danger', message: `Erro ao gerar a nota fiscal` });
        }

        const pdfBlob = await pdfResponse.blob();
        this.pdf_url = URL.createObjectURL(pdfBlob);

      } catch (error) {
        eventBus.emit('show-alert', { type: 'warning', message: "Erro ao enviar o pedido ou gerar a nota fiscal:", error});
      }
    },

    async retornarHome() { 
      localStorage.removeItem('cliente_selecionado');
      localStorage.removeItem('produtos_pedido');
      localStorage.removeItem('forma_pagamento_pedido');
      localStorage.removeItem('valores_pagos_pedidos');
      this.$router.push({ name: 'Venda' });
    },

    async buscarFormasPagamento() {
      try {
        const req = await fetch('http://127.0.0.1:8000/api/v1/formas_pagamento/');
        if (!req.ok) {
          eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar formas de pagamento: ${req.statusText}` });
        }
        const data = await req.json();
        this.formas = Array.isArray(data.results) ? data.results : [];
      } catch (error) {
        eventBus.emit('show-alert', { type: 'warning', message: "Erro ao buscar formas de pagamento:", error});
      }
    },
  }
};
</script>

<style scoped>
  .overflow-auto{
    max-height: 25rem;
  }
</style>