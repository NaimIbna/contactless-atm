<template>
  <div class="container my-5">
    <button class="btn btn-lg btn-success medium-btn" @click="reloadPage()">
      Back to home
    </button>
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