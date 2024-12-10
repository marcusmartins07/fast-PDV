<template>
  <div class="container mt-2">
    <Alert/>
    <Navbar v-if="isAuthenticated" />
    <Login/>
  </div>
</template>

<script>
import Spinner from "../Utilities/Spinner.vue";
import Alert from "../Utilities/Alert.vue";
import eventBus from '@/utils/eventBus';
import Navbar from "@/components/Utilities/Navbar.vue";
import Login from "@/components/Home/Login.vue";
import ConsultaProdutos from '../Utilities/ConsultaProdutos.vue';

export default {
  name: "IniciarVenda",
  components: {
    Spinner,
    Alert,
    Navbar,
    Login,
    ConsultaProdutos,
  },
  data() {
    return {
      isAuthenticated: false,
    };
  },
  mounted() {
    const token = localStorage.getItem("accessToken");
    this.isAuthenticated = !!token; 
  },
};
</script>

<style scoped>
</style>
