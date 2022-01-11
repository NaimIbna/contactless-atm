<template>
  <div class="container">
    <h1>Scan Your RFID Card</h1>
    <input
      class="my-5 form-control form-control-lg user-input"
      type="text"
      placeholder="RFID No"
      aria-label=""
      v-model="rfid"
      autofocus
    />
    <div class="my-5">
      <button class="mx-2 btn btn-lg btn-primary medium-btn" @click="rfid = ''">
        <img src="/clear.png" class="btn-icon" alt="Fund Transfer" />
        <br />
        Clear
      </button>
      <button
        class="mx-2 btn btn-lg btn-primary medium-btn"
        @click="$emit('rfid-entered')"
      >
        <img src="/right-arrow.png" class="btn-icon" alt="Fund Transfer" />
        <br />
        Next
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rfid: "",
    };
  },
};
</script>

<style>
</style>