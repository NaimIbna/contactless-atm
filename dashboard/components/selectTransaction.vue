<template>
  <div class="container my-5">
    <div v-if="!pressedButton">
      <h2 class="my-5">Select Transaction Type</h2>
      <div class="my-3">
        <button
          class="mx-2 btn btn-lg btn-primary medium-btn"
          @click="pressedButton = 'fund-transfer'"
        >
          <img src="/two-arrows.png" class="btn-icon" alt="Fund Transfer" />
          <br />
          Fund Transfer
        </button>
        <button
          class="mx-2 btn btn-lg btn-primary medium-btn"
          @click="pressedButton = 'cash-withdrawal'"
        >
          <img src="/money-withdrawal.png" class="btn-icon" alt="Cash" /><br />
          Cash Withdrawal
        </button>
      </div>
      <div class="my-3">
        <button
          class="mx-2 btn btn-lg btn-primary medium-btn"
          @click="pressedButton = 'balance-enquiry'"
        >
          <img src="/dollar.png" class="btn-icon" alt="Coin" /> <br />
          Balance Enquiry
        </button>
        <button
          class="mx-2 btn btn-lg btn-primary medium-btn"
          @click="pressedButton = 'mini-statement'"
        >
          <img src="/bank.png" class="btn-icon" alt="MiniStatement" /> <br />
          Mini Statement
        </button>
      </div>
    </div>
    <div v-else-if="pressedButton == 'fund-transfer'">
      <fund-transfer />
    </div>
    <div v-else-if="pressedButton == 'cash-withdrawal'">
      <cash-withdrawal />
    </div>
    <div v-else-if="pressedButton == 'balance-enquiry'">
      <balance-enquiry />
    </div>
    <div v-else-if="pressedButton == 'mini-statement'">
      <mini-statement />
    </div>
  </div>
</template>

<script>
import balanceEnquiry from "./balanceEnquiry.vue";
import CashWithdrawal from "./cashWithdrawal.vue";
import FundTransfer from "./fundTransfer.vue";
import MiniStatement from "./miniStatement.vue";
export default {
  components: { balanceEnquiry, MiniStatement, CashWithdrawal, FundTransfer },
  data() {
    return {
      pressedButton: "",
    };
  },
};
</script>

<style scoped>
.medium-btn {
  font-size: 1.9em;
}
.btn-icon {
  width: 75px;
  height: auto;
  padding: 10px;
}
</style>