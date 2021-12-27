<template>
  <div class="container my-5 text-center">
    <h1>Face Recognition</h1>
    <div class="camera-view"></div>
    <button class="btn btn-lg btn-primary medium-btn" @click="$emit('next-step')">Next</button>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.camera-view {
  height: 350px;
  width: 350px;
  border: 1px solid #111;
  margin: 50px auto;
}
</style>