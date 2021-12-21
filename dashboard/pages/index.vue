<template>
  <div class="text-center my-5">
    <div v-if="step == 1">
      <h2>Welcome To</h2>
      <h3>Contactless ATM</h3>
      <button @click="step = 2" class="my-5 btn btn-lg btn-primary">
        Start
      </button>
    </div>
    <div v-else-if="step == 2">
      <enter-password v-on:password-entered="step = 3" />
    </div>
    <div v-else-if="step == 3">
      <face-recognition v-on:next-step="step = 4" />
    </div>
    <div v-else-if="step == 4">
      <select-transaction />
    </div>
  </div>
</template>

<script>
import enterPassword from "../components/enterPassword.vue";
export default {
  components: { enterPassword },
  name: "IndexPage",
  data() {
    return {
      step: 1,
    };
  },
};
</script>
