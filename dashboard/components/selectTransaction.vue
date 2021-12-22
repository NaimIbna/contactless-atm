<template>
  <div class="container my-5">
    <div v-if="!pressedButton">
      <h2 class="my-5">Select Transaction Type</h2>
      <div class="my-3">
        <button
          class="mx-2 btn btn-lg btn-primary"
          @click="pressedButton = 'fund-transfer'"
        >
          Fund Transfer
        </button>
        <button
          class="mx-2 btn btn-lg btn-primary"
          @click="pressedButton = 'cash-withdrawal'"
        >
          Cash Withdrawal
        </button>
      </div>
      <div class="my-3">
        <button
          class="mx-2 btn btn-lg btn-primary"
          @click="pressedButton = 'balance-enquiry'"
        >
          Balance Enquiry
        </button>
        <button
          class="mx-2 btn btn-lg btn-primary"
          @click="pressedButton = 'mini-statement'"
        >
          Mini Statement
        </button>
      </div>
    </div>
    <div v-else-if="pressedButton == 'fund-transfer'"></div>
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
import MiniStatement from "./miniStatement.vue";
export default {
  components: { balanceEnquiry, MiniStatement, CashWithdrawal },
  data() {
    return {
      pressedButton: "",
    };
  },
};
</script>

<style>
</style>