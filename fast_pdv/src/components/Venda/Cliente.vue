<template>
  <div class="container=sm">
    <div class="card">
      <div class="card-header text-center h6">Cliente</div>
      <div class="card-body">
        <div class="row g-1 mb-3">
          <div class="col col-lg-3">
            <div class="form-floating mx-1 row">
              <input type="text" v-model="cliente_id" class="form-control" id="cliente-codigo" placeholder="Código" @blur="buscarClientePorId" :disabled="input_disabled"/>
              <label for="cliente-codigo">Código</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating mx-1 row">
              <input type="text" v-model="cpf_cliente" class="form-control col" id="cliente-cpf" v-mask="'###.###.###-##'" placeholder="CPF" @blur="buscarClientePorCPF" :disabled="input_disabled"/>
              <label for="cliente-cpf">CPF</label>
            </div>
          </div>
        </div>
        <div class="form-floating mb-3">
          <input
            type="text"
            class="form-control"
            id="cliente-nome"
            placeholder="Fulano de Ciclano"
            v-model="cliente.nome"
            disabled
          />
          <label for="cliente-nome">Nome Completo</label>
        </div>
        <div class="row g-1 mb-3">
          <div class="col-md">
            <div class="form-floating">
              <input
                type="date"
                class="form-control col"
                id="cliente-nascimento"
                placeholder="01/01/2001"
                v-model="cliente.data_nascimento"
                disabled
              />
              <label for="cliente-nascimento">Data de Nascimento</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <select class="form-select" id="floatingSelectGrid" v-model="cliente.genero" disabled>
                <option value="">Selecione um gênero</option>
                <option value="M">Masculino</option>
                <option value="F">Feminino</option>
                <option value="I">Indefinido</option>
              </select>
              <label for="floatingSelectGrid">Gênero</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating col-md">
              <input type="text" class="form-control" id="cliente-cep" placeholder="CEP" v-model="cliente.cep" v-mask="'#####-###'" disabled/>
              <label for="cliente-cep">CEP</label>
            </div>
          </div>
        </div>
        <div class="row g-1 mb-3">
          <div class="form-floating col-8">
            <input type="text" class="form-control" id="cliente-endereco" placeholder="endereco" v-model="cliente.endereco" disabled/>
            <label for="cliente-endereco">Endereço</label>
          </div>
          <div class="form-floating col-4">
            <input
              type="text"
              class="form-control"
              id="cliente-numero"
              placeholder="Numero"
              v-model="cliente.numero"
              disabled
            />
            <label for="cliente-numero">Número</label>
          </div>
        </div>
        <div class="row g-1 mb-3">
          <div class="form-floating col-md-4">
            <input type="text" class="form-control" id="cliente-bairro" placeholder="Bairro" v-model="cliente.bairro" disabled/>
            <label for="cliente-bairro">Bairro</label>
          </div>
          <div class="form-floating col-md-6">
            <input type="text" class="form-control" id="cliente-cidade" placeholder="Cidade" v-model="cliente.cidade" disabled/>
            <label for="cliente-cidade">Cidade</label>
          </div>
          <div class="form-floating col-md-2" v-if="cliente.genero != null">
              <select class="form-select" id="floatingSelectGrid" v-model="cliente.uf_estado" disabled>
                  <option v-for="estado in estados" :key="estado.uf" :value="estado.uf" >{{ estado.uf }}</option>
              </select>
              <label for="floatingSelectGrid">UF</label>
          </div>
        </div>
        <div class="row g-1">
          <div class="form-floating col-md">
            <input type="text" class="form-control" id="cliente_email" placeholder="E-mail" v-model="cliente.email" disabled/>
            <label for="cliente_email">E-mail</label>
          </div>
          <div class="form-floating col-md">
            <input type="text" class="form-control" id="cliente-tel-celular" placeholder="Telefone/Celular" v-mask="'(##) 9 #### ####'" v-model="cliente.tel_celular" disabled/>
            <label for="cliente-tel-celular">Telefone/Celular</label>
          </div>
        </div>
      </div>
      <div class="card-footer">
        <div class="row my-1">
          <button class="col mx-1 btn btn-bd-primary"><CadastroCliente/></button>
          <button class="col mx-1 btn btn-bd-primary" :disabled="input_disabled == false"><AtualizarCliente :cliente="cliente"/></button>
          <button class="col mx-1 btn btn-bd-primary" @click.prevent="limpaCliente" :disabled="input_disabled == false" >
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill-x" viewBox="0 0 16 16">
              <path d="M11 5a3 3 0 1 1-6 0 3 3 0 0 1 6 0m-9 8c0 1 1 1 1 1h5.256A4.5 4.5 0 0 1 8 12.5a4.5 4.5 0 0 1 1.544-3.393Q8.844 9.002 8 9c-5 0-6 3-6 4"/>
              <path d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7m-.646-4.854.646.647.646-.647a.5.5 0 0 1 .708.708l-.647.646.647.646a.5.5 0 0 1-.708.708l-.646-.647-.646.647a.5.5 0 0 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 .708-.708"/>
            </svg>
            Limpar Cliente
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import Spinner from '../Utilities/Spinner.vue';
import eventBus from '@/utils/eventBus';
import CadastroCliente from './CadastroCliente.vue';
import AtualizarCliente from './AtualizarCliente.vue';

export default {
  name: "Cliente",
  components: {
    Spinner,
    CadastroCliente,
    AtualizarCliente,
  },
  data() {
    return {
      cliente: '',
      cpf_cliente: '',
      cpf_limpo: '',
      cliente_id: '',
      estados: [],
      input_disabled: false,
    };
  },
  mounted() {
    this.buscarCliente();
    this.buscarEstados();
  },
  methods: {

    async buscarCliente (){
      const clienteStorage = localStorage.getItem('clienteSelecionado');

      if (clienteStorage) {
        this.cliente = JSON.parse(clienteStorage);
        this.cliente_id = this.cliente.cliente_id
        this.cpf_cliente = this.cliente.cpf
        this.input_disabled = true
        console.log(this.input_disabled)
      }
    },  


    async limpaCliente(){
      this.cliente = '',
      this.cpf_cliente = '',
      this.cpf_limpo = '',
      this.cliente_id = '',
      this.input_disabled = false
      localStorage.removeItem('clienteSelecionado');
    },

    async buscarEstados() {
        try {
            const req = await fetch('http://127.0.0.1:8000/api/v1/estados/');
            const data = await req.json();
            this.estados = Array.isArray(data.results) ? data.results : [];
        } catch (error) {
            eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar estados: ${error}` });
        }
    },

    async buscaCPF() {
      eventBus.emit('loading', true);
      try {
        const req = await this.$RequisicaoAutenticada(`http://127.0.0.1:8000/api/v1/clientes/buscar_por_cpf/?cpf=${this.cpf_cliente}`);
        
        // Verifica resposta
        if (!req.ok) {
          if (req.status === 404) {
            eventBus.emit('show-alert', { type: 'danger', message: 'Cliente não encontrado.' });
          } else {
            eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar cliente: ${req.statusText}` });
          }
          this.limpaCliente()
          return;
        }
        
        const data = await req.json();
        this.cliente = data;
        this.cliente_id = this.cliente.cliente_id
        this.input_disabled = true
        localStorage.setItem('clienteSelecionado', JSON.stringify(this.cliente));
        eventBus.emit('show-alert', { type: 'success', message: 'Cliente encontrado!'});
      } catch (error) {
        this.cliente = null;
      } finally {
        eventBus.emit('loading', false);
      }
    },
    async buscaId() {
      try {
        const req = await this.$RequisicaoAutenticada(`http://127.0.0.1:8000/api/v1/clientes/${this.cliente_id}`);
        if (!req.ok) {
          if (req.status === 404) {
            eventBus.emit('show-alert', { type: 'danger', message: 'Cliente não encontrado.' });
          } else {
            eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar cliente: ${req.statusText}` });
          }
          this.limpaCliente()
          return;
        }
        
        const data = await req.json();
        this.cliente = data;
        this.cpf_cliente = this.cliente.cpf
        this.input_disabled = true
        localStorage.setItem('clienteSelecionado', JSON.stringify(this.cliente));
        
      } catch (error) {
        eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar o cliente: ${error}` });
        this.cliente = null;
      }
    },

    async buscarClientePorCPF() {
      this.cpf_cliente = String(this.cpf_cliente).replace(/\D/g, '');
      if (this.cpf_cliente.length === 11) {
        await this.buscaCPF();
      } else if (this.cpf_cliente.length != 0) {
        this.limpaCliente()
        eventBus.emit('show-alert', { type: 'danger', message: 'Erro ao buscar o cliente' });
      }
    },
    async buscarClientePorId(){
      if (this.cliente_id.length != 0) {
        await this.buscaId();
      }
    }
  }
};

</script>

<style scoped>
</style>