<template>
  <div>
    <div class="modal fade" id="cancelarVenda" tabindex="-1" aria-labelledby="cancelarVendaLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="cancelarVendaLabel">Cancelar Venda</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <form @submit.prevent="validarSenha">
            <div class="modal-body">
              <p class="mx-1">Tem certeza que deseja cancelar a venda?</p>
              <div class="form-floating mx-1">
                <input type="password" class="form-control col" id="floatingInput" v-model="senha" required/>
                <label for="floatingInput">Senha</label>
              </div>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-bd-primary">Confirmar</button> 
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="d-flex flex-column">
      <div class="d-grid gap-2 mt-auto">
        <button class="btn btn-bd-primary" type="button" :disabled="disabled" @click="abrirModal">Cancelar Venda Atual</button>
      </div>
    </div>
  </div>  
</template>
  
  <script>
  import Spinner from "../Utilities/Spinner.vue";
  import eventBus from "@/utils/eventBus";
  
  export default {
    name: "CancelarVenda",
    data() {
      return {
        senha: '',       
        mensagem: '',      
        sucesso: false,    
      };
    },
    components: {
      Spinner,
    },
    props: {
      disabled: {
        type: Boolean,
        default: false,
      },
    },
    methods: {
    abrirModal() {
      const modal = new bootstrap.Modal(document.getElementById('cancelarVenda'), {
        backdrop: 'static', 
        keyboard: false    
      });
      modal.show();
      document.querySelectorAll('.modal-backdrop').forEach(backdrop => backdrop.remove());
    },
    async validarSenha() {
      const resultado = await this.$ValidarSenha(this.senha);
        if (resultado.success){
        localStorage.removeItem("cliente_selecionado");
        localStorage.removeItem("produtos_pedido");
        localStorage.removeItem("forma_pagamento_pedido");
        localStorage.removeItem("valores_pagos_pedidos");
        window.location.reload();
        eventBus.emit('show-alert', { type: 'success', message: resultado.message });
      } else {
        eventBus.emit('show-alert', { type: 'danger', message: resultado.message });
      }
    },
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
  
  </style>
  