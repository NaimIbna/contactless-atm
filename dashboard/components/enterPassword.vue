<template>
  <div class="container">
    <h1>Enter your PIN</h1>
    <input
      class="my-5 form-control form-control-lg user-input"
      type="password"
      placeholder="PIN No"
      aria-label=""
      v-model="password"
      autofocus
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
          <div class="keyboard-column back-btn" @click="clearVal()">
            &#8592;
          </div>
          <div class="keyboard-column" @click="pressKey('0')">0</div>
          <div class="keyboard-column enter-btn" @click="pressEnter()">
            Enter
          </div>
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
      canEnterPassword: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.canEnterPassword = true;
    }, 700);
  },
  methods: {
    pressKey(val) {
      if (!this.canEnterPassword) return;

      console.log(val);
      this.password += val;
      this.canEnterPassword = false;
      setTimeout(() => {
        this.canEnterPassword = true;
      }, 700);
    },
    clearVal() {
      if (!this.canEnterPassword) return;
      if (this.password.length > 0)
        this.password = this.password.substr(0, this.password.length - 1);

      this.canEnterPassword = false;
      setTimeout(() => {
        this.canEnterPassword = true;
      }, 700);
    },
    async pressEnter() {
      if (!this.password) return;
      try {
        var res = await this.$axios.$get("http://localhost:5009/api/user/" + this.password);
        if(res=='UserNotFound' || !res.name) return;

        localStorage.setItem("name", res.name);
        localStorage.setItem("balance", res.balance);
        localStorage.setItem("password", res.password);
        localStorage.setItem("uname", res.uname);
        console.log(res);
        this.$emit("password-entered");
      } catch {}
    },
  },
};
</script>

<style scoped>
.keyboard {
  font-weight: 700;
  font-size: 2em;
}
.keyboard-row {
  display: flex;
  justify-content: center;
}
.keyboard-column {
  cursor: pointer;
  padding: 25px 100px;
  margin: 10px 20px;
  border: 2px solid #111;
  border-radius: 5px;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
}

.keyboard-column:hover {
  background-color: #111;
  color: #fff;
}

.back-btn {
  padding: 25px 95px;
}
.enter-btn {
  padding: 25px 71px;
}
</style>