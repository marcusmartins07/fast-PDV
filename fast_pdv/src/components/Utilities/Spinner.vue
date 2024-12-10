<template>
    <div class="loader" v-if="isLoading"></div>
</template>

<script>
import eventBus from '@/utils/eventBus';

export default {
    name: "Spinner",
    data() {
        return {
            isLoading: false,
        };
    },
    created() {
        eventBus.on('loading', this.setLoading);
    },
    beforeDestroy() {
        eventBus.off('loading', this.setLoading);
    },
    methods: {
        setLoading(isLoading) {
            this.isLoading = isLoading;
        }
    }
}
</script>

<style scoped>

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.137);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.loading-overlay .spinner-border {
  width: 3rem;
  height: 3rem;
}

.loader{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f7f9fb79;
  transition: opacity 0.75s, visibility 0.75;
}

.loader-hidden{
  opacity: 0;
  visibility: hidden;
}

.loader::after{
  content: "";
  width: 75px;
  height: 75px;
  border: 15px solid #dddddd;
  border-top-color: #7449f5;
  border-radius: 50%;
  animation: loading 0.75s ease infinite;
}

@keyframes loading {
  from{
    transform: rotate(0turn);
  }
  to{
    transform: rotate(1turn)
  }
}

</style>