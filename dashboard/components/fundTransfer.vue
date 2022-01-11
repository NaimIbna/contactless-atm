<template>
  <div class="container my-5">
    <div v-if="step == 1">
      <div class="my-3">
        <h1>Enter your Account Number</h1>
        <input
          class="my-3 form-control form-control-lg user-input"
          type="text"
          placeholder="Account Number"
          aria-label=""
          v-model="accountNumber"
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
              <div class="keyboard-column enter-btn" @click="step = 2">
                Enter
              </div>
            </div>
          </div>
        </div>
      </div>
      <button class="btn btn-lg btn-success medium-btn" @click="reloadPage()">
        Back to home
      </button>
    </div>
    <div v-else-if="step == 2">
      <h1 class="my-3">Enter the amount</h1>
      <input
        class="my-3 form-control form-control-lg user-input"
        type="text"
        placeholder="Amount"
        aria-label=""
        v-model="amount"
      />
      <div class="mt-5">
        <div class="keyboard">
          <div class="keyboard-row">
            <div class="keyboard-column" @click="pressKey('1', '2')">1</div>
            <div class="keyboard-column" @click="pressKey('2', '2')">2</div>
            <div class="keyboard-column" @click="pressKey('3', '2')">3</div>
          </div>
          <div class="keyboard-row">
            <div class="keyboard-column" @click="pressKey('4', '2')">4</div>
            <div class="keyboard-column" @click="pressKey('5', '2')">5</div>
            <div class="keyboard-column" @click="pressKey('6', '2')">6</div>
          </div>
          <div class="keyboard-row">
            <div class="keyboard-column" @click="pressKey('7', '2')">7</div>
            <div class="keyboard-column" @click="pressKey('8', '2')">8</div>
            <div class="keyboard-column" @click="pressKey('9', '2')">9</div>
          </div>
          <div class="keyboard-row">
            <div class="keyboard-column back-btn" @click="clearVal('2')">
              &#8592;
            </div>
            <div class="keyboard-column" @click="pressKey('0', '2')">0</div>
            <div class="keyboard-column enter-btn" @click="transferAmount('3')">
              Enter
            </div>
          </div>
        </div>
      </div>
      <button class="btn btn-lg btn-success medium-btn" @click="reloadPage()">
        Back to home
      </button>
    </div>
    <div v-else-if="step == 3">Processing...</div>
    <div v-else-if="step == 4">
      <h1>Thank You!</h1>
      <button
        class="btn btn-lg btn-success medium-btn my-5"
        @click="reloadPage()"
      >
        Back to home
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pressedButton: "",
      accountNumber: "",
      amount: "",
      step: 1,
      canEnterData: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.canEnterData = true;
    }, 700);
  },
  methods: {
    reloadPage() {
      window.location.reload(true);
    },
    pressKey(val, pad = "1") {
      if (!this.canEnterData) return;

      if (pad == "1") this.accountNumber += val;
      else this.amount += val;

      this.canEnterData = false;
      setTimeout(() => {
        this.canEnterData = true;
      }, 700);
    },
    clearVal(pad = "1") {
      if (!this.canEnterData) return;

      if (pad == "1") {
        if (this.accountNumber.length > 0)
          this.accountNumber = this.accountNumber.substr(
            0,
            this.accountNumber.length - 1
          );
      } else {
        if (this.amount.length > 0)
          this.amount = this.amount.substr(0, this.amount.length - 1);
      }

      this.canEnterData = false;
      setTimeout(() => {
        this.canEnterData = true;
      }, 700);
    },
    transferAmount(val) {
      this.step = val;
      setTimeout(() => {
        this.step = 4;
      }, 3000);
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
  padding: 15px 100px;
  margin: 8px 20px;
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
  padding: 15px 95px;
}
.enter-btn {
  padding: 15px 71px;
}
</style>