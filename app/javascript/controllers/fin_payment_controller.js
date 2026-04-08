// DUMMY FRONTEND-ONLY SECRETS FOR FINGUARD DEMO
// These are fake keys and test values, used only
// to exercise FinGuard's secrets + fintech logic.

export const STRIPE_PUBLISHABLE_KEY = "pk_live_FAKE_FRONTEND_KEY_DO_NOT_USE";
export const RAZORPAY_KEY_ID = "rzp_live_FAKE_FRONTEND_KEY_DO_NOT_USE";
export const PAYMENT_GATEWAY_API_KEY = "fg_pg_api_key_1234567890_FAKE";

// Simulated UPI / card test data (non-real)
export const TEST_UPI_VPA = "demo-merchant@upi";
export const TEST_CARD_NUMBER = "4111111111111111"; // test PAN
export const TEST_CARD_EXPIRY = "12/29";
export const TEST_CARD_CVV = "123";

export function initFinPaymentClient() {
  console.log("[FinGuard Demo] Initializing frontend payment client");
  console.log("Using STRIPE_PUBLISHABLE_KEY:", STRIPE_PUBLISHABLE_KEY.slice(0, 10) + "...");
}
