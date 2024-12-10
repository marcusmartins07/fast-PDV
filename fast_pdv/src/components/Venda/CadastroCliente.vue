<template>
<div>
    <div data-bs-toggle="modal" data-bs-target="#cadastrarCliente">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-plus-fill" viewBox="0 0 16 16">
            <path d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
            <path fill-rule="evenodd" d="M13.5 5a.5.5 0 0 1 .5.5V7h1.5a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0V8h-1.5a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5"/>
        </svg> Cadastrar Cliente
    </div>

    <div class="modal fade" id="cadastrarCliente" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="cadastrarClienteLabel">Cadastrar Cliente</h5>
            </div>
            <div class="modal-body">
                <div class="row g-1 mb-3">
                    <div class="col col-lg-4">
                        <div class="form-floating mx-1 row">
                            <input type="text" class="form-control col" id="cpf-cadastro" v-mask="'###.###.###-##'" v-model="novo_cliente.cpf"/>
                            <label for="cpf-cadastro">CPF</label>
                        </div>
                    </div>
                    <div class="col-md">
                        <div class="form-floating">
                            <input type="text" class="form-control" id="nome-cadastro" v-model="novo_cliente.nome"/>
                            <label for="nome-cadastro">Nome Completo</label>
                        </div>
                    </div>
                    </div>
                    <div class="row g-1 mb-3">
                        <div class="col-md">
                            <div class="form-floating">
                                <input type="date" class="form-control col" id="nascimento-cadastro" v-model="novo_cliente.data_nascimento"/>
                                <label for="nascimento-cadastro">Data de Nascimento</label>
                            </div>
                        </div>
                    <div class="col-md">
                        <div class="form-floating">
                        <select class="form-select" id="floatingSelectGrid" v-model="novo_cliente.genero">
                            <option value="">Selecione um gênero</option>
                            <option v-for="genero in generos" :key="genero.id_genero" :value="genero.id_genero" >{{ genero.genero }}</option>
                        </select>
                        <label for="floatingSelectGrid">Gênero</label>
                        </div>
                    </div>
                    <div class="col-md">
                        <form @submit.prevent="cep_cadastro_cliente">
                            <div class="form-floating col-md">
                                <input type="text" v-model="cep_cadastro_cliente" class="form-control" id="cep-cadastro" placeholder="CEP" v-mask="'#####-###'" @blur="buscaCEP"/>
                                <label for="cep-cadastro">CEP</label>
                            </div>
                        </form>
                    </div>
                    </div>
                    <div class="row g-1 mb-3">
                    <div class="form-floating col-8">
                        <input type="text" class="form-control" id="endereco-cadastro" placeholder="endereco" v-model="novo_cliente.endereco"/>
                        <label for="endereco-cadastro">Endereço</label>
                    </div>
                    <div class="form-floating col-4">
                        <input type="text" class="form-control" id="numero-cadastro" placeholder="Numero" v-model="novo_cliente.numero">
                        <label for="numero-cadastro">Número</label>
                    </div>
                    </div>
                    <div class="row g-1 mb-3">
                    <div class="form-floating col-md-4">
                        <input type="text" class="form-control" id="bairro-cadastro" placeholder="Bairro" v-model="novo_cliente.bairro"/>
                        <label for="bairro-cadastro">Bairro</label>
                    </div>
                    <div class="form-floating col-md-6">
                        <input type="text" class="form-control" id="cidade-cadastro" placeholder="Cidade" v-model="novo_cliente.cidade"/>
                        <label for="cidade-cadastro">Cidade</label>
                    </div>
                    <div class="form-floating col-md-2">
                        <select class="form-select" id="floatingSelectGrid" v-model="novo_cliente.uf_estado">
                        <option v-for="estado in estados" :key="estado.uf" :value="estado.uf" >{{ estado.uf }}</option>
                        </select>
                        <label for="floatingSelectGrid">UF</label>
                    </div>    
                </div>
                <div class="row g-1 mb-3">
                    <div class="form-floating col-md">
                        <input type="text" class="form-control" id="email-cadastro" placeholder="E-mail" v-model="novo_cliente.email"/>
                        <label for="email-cadastro">E-mail</label>
                    </div>
                    <div class="form-floating col-md">
                        <input type="text" class="form-control" id="telefone-cadastro" placeholder="Telefone/Celular" v-mask="'(##) 9 #### ####'" v-model="novo_cliente.tel_celular"/>
                        <label for="telefone-cadastro">Telefone/Celular</label>
                    </div>
                </div>
            </div>
            <div class="modal-footer d-flex justify-content-between">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancelar</button>
                <button class="btn btn-bd-primary" type="submit" id="button-addon2" @click.prevent="enviarCliente">Salvar</button>
            </div>
            </div>
        </div>
    </div>
</div>
</template>
    
<script>
import Spinner from '../Utilities/Spinner.vue';
import eventBus from '@/utils/eventBus';

export default {
    name: "CadastroCliente",
    components: {
        Spinner
    },
    data() {
        return{
            estados: [],
            generos: [],
            cep_cadastro_cliente:'',
            novo_cliente : {},
        };
    },
    mounted() {
        this.buscarEstados();
        this.buscarGeneros();
    },
    methods: {
        async buscarEstados() {
            try {
                const req = await fetch('http://127.0.0.1:8000/api/v1/estados/');
                const data = await req.json();
                this.estados = Array.isArray(data.results) ? data.results : [];
            } catch (error) {
                eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar estados: ${error}`});
            }
        },
        async buscarGeneros() {
            try {
                const req = await fetch('http://127.0.0.1:8000/api/v1/generos/');
                const data = await req.json();
                this.generos = Array.isArray(data.results) ? data.results : [];
            } catch (error) {
                eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar generos: ${error}`});
            }
        },
        async buscaCEP() {
            eventBus.emit('loading', true);
            try {
                const req = await fetch(`https://viacep.com.br/ws/${this.cep_cadastro_cliente}/json/`);
                if (!req.ok) {
                if (req.status === 404) {
                    eventBus.emit('show-alert', { type: 'danger', message: 'CEP não encontrado.' });
                } else {
                    eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar CEP: ${req.statusText}` });
                }
                }
                
                const data = await req.json();

                this.novo_cliente = {
                ...this.novo_cliente,
                cep: data.cep,
                endereco: data.logradouro,
                bairro: data.bairro,
                cidade: data.localidade,
                uf_estado: data.uf,
                };
                eventBus.emit('show-alert', { type: 'success', message: 'CEP encontrado!'});
            } catch (error) {
                eventBus.emit('show-alert', { type: 'danger', message: 'Erro ao buscar CEP: ${error}' });
            } finally {
                eventBus.emit('loading', false);
            }
        },

        async enviarCliente() {
            try {
                const clienteFormatado = {
                    ...this.novo_cliente,
                    cpf: (this.novo_cliente.cpf ?? '').replace(/[.-]/g, ''), 
                    cep: (this.novo_cliente.cep ?? '').replace(/-/g, ''), 
                    tel_celular: (this.novo_cliente.tel_celular ?? '').replace(/[\(\)\s-]/g, ''), 
                    
                };

                const req =  await this.$RequisicaoAutenticada('http://127.0.0.1:8000/api/v1/clientes/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(clienteFormatado),
                });
                
                if (!req.ok) {
                    const errorData = await req.json(); 
                    eventBus.emit('show-alert', { type: 'danger', message: `Erro ao enviar cliente: ${req.statusText} - ${JSON.stringify(errorData)}`});
                }

                const data = await req.json();
                eventBus.emit('show-alert', { type: 'success', message: 'Cliente cadastrado com sucesso!' });

                const modal_cadastro = bootstrap.Modal.getInstance(document.getElementById(`cadastrarCliente`));
                modal_cadastro.hide();
                
                this.novo_cliente = {};
                this.cep_cadastro_cliente = '';

            } catch (error) {
                eventBus.emit('show-alert', { type: 'danger', message: `Erro ao cadastrar cliente: ${error.message}` });
            }
        },

    }

}

</script>
    
<style scoped>

    #cadastrarCliente {
        color: black;
    }

    .modal-header{
        justify-content: space-evenly;
    }
    

</style>
    