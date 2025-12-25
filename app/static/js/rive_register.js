document.addEventListener("DOMContentLoaded", () => {
  console.log("✅ rive_register.js loaded");

  if (typeof rive === "undefined") {
    console.error("❌ Rive runtime not loaded. Check the <script src='https://unpkg.com/@rive-app/canvas...'> tag");
    return;
  }

  const canvas = document.getElementById("riveCanvas");
  const usernameInput = document.getElementById("usernameInput");
  const emailInput = document.getElementById("emailInput");
  const passwordInput = document.getElementById("passwordInput");

  console.log("canvas:", !!canvas);
  console.log("usernameInput:", !!usernameInput);
  console.log("emailInput:", !!emailInput);
  console.log("passwordInput:", !!passwordInput);

  if (!canvas || !usernameInput || !emailInput || !passwordInput) {
    console.error("❌ Missing elements. Check IDs in register.html match JS.");
    return;
  }

  const STATE_MACHINE = "State Machine 1";

  const riveInstance = new rive.Rive({
    src: "/static/rive/login_bunny.riv",
    canvas,
    stateMachines: STATE_MACHINE,
    autoplay: true,
    onLoad: () => {
      riveInstance.resizeDrawingSurfaceToCanvas();
      const inputs = riveInstance.stateMachineInputs(STATE_MACHINE) || [];
      console.log("✅ Rive loaded. Inputs:", inputs.map(i => ({ name: i.name, type: i.type })));
    },
  });

  function getInput(name) {
    const inputs = riveInstance.stateMachineInputs(STATE_MACHINE) || [];
    return inputs.find((i) => i.name === name);
  }

  function setBool(name, value) {
    const i = getInput(name);
    if (i) i.value = value;
  }

  // Reaction for username/email focus
  function focusText() {
    setBool("isFocus", true);
    setBool("IsPassword", false);
  }

  function blurText() {
    setBool("isFocus", false);
  }

  usernameInput.addEventListener("focus", focusText);
  usernameInput.addEventListener("blur", blurText);

  emailInput.addEventListener("focus", focusText);
  emailInput.addEventListener("blur", blurText);

  // Reaction for password focus
  passwordInput.addEventListener("focus", () => {
    setBool("isFocus", true);
    setBool("IsPassword", true);
  });

  passwordInput.addEventListener("blur", () => {
    setBool("IsPassword", false);
    setBool("isFocus", false);
  });

  window.addEventListener("resize", () => riveInstance.resizeDrawingSurfaceToCanvas());
});

