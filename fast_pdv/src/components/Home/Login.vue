<template>
    <div class="container mt-2">
      <div
        class="modal fade"
        id="loginModal"
        tabindex="-1"
        aria-labelledby="loginModalLabel"
        aria-hidden="true"
        data-bs-backdrop="static"
        data-bs-keyboard="false"
      >
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header d-flex justify-content-center">
              <img class="navbar-brand" id="fast_logo_branco" src="/image/fast_logo_purple-2.png" alt="fast_logo_branco">
            </div>
  
            <form @submit.prevent="login">
              <div class="modal-body">
                <div class="form-floating mb-3">
                  <input type="text" v-model="username" class="form-control" id="username" placeholder="Usuário" required>
                  <label for="floatingInput">Usuário</label>
                </div>
                <div class="form-floating">
                  <input type="password" v-model="password" class="form-control" id="password" placeholder="Senha" required>
                  <label for="floatingPassword">Senha</label>
                </div>
              </div>
              <div class="modal-footer d-flex justify-content-center">
                
                <div class="d-grid gap-2 col-3 mx-auto">
                  <button type="submit" class="btn btn-bd-primary">Entrar</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Spinner from "../Utilities/Spinner.vue";
  import Alert from "../Utilities/Alert.vue";
  import eventBus from '@/utils/eventBus';
  
  export default {
    name: "Login",
    components: {
      Spinner,
      Alert,
    },
    data() {
      return {
        username: "",
        password: "",
        error_message: null,
        login_modal_instance: null,
      };
    },
    mounted() {
      const token = localStorage.getItem("access_token");
      if (!token) {
        const modalElement = document.getElementById("loginModal");
        this.login_modal_instance = new bootstrap.Modal(modalElement);
        this.login_modal_instance.show();
      }
    },
    methods: {
      async login() {
        try {
          const response = await fetch("http://127.0.0.1:8000/api/token/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              username: this.username,
              password: this.password,
            }),
          });
  
          if (!response.ok) {
            eventBus.emit('show-alert', { type: 'danger', message: `Falha ao autenticar. Verifique as credenciais.`});
          }
  
          const data = await response.json();
          localStorage.setItem("access_token", data.access);
          localStorage.setItem("refresh_token", data.refresh);
          
          if (this.login_modal_instance) {
            this.login_modal_instance.hide();
          }
  
          this.$router.push({ name: "Venda" });
        } catch (error) {
          eventBus.emit('show-alert', { type: 'danger', message: 'Usuário ou senha inválidos. Tente novamente!'});
        }
      },
    },
  };
  </script>
  
  <style scoped>
  
  #fast_logo_branco {
      height: 4rem;
  }
  
  
  </style>
  