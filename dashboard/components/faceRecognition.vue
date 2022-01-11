<template>
  <div class="container my-5 text-center">
    <h1>Face Recognition</h1>
    <div class="camera-view">
      <img src="/face.png" alt="Face" style="width: 100%" />
    </div>
    <div v-if="loading" class="alert alert-primary text-center" role="alert">
      Please wait!
    </div>
    <div
      v-else-if="!loading && !error"
      class="alert alert-success text-center"
      role="alert"
    >
      Success!
    </div>
    <div
      v-else-if="!loading && error"
      class="alert alert-danger text-center"
      role="alert"
    >
      Couldn't recognize!
    </div>

    <button class="btn btn-lg btn-primary medium-btn" @click="nextStep">
      Next
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      error: false,
      intervalRes: null,
    };
  },
  mounted() {
    this.intervalRes = setInterval(() => {
      this.startFaceRecognition();
    }, 2000);
  },
  methods: {
    async startFaceRecognition() {
      try {
        var res = await this.$axios.$get("http://localhost:5009/api/name");
        console.log(res);
        let uname = localStorage.getItem("uname");
        if (res == uname) {
          this.error = false;
        } else {
          this.error = true;
        }
        this.loading = false;
      } catch {}
    },
    nextStep() {
      if (!this.loading && !this.error) {
        clearInterval(this.intervalRes);
        this.$emit("next-step");
      }
    },
  },
};
</script>

<style scoped>
.camera-view {
  height: 350px;
  width: 350px;
  border: 1px solid #111;
  margin: 50px auto;
  margin-bottom: 30px;
}
</style>