<template>
    <nav class="navbar fixed-top navbar">
    <div class="container-fluid">
        <button class="navbar-toggler btn-bd-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" @click="atualizarQuantidadeProduto">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="white" class="bi bi-list" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
            </svg>
        </button>
        <img class="navbar-brand me-auto ms-3" id="fast_logo_branco" src="/image/fast_logo_branco.png" alt="fast_logo_branco">
        
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title ms-3" id="offcanvasNavbarLabel">Menu</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="d-flex flex-column">
                <div class="d-grid gap-2 mt-auto mx-3">
                  <div class="card mb-3">
                    <h5 class="card-body text-center text-light">
                      <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                      </svg>
                      {{ usuario_logado.first_name }} {{ usuario_logado.last_name }}
                    </h5>
                  </div>
                    <router-link to="/" class="btn btn-bd-primary" type="button">Venda</router-link>
                    <button to="/pedido" class="btn btn-bd-primary" :disabled="possui_produto == false" @click="irParaPagamento">Pedido</button>
                    <ConsultaProdutos/>
                    <ReimprimirVenda/>
                    <CancelarVenda :disabled="possui_produto == false"/>
                </div>
            </div>
            <div class="offcanvas-body d-flex flex-column">
                <div class="d-grid gap-2 mt-auto">
                    <button class="btn btn-danger" type="button" @click="fazerLogout">Sair</button>
                </div>
            </div>
        </div>
    </div>
</nav>

</template>

<script>
import Spinner from '../Utilities/Spinner.vue';
import eventBus from '@/utils/eventBus';
import ConsultaProdutos from '../Utilities/ConsultaProdutos.vue';
import CancelarVenda from './CancelarVenda.vue';
import ReimprimirVenda from './ReimprimirVenda.vue';

export default {
  name: "Navbar",
  components: {
    Spinner,
    ConsultaProdutos,
    CancelarVenda,
    ReimprimirVenda,
  },
  data() {
    return {
      produtos_pedido: [],
      usuario_logado: {},
      possui_produto: false,
    };
  },
  mounted() {
    this.buscarUsuarioLogado();
  },

  methods: {
    fazerLogout () {
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      localStorage.removeItem("clienteSelecionado");
      localStorage.removeItem("produtosPedido");
      this.$router.push({ name: "Home" });
    },
    async atualizarQuantidadeProduto() {
      const produtosStorage = localStorage.getItem('produtosPedido');
      const produtosPedido = JSON.parse(produtosStorage);
      if(!produtosPedido || produtosPedido.length === 0){
          this.possui_produto = false
        }
        else {
          this.possui_produto = true
          this.produtos_pedido = produtosPedido
        }
      
    },
    irParaPagamento() {
      this.$router.push({ name: 'Pedido' });
    },
    async buscarUsuarioLogado() {
      try {
        const response = await this.$RequisicaoAutenticada('http://127.0.0.1:8000/api/v1/usuarios/me/');
        this.usuario_logado = await response.json();
      } catch (error) {
        eventBus.emit("show-alert", {
          type: "danger",
          message: `Erro ao buscar usuário logado: ${error.message}`,
        });
      }
    }
  }
}

</script>


<style scoped>

.navbar {
    background-color: var(--bd-violet-bg);
}

#fast_logo_branco {
    height: 2.5rem;
}

.navbar-toggler {
  outline: white; 
  box-shadow: white;
}

.navbar-toggler:focus {
  outline: none;
  box-shadow: none;
}

.card {
  background-color: var(--bd-violet-bg);
}

.bi-person-circle {
    vertical-align: sub;
    margin-right: 0.3rem;
}
</style>