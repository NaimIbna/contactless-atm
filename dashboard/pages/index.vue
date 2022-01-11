<template>
  <div class="text-center my-5">
    <div style="position: fixed; right: 20px; top: 20px">
      <button class="btn btn-lg btn-success" @click="reloadPage()">
        <img src="/home.png" class="btn-icon" alt="Home" />
      </button>
    </div>
    <div>
      <div v-if="step == 1">
        <h1 style="margin-top: 100px">Welcome</h1>
        <h2>To</h2>
        <h3>Contactless ATM</h3>
        <button @click="step = 2" class="my-5 btn btn-lg btn-primary large-btn">
          <img src="/power.png" class="btn-icon" alt="Start" /><br />
          Start
        </button>
      </div>
      <div v-else-if="step == 2">
        <rfid-scan v-on:rfid-entered="step = 3" />
      </div>
      <div v-else-if="step == 3">
        <enter-password v-on:password-entered="step = 4" />
      </div>
      <div v-else-if="step == 4">
        <face-recognition v-on:next-step="step = 5" />
      </div>
      <div v-else-if="step == 5">
        <select-transaction />
      </div>
    </div>
  </div>
</template>

<script>
import enterPassword from "../components/enterPassword.vue";
import RfidScan from '../components/rfidScan.vue';
export default {
  components: { enterPassword, RfidScan },
  name: "IndexPage",
  data() {
    return {
      step: 4,
    };
  },
  methods: {
    reloadPage() {
      window.location.reload(true);
    },
  },
};
</script>
<style scoped>
h1 {
  font-size: 3.5em;
  font-weight: 800;
}
.large-btn {
  font-size: 2em;
}
</style>