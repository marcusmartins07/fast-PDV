<template>
  <div class="container">
    <Navbar />
    <Alert />
    <div class="d-flex flex-column justify-content-center align-items-center vh-100">
      <div class="row w-100 mt-4">
        <div class="col-6"> <Cliente /> </div>
        <div class="col-6"> <Produto @atualizarProdutos="atualizarProdutos" /></div>
      </div>
      <div class="mt-2 w-100 d-flex justify-content-end">
        <button class="btn btn-bd-primary" :disabled="produtos_pedido.length === 0" @click="irParaPagamento">
          Continuar para Pagamento
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-arrow-right-circle" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"/>
          </svg>
        </button>
      </div>
    </div>
    <Spinner />
  </div>
</template>

  
  <script>
    import Produto from "../components/Venda/Produto.vue";
    import Cliente from "../components/Venda/Cliente.vue";
    import Spinner from "../components/Utilities/Spinner.vue";
    import Alert from "../components/Utilities/Alert.vue";
    import Navbar from "@/components/Utilities/Navbar.vue";

    export default {
      name: "Home",
      components: {
        Produto,
        Cliente,
        Spinner,
        Alert,
        Navbar,
      },
      data() {
        return {
          cliente: null,
          produtos_pedido: [],
        };
      },
      
      methods: {
        async atualizarProdutos(produtos) {
          this.produtos_pedido = produtos;
        },
        irParaPagamento() {
          this.$router.push({ name: 'Pedido' });
        }
      },
    };
</script>

<style scoped>

body {
  padding-top: 100px;
}

.btn-bd-primary{
  margin-right: 15px;
}

.bi-arrow-right-circle {
    vertical-align: sub;
}


</style>