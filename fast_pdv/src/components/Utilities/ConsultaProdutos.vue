<template>
<div>
  <div class="modal fade" id="consultaProduto" tabindex="-1" aria-labelledby="consultaProdutoLabel" aria-hidden="true">
    <div class="modal-dialog modal-fullscreen">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="consultaProdutoLabel">Consultar Produtos</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row row-cols-1 row-cols-md-5 g-4">
            <div v-for="produto in produtos_buscados" :key="produto.id" class="col">
              <div class="card h-100">
                <div class="card-body">
                  <h5 class="card-title">{{ produto.nome }}</h5>
                  <div class="card-text"><span class="fw-bold">Descrição: </span>{{ produto.descricao }}</div>
                  <div class="card-text"><span class="fw-bold">Categoria: </span>{{ produto.categoria }}</div>
                  <div class="card-text"><span class="fw-bold">Quantidade: </span>{{ produto.estoque }}</div>
                  <div class="card-text"><span class="fw-bold">Código: </span>{{ produto.codigo_barras }}</div>
                  <div class="card-text fw-bold mt-1">R$ {{formatPreco(produto.preco_venda)}}</div>
                </div>
                <div class="card-footer text-center">
                  <button class="btn btn-bd-primary" @click="copiarCodigo(produto.codigo_barras)">Copiar Código</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <div class="pagination">
            <button class="btn btn-bd-primary me-2" :disabled="!previous" @click="consultarProdutos(previous)">Página Anterior</button>
            <button class="btn btn-bd-primary me-2" :disabled="!next" @click="consultarProdutos(next)">Próxima Página</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="d-flex flex-column">
    <div class="d-grid gap-2 mt-auto">
      <div  class="btn btn-bd-primary" type="button" @click="abrirModal">Consultar Produtos</div>
    </div>
  </div>
</div>

</template>

<script>
import Spinner from "../Utilities/Spinner.vue";
import eventBus from "@/utils/eventBus";

export default {
  name: "ConsultaProdutos",
  components: {
    Spinner,
  },
  data() {
    return {
      produtos_buscados: [],
      next: null, 
      previous: null 
    };
  },
  mounted() {
    this.consultarProdutos();
  },
  
  methods: {
    abrirModal() {
      const modal = new bootstrap.Modal(document.getElementById('consultaProduto'), {
        backdrop: 'static', 
        keyboard: false 
      });
      modal.show();
      document.querySelectorAll('.modal-backdrop').forEach(backdrop => backdrop.remove());
    },

    async consultarProdutos(url = "http://127.0.0.1:8000/api/v1/produto/") {
      try {
        const req = await this.$RequisicaoAutenticada(url);

        if (!req.ok) {
          eventBus.emit("show-alert", {
          type: "danger",
          message: `Erro HTTP: ${req.status} - ${req.statusText}`,
        });
        }

        const data = await req.json();
        this.produtos_buscados = data.results;
        this.next = data.next;
        this.previous = data.previous;
        
      } catch (error) {
        eventBus.emit("show-alert", {
          type: "danger",
          message: `Erro ao buscar os produtos: ${error.message}`,
        });
      }
    },
    formatPreco(value) {
      const num = parseFloat(value);
      if (isNaN(num)) {
        return "0,00";
      }
      return num.toFixed(2).replace('.', ',');
    },

    copiarCodigo(produto_codigo_barras){
      navigator.clipboard
        .writeText(produto_codigo_barras)
        .then(() => {
            eventBus.emit("show-alert", {
              type: "success",
              message: `Código ${produto_codigo_barras} copiado com sucesso!`,
            });
          })
    }

}
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
