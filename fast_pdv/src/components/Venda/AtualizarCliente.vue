<template>
    <div>
        <div data-bs-toggle="modal" data-bs-target="#atualizarCliente">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                class="bi bi-person-fill-up" viewBox="0 0 16 16">
                <path
                    d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7m.354-5.854 1.5 1.5a.5.5 0 0 1-.708.708L13 11.707V14.5a.5.5 0 0 1-1 0v-2.793l-.646.647a.5.5 0 0 1-.708-.708l1.5-1.5a.5.5 0 0 1 .708 0M11 5a3 3 0 1 1-6 0 3 3 0 0 1 6 0" />
                <path
                    d="M2 13c0 1 1 1 1 1h5.256A4.5 4.5 0 0 1 8 12.5a4.5 4.5 0 0 1 1.544-3.393Q8.844 9.002 8 9c-5 0-6 3-6 4" />
            </svg> Atualizar Cliente
        </div>

        <div class="modal fade" id="atualizarCliente" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
            aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="atualizarClienteLabel">Atualizar Dados do Cliente</h5>
                    </div>
                    <div class="modal-body">
                        <div class="row g-1 mb-3">
                            <div class="col col-lg-3">
                                <div class="form-floating mx-1 row">
                                    <input type="text" v-model="cliente_atualizar.cliente_id" class="form-control" id="codigo-atualizar" placeholder="Código"/>
                                    <label for="codigo-atualizar">Código</label>
                                </div>
                            </div>
                            <div class="col-md">
                                <div class="form-floating mx-1 row">
                                    <input type="text" v-model="cliente_atualizar.cpf" class="form-control col"
                                        id="cpf-atualizar" v-mask="'###.###.###-##'" placeholder="CPF"/>
                                    <label for="cpf-atualizar">CPF</label>
                                </div>
                            </div>
                        </div>
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" id="nome-atualizar" placeholder="Fulano de Ciclano"
                                v-model="cliente_atualizar.nome" />
                            <label for="nome-atualizar">Nome Completo</label>
                        </div>
                        <div class="row g-1 mb-3">
                            <div class="col-md">
                                <div class="form-floating">
                                    <input type="date" class="form-control col" id="nascimento-atualizar"
                                        placeholder="01/01/2001" v-model="cliente_atualizar.data_nascimento" />
                                    <label for="nascimento-atualizar">Data de Nascimento</label>
                                </div>
                            </div>
                            <div class="col-md">
                                <div class="form-floating">
                                    <select class="form-select" id="floatingSelectGrid" v-model="cliente_atualizar.genero">
                                        <option value="">Selecione um gênero</option>
                                        <option v-for="genero in generos" :key="genero.id_genero" :value="genero.id_genero" >{{ genero.genero }}</option>
                                    </select>
                                    <label for="floatingSelectGrid">Gênero</label>
                                </div>
                            </div>
                            <div class="col-md">
                                <div class="form-floating col-md">
                                    <input type="text" class="form-control" id="cep-atualizar" placeholder="CEP"
                                        v-model="cliente_atualizar.cep" v-mask="'#####-###'" />
                                    <label for="cep-atualizar">CEP</label>
                                </div>
                            </div>
                        </div>
                        <div class="row g-1 mb-3">
                            <div class="form-floating col-8">
                                <input type="text" class="form-control" id="endereco-atualizar" placeholder="endereco"
                                    v-model="cliente_atualizar.endereco" />
                                <label for="endereco-atualizar">Endereço</label>
                            </div>
                            <div class="form-floating col-4">
                                <input type="text" class="form-control" id="numero-atualizar" placeholder="Numero"
                                    v-model="cliente_atualizar.numero" />
                                <label for="numero-atualizar">Número</label>
                            </div>
                        </div>
                        <div class="row g-1 mb-3">
                            <div class="form-floating col-md-4">
                                <input type="text" class="form-control" id="bairro-atualizar" placeholder="Bairro"
                                    v-model="cliente_atualizar.bairro" />
                                <label for="bairro-atualizar">Bairro</label>
                            </div>
                            <div class="form-floating col-md-6">
                                <input type="text" class="form-control" id="cidade-atualizar" placeholder="Cidade"
                                    v-model="cliente_atualizar.cidade" />
                                <label for="cidade-atualizar">Cidade</label>
                            </div>
                            <div class="form-floating col-md-2" v-if="cliente_atualizar.genero != null">
                                <select class="form-select" id="floatingSelectGrid" v-model="cliente_atualizar.uf_estado">
                                    <option v-for="estado in estados" :key="estado.uf" :value="estado.uf" >{{ estado.uf }}</option>
                                </select>
                                <label for="floatingSelectGrid">UF</label>
                            </div>
                        </div>
                        <div class="row g-1 mb-3">
                            <div class="form-floating col-md">
                                <input type="text" class="form-control" id="email-atualizar" placeholder="E-mail"
                                    v-model="cliente_atualizar.email" />
                                <label for="email-atualizar">E-mail</label>
                            </div>
                            <div class="form-floating col-md">
                                <input type="text" class="form-control" id="celular-atualizar"
                                    placeholder="Telefone/Celular" v-mask="'(##) 9 #### ####'"
                                    v-model="cliente_atualizar.tel_celular" />
                                <label for="celular-atualizar">Telefone/Celular</label>
                            </div>
                        </div>
                        <div class="modal-footer d-flex justify-content-between">
                            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancelar</button>
                            <button class="btn btn-bd-primary" type="submit" @click.prevent="atualizarCliente">Salvar Alterações</button>
                        </div>
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
        name: "AtualizarCliente",
        components: {
            Spinner
        },
        data() {
            return {
                estados: [],
                generos: [],
                cliente_atualizar: {},
            };
        },
        props: {
            cliente: {
                type: Object,
                required: true
            }
        },
        mounted() {
            this.buscarEstados();
            this.buscarGeneros();
        },
        watch: {
            cliente: {
                handler(newCliente) {
                    this.cliente_atualizar = { ...newCliente };
                },
                immediate: true,
                deep: true
            }
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

            async buscarCEP() {
                try {
                    const req = await fetch(`https://viacep.com.br/ws/${this.cliente_atualizar.cep}/json/`);
                    const data = await req.json();
                    this.cliente_atualizar.endereco = data.logradouro;
                    this.cliente_atualizar.bairro = data.bairro;
                    this.cliente_atualizar.cidade = data.localidade;
                    this.cliente_atualizar.ufEstado = data.uf;
                } catch (error) {
                    eventBus.emit('show-alert', { type: 'danger', message: `Erro ao buscar CEP: ${error}`});
                }
            },

            async atualizarCliente() {
                try {
                    const clienteFormatado = {
                        ...this.cliente_atualizar,
                        cpf: (this.cliente_atualizar.cpf ?? '').replace(/[.-]/g, ''), 
                        cep: (this.cliente_atualizar.cep ?? '').replace(/-/g, ''), 
                        tel_celular: (this.cliente_atualizar.tel_celular ?? '').replace(/[\(\)\s-]/g, ''), 
                        
                    };

                    const req = await fetch(`http://127.0.0.1:8000/api/v1/clientes/${this.cliente_atualizar.cliente_id}/`, {
                        method: 'PUT', 
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
                    
                    eventBus.emit('show-alert', { type: 'success', message: 'Cliente atualizado com sucesso!' });
                    const atualizarCliente = bootstrap.Modal.getInstance(document.getElementById(`atualizarCliente`));
                    localStorage.setItem('clienteSelecionado', JSON.stringify(clienteFormatado));
                    atualizarCliente.hide();

                } catch (error) {
                    eventBus.emit('show-alert', { type: 'danger', message: `Erro ao atualizar cliente: ${error.message}` });
                }
            }
        }
    };
</script>

<style scoped>
    #atualizarCliente {
        color: black;
    }

    .modal-header {
        justify-content: space-evenly;
    }
</style>