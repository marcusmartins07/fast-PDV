<template>
  <div>
    <IniciarVenda />
  </div>
</template>

<script>
  import Spinner from "../components/Utilities/Spinner.vue";
  import Alert from "../components/Utilities/Alert.vue";
  import IniciarVenda from "../components/Home/IniciarVenda.vue";
  
  export default {
    name: "Home",
    components: {
      Spinner,
      Alert,
      IniciarVenda,
    },
    data() {
      return {
        cliente: null, 
        produtos_pedido: [],
      };
    },    
  };
</script>