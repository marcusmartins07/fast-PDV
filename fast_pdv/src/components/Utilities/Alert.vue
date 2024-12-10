<template>
  <div class="alerts-container" v-if="alerts.length">
    <div
      v-for="(alert, index) in alerts"
      :key="index"
      :class="`alert alert-${alert.type} alert-dismissible fade show`"
      role="alert"
    >
      {{ alert.message }}
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="closeAlert(index)"></button>
    </div>
  </div>
</template>
  
  <script>
import eventBus from "@/utils/eventBus";

export default {
  name: "Alert",
  data() {
    return {
      alerts: [], 
    };
  },
  created() {
    eventBus.on("show-alert", this.addAlert);
  },
  methods: {
    addAlert(alert) {
      this.alerts.push(alert);

      setTimeout(() => {
        this.alerts.shift();
      }, 5000);
    },
    closeAlert(index) {
      this.alerts.splice(index, 1);
    },
  },
};
</script>
  
  <style scoped>
.alerts-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1050;
  width: 300px;
}

.alert {
  margin-bottom: 10px;
}

.btn-close {
  float: right;
  border: none;
  opacity: 0.6;
}

.btn-close:hover {
  opacity: 1;
}
</style>
  