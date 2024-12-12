import './assets/css/global.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import VueTheMask from 'vue-the-mask';

const app = createApp(App);

const RequisicaoAutenticada = async (url, options = {}) => {
  const access_token = localStorage.getItem('access_token');
  options.headers = {
    ...options.headers,
    'Content-Type': 'application/json',
    Authorization: `Bearer ${access_token}`,
  };

  const response = await fetch(url, options);

  if (response.status === 401) {
    const refreshResponse = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh: localStorage.getItem('refresh_token') }),
    });

    if (refreshResponse.ok) {
      const newTokens = await refreshResponse.json();
      localStorage.setItem('access_token', newTokens.access);
      options.headers.Authorization = `Bearer ${newTokens.access}`;
      return fetch(url, options);
    }

    if (!refreshResponse.ok) {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
    }

    localStorage.clear();
    router.push({ name: 'Login' });
  }

  return response;
};

const ValidarSenha = async (senha) => {
  try {
    const url = 'http://127.0.0.1:8000/api/v1/usuarios/validar-senha/';
    const options = {
      method: 'POST',
      body: JSON.stringify({ senha }),
    };

    const response = await RequisicaoAutenticada(url, options);

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Erro ao validar senha.');
    }

    const data = await response.json();
    return { success: true, message: data.message };
  } catch (error) {
    console.error('Erro:', error.message);
    return { success: false, message: error.message };
  }
};

app.use(router);
app.use(VueTheMask);
app.config.globalProperties.$RequisicaoAutenticada = RequisicaoAutenticada;
app.config.globalProperties.$ValidarSenha = ValidarSenha;

app.mount('#app');
