<template>
  <div class="container=sm">
    <div class="card">  
    <div class="card-header text-center h6">Produtos</div>
      <div class="card-body overflow-auto px-0" ref="produtosContainer">
        <ul class="list-group list-group-flush" >
          <li class="list-group-item" v-for="(produto, index) in produtos_pedido" :key="index">
            
            <div class="modal fade" :id="'desconto-produto-' + index" tabindex="-1" aria-labelledby="desconto-produto" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title">Editar Desconto</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="container row">
                      <div class="col-2">{{ (index + 1).toString().padStart(3, '0') }}</div>
                      <div class="col">{{ produto.nome }}</div>
                    </div>
                    <form class="mt-3">
                      <label for="basic-url">Valor do produto:</label>
                      <div class="input-group my-2">
                        <div class="input-group-prepend">
                          <span class="input-group-text">R$</span>
                        </div>
                        <input type="text" class="form-control" v-model="produto.preco_venda" disabled>
                      </div>

                      <label for="basic-url">Desconto %:</label>
                      <div class="input-group my-2">
                        <div class="input-group-prepend">
                          <span class="input-group-text">%</span>
                        </div>
                        <input type="number" class="form-control" v-model.number="produto.porcentagem_desconto" @input="calcularPorPercentual(index)">
                      </div>

                      <label for="basic-url">Desconto R$:</label>
                      <div class="input-group my-2">
                        <div class="input-group-prepend">
                          <span class="input-group-text">R$</span>
                        </div>
                        <input type="number" class="form-control" v-model.number="produto.preco_desconto" @input="calcularPorValorDesconto(index)">
                      </div>

                      <label for="basic-url">Valor final do produto:</label>
                      <div class="input-group my-2">
                        <div class="input-group-prepend">
                          <span class="input-group-text">R$</span>
                        </div>
                        <input type="number" class="form-control" v-model.number="produto.preco_final" @input="calcularPorValorFinal(index)">
                      </div>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="cancelarAlteracoes(index)">Cancelar</button>
                    <button type="button" class="btn btn-bd-primary" @click="salvarAlteracoes(index)">Salvar</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="modal fade" :id="'abrirModalExclusao-'+index" tabindex="-1" aria-labelledby="confirmarExclusaoLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="confirmarExclusaoLabel">Confirmar Exclusão</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    Você tem certeza que deseja excluir este produto?
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-danger" @click="confirmarExclusao(index)">Excluir</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="card-title row">
              <div class="col-1 p-0 ps-2">{{ (index + 1).toString().padStart(3, '0') }}</div>
              <div class="col-8">{{ produto.nome }}</div>
              <div class="col text-end d-flex justify-content-end align-items-center"> 
                <div v-if="produto.preco_desconto > 0" class="me-2">D:{{ produto.porcentagem_desconto }}%</div>
                R$ {{ formatPreco(produto.preco_venda-produto.preco_desconto) }}
              </div>
            </div>
            <div class="card-text row segunda-linha">
              <div class="col-auto p-0 me-1">
                <button type="button" class="btn btn-bd-primary btn-sm" @click="abrirModal(index)" :disabled="possui_forma_pagamento == true">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-slash-minus" viewBox="0 0 16 16">
                    <path d="m1.854 14.854 13-13a.5.5 0 0 0-.708-.708l-13 13a.5.5 0 0 0 .708.708M4 1a.5.5 0 0 1 .5.5v2h2a.5.5 0 0 1 0 1h-2v2a.5.5 0 0 1-1 0v-2h-2a.5.5 0 0 1 0-1h2v-2A.5.5 0 0 1 4 1m5 11a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5A.5.5 0 0 1 9 12"/>
                  </svg>
                </button>
              </div>
              <div class="col-auto p-0">
                <button type="button" class="btn btn-danger btn-sm" @click="abrirModalExclusao(index)" :disabled="possui_forma_pagamento == true">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5M8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5m3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0"/>
                  </svg>
                </button>
              </div>
              <div class="col-md">Cod.: {{ produto.codigo_barras }}</div>
              <div class="col-md" v-if="produto.preco_desconto > 0">De: {{ formatPreco(produto.preco_venda) }}  Por: {{ formatPreco(produto.preco_venda-produto.preco_desconto) }}</div>
              <div class="col text-end"> {{ produto.categoria }}</div>
            </div>
          </li>
        </ul>
      </div>
      <div class="card-footer">
        <form @submit.prevent="biparProduto">
          <div class="input-group my-3">
            <input type="text" v-model="codigo_barras" class="form-control" placeholder="Código de barras" aria-label="Código de barras" aria-describedby="button-addon2">
            <button class="btn btn-bd-primary" type="submit" id="button-addon2">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
              </svg>
            </button>
          </div>
        </form>
        <div class="row">
          <div class="col">Desconto: R$ {{ formatPreco(valor_desconto) }}</div>
          <div class="col">% Desconto = {{ calcularPercentualDesconto(valor_subtotal, valor_desconto) }}%</div>
          <div class="col">Subtotal: R$ {{ formatPreco(valor_subtotal)  }}</div>
          
        </div>
        <div class="row mt-3 mb-2">
          <div class="col">Quantidade: {{ quantidade_total }}</div>
          <div class="col">Total: R$ {{ formatPreco(valor_total) }}</div>
        </div>
        
      </div>
    </div>
    
  </div>
</template>

<script>
import Spinner from '../Utilities/Spinner.vue';
import eventBus from '@/utils/eventBus';
export default {
  name: "Produto",
  components: {
    Spinner,
  },
  data() {
    return {
      produtos_pedido: [],
      codigo_barras: '',
      valor_subtotal: 0,
      valor_total: 0,
      valor_desconto: 0,
      quantidade_total: 0,
      produto_original: {},
      produto_para_excluir: null,
      possui_forma_pagamento: false,
    };
  },

  mounted() {
    const produtosStorage = localStorage.getItem('produtosPedido');

    if (produtosStorage) {
      const produtosPedido = JSON.parse(produtosStorage);
      this.produtos_pedido = produtosPedido
      this.somaProduto();
      this.$emit("atualizarProdutos", this.produtos_pedido);
    } 
    this.carregarDadosPagamentoPedido();
  },
  
  methods: {
    async atualizarProduto(){
      const produtosPedido = this.produtos_pedido;
      localStorage.setItem('produtosPedido', JSON.stringify(produtosPedido));
      this.$emit("atualizarProdutos", this.produtos_pedido);
    },
    async getProduto() {
      try {
        const req = await this.$RequisicaoAutenticada(
          `http://127.0.0.1:8000/api/v1/produto/buscar_por_codigo_barras/?codigo_barras=${this.codigo_barras}`
        );

        if (req.status === 404) {
          eventBus.emit('show-alert', { type: 'danger', message: `Produto não existe:` });
        } else if (!req.ok) {
          eventBus.emit('show-alert', { type: 'danger', message: `Erro na requisição:` });
        }

        const data = await req.json();
        this.produtos_pedido.push(data);
        this.codigo_barras = "";

        this.$nextTick(() => {
          const produtosContainer = this.$refs.produtosContainer;
          if (produtosContainer) {
            produtosContainer.scrollTop = produtosContainer.scrollHeight;
          }
        });
      } catch (error) {
        eventBus.emit("show-alert", {
          type: "danger",
          message: `Erro ao buscar o produto: ${error.message}`,
        });
      }
    },

    carregarDadosPagamentoPedido() {
      if (this.produtos_pedido){
        const pagamento_pedido = localStorage.getItem('forma_pagamento_pedido');
        const forma_pagamento_pedido = JSON.parse(pagamento_pedido);
        if(!forma_pagamento_pedido || forma_pagamento_pedido.length === 0){
          this.possui_forma_pagamento = false
        }
        else {
          this.possui_forma_pagamento = true
        }
      }
    },
    
    async somaProduto() {
      let subtotal = 0;
      let total = 0;
      let desconto = 0;

      this.produtos_pedido.forEach(produto => {
        subtotal += parseFloat(produto.preco_venda);
        total += parseFloat(produto.preco_venda);
        const precoDesconto = parseFloat(produto.preco_desconto);
        if (!isNaN(precoDesconto)) {
          desconto += precoDesconto;
        }
      });

      total = total - desconto

      this.quantidade_total = this.produtos_pedido.length;
      this.valor_subtotal = subtotal;
      this.valor_total = total;
      this.valor_desconto = desconto;
      this.atualizarProduto();
    },

    async biparProduto() {
      if (this.codigo_barras.length == 13) { 
        eventBus.emit('loading', true);
        await this.getProduto();
        await this.somaProduto();
        eventBus.emit('loading', false);
      } else {
        eventBus.emit('show-alert', { type: 'danger', message: 'Código de barras inválido, deve ter 13 dígitos.'});
        this.codigo_barras = ''; // Limpa o campo de código de barras
      }
    },

    calcularPercentualDesconto(preco_venda, preco_desconto) {
      if (preco_venda === 0 || !preco_desconto) return 0;
      return ((preco_desconto / preco_venda) * 100).toFixed(2);
    },

    calcularPorPercentual(index) {
      const produto = this.produtos_pedido[index];

      produto.preco_desconto = (produto.preco_venda * produto.porcentagem_desconto / 100).toFixed(2);
      produto.preco_final = (produto.preco_venda - produto.preco_desconto).toFixed(2);
    },

    calcularPorValorDesconto(index) {
      const produto = this.produtos_pedido[index];

      produto.porcentagem_desconto = this.calcularPercentualDesconto(produto.preco_venda, produto.preco_desconto);
      produto.preco_final = (produto.preco_venda - produto.preco_desconto).toFixed(2);
    },

    calcularPorValorFinal(index) {
      const produto = this.produtos_pedido[index];

      produto.preco_desconto = (produto.preco_venda - produto.preco_final).toFixed(2);
      produto.porcentagem_desconto = this.calcularPercentualDesconto(produto.preco_venda, produto.preco_desconto);
    },

    formatPreco(value) {
      const num = parseFloat(value);
      if (isNaN(num)) {
        return "0,00";
      }
      return num.toFixed(2).replace('.', ',');
    },

    calcularPercentualDesconto(precoVenda, precoDesconto) {
      if (!precoDesconto || precoDesconto === precoVenda) return 0;
      const desconto = ((precoVenda - (precoVenda-precoDesconto)) / precoVenda)*100;
      return desconto.toFixed(0);
    },
    abrirModal(index) {
      this.produto_original = { ...this.produtos_pedido[index] };
      const modal = new bootstrap.Modal(document.getElementById(`desconto-produto-${index}`));
      modal.show();
    },

    cancelarAlteracoes(index) {
      this.produtos_pedido[index] = { ...this.produto_original };
    },

    salvarAlteracoes(index) {
      const modal = bootstrap.Modal.getInstance(document.getElementById(`desconto-produto-${index}`));
      this.somaProduto();
      modal.hide();
    },

    abrirModalExclusao(index) {
      this.produto_para_excluir = index;
      const modalExclusao = new bootstrap.Modal(document.getElementById(`abrirModalExclusao-${index}`));
      modalExclusao.show();
    },

    confirmarExclusao(index) {
      if (this.produto_para_excluir !== null) {
        this.produtos_pedido.splice(this.produto_para_excluir, 1);
        const modalExclusao = bootstrap.Modal.getInstance(document.getElementById(`abrirModalExclusao-${index}`));
        modalExclusao.hide();
        this.somaProduto();
        this.produto_para_excluir = null;
      }
      const modalExclusao = bootstrap.Modal.getInstance(document.getElementById(`abrirModalExclusao-${index}`));
      modalExclusao.hide();
    }, 
  },
};
</script>

<style scoped>
  .card-body {
    height: 22.8rem;
  }

  .custom-table {
    width: 100%;
  }

  .product-separator {
    border-bottom: 2px solid #dee2e6;
  }

  .btn-sm{
    padding-left: 10PX;
    padding: .1rem .4rem;
    font-size: 0.8rem;
  }

  .bi-plus-slash-minus{
    font-weight: bold;
  }

</style>