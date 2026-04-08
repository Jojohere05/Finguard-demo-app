// DUMMY FRONTEND-ONLY SECRETS FOR FINGUARD DEMO
// These are fake keys and test values, used only
// to exercise FinGuard's secrets + fintech logic.

// These dummy keys are shaped like real Stripe/Razorpay keys so
// FinGuard's secrets agent will detect them, but they are NOT real.
export const STRIPE_PUBLISHABLE_KEY = "pk_live_9xKf3qA7bC2mZp8Lr4Tn6Vy1Ds0Qw";
export const RAZORPAY_KEY_ID = "rzp_live_7HdPq9LmX2vBt5NcR8yKz3Ws";
export const PAYMENT_GATEWAY_API_KEY = "fg_pg_api_key_Z8xC3vB7nM4kL2pQ9rT1";

// Simulated UPI / card test data (non-real)
export const TEST_UPI_VPA = "demo-merchant@upi";
export const TEST_CARD_NUMBER = "4111111111111111"; // test PAN
export const TEST_CARD_EXPIRY = "12/29";
export const TEST_CARD_CVV = "123";

export function initFinPaymentClient() {
  console.log("[FinGuard Demo] Initializing frontend payment client");
  console.log("Using STRIPE_PUBLISHABLE_KEY:", STRIPE_PUBLISHABLE_KEY.slice(0, 10) + "...");
}
