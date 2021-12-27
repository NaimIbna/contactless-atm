<template>
  <div class="container text-center my-5">
    <div v-if="step == 1">
      <h1>Enter the amount:</h1>
      <input
        class="my-5 form-control form-control-lg user-input"
        type="text"
        placeholder="Enter Amount"
        aria-label=""
        v-model="amount"
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
    <div v-else-if="step == 2">
      <h2>Do you want any printed receipt?</h2>
      <div class="my-5">
        <button class="btn btn-primary btn-lg medium-btn mx-3" @click="printReceipt()">
          Yes
        </button>
        <button class="btn btn-primary btn-lg medium-btn mx-3" @click="printReceipt()">
          No
        </button>
      </div>
    </div>
    <div v-else-if="step == 3">Processing...</div>
    <div v-else-if="step == 4">
      <h1>
        Thank You!
      </h1>
      <button class="btn btn-lg btn-success medium-btn my-5" @click="reloadPage()">
        Back to home
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      amount: "",
      step: 1,
    };
  },
  methods: {
    pressKey(val) {
      console.log(val);
      this.amount += val;
    },
    clearVal() {
      if (this.amount.length > 0)
        this.amount = this.amount.substr(0, this.amount.length - 1);
    },
    pressEnter() {
      console.log(this.amount);
      //this.$emit('password-entered')
      this.step = 2;
    },
    printReceipt() {
      this.step = 3;
      setTimeout(() => {
        this.step = 4;
      }, 3000);
    },
    reloadPage() {
      window.location.reload(true);
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
}

.keyboard-column:hover{
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