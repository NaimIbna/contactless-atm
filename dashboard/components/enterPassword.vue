<template>
  <div class="container">
    <input
      class="my-5 form-control form-control-lg"
      type="password"
      placeholder="PIN No"
      aria-label=""
      v-model="password"
    />
    <div class="mt-5">
      <div class="keyboard">
        <div class="keyboard-row">
          <div class="keyboard-column" @click="pressKey('1')">1</div>
          <div class="keyboard-column" @click="pressKey('2')">2</div>
          <div class="keyboard-column" @click="pressKey('3')">3</div>
        </div>
        <div class="keyboard-row">
          <div class="keyboard-column" @click="pressKey('4')">4</div>
          <div class="keyboard-column" @click="pressKey('5')">5</div>
          <div class="keyboard-column" @click="pressKey('6')">6</div>
        </div>
        <div class="keyboard-row">
          <div class="keyboard-column" @click="pressKey('7')">7</div>
          <div class="keyboard-column" @click="pressKey('8')">8</div>
          <div class="keyboard-column" @click="pressKey('9')">9</div>
        </div>
        <div class="keyboard-row">
          <div class="keyboard-column back-btn" @click="clearVal()">&#8592;</div>
          <div class="keyboard-column" @click="pressKey('0')">0</div>
          <div class="keyboard-column enter-btn" @click="pressEnter()">Enter</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      password: "",
    };
  },
  methods: {
    pressKey(val) {
      console.log(val);
      this.password+=val
    },
    clearVal(){
      if(this.password.length>0)
        this.password = this.password.substr(0, this.password.length - 1)
    },
    pressEnter(){
      console.log(this.password);
      this.$emit('password-entered')
    }
  },
};
</script>

<style scoped>
.keyboard {
  font-weight: 700;
  font-size: 1.3em;
}
.keyboard-row {
  display: flex;
  justify-content: center;
}
.keyboard-column {
  cursor: pointer;
  padding: 14px 70px;
  margin: 5px 20px;
  border: 2px solid #111;
  border-radius: 5px;
}

.back-btn {
  padding: 14px 67px;
}
.enter-btn {
  padding: 14px 52px;
}
</style>