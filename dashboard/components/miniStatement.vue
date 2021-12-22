<template>
  <div class="container my-5">
    <h2>Your Mini-Statement</h2>
    <h3 class="my-3">---</h3>
    <div class="my-5">
      <button class="btn btn-lg btn-success" @click="reloadPage()">
        Back to home
      </button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    reloadPage() {
      window.location.reload(true);
    },
  },
};
</script>

<style>
</style>