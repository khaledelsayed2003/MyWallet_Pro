document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("riveCanvas");
  if (!canvas) return;

  const emailInput = document.getElementById("emailInput");
  const passwordInput = document.getElementById("passwordInput");

  const STATE_MACHINE = "State Machine 1"; 

  const riveInstance = new rive.Rive({
    src: "/static/rive/login_bunny.riv",
    canvas: canvas,
    stateMachines: STATE_MACHINE,  
    autoplay: true,
    onLoad: () => riveInstance.resizeDrawingSurfaceToCanvas(),
  });

  function input(name) {
    const inputs = riveInstance.stateMachineInputs(STATE_MACHINE) || [];
    return inputs.find((i) => i.name === name);
  }

  function setBool(name, value) {
    const i = input(name);
    if (i) i.value = value;
  }

  // ✅ Reaction 1: focus email => bunny focuses
  emailInput.addEventListener("focus", () => {
    setBool("isFocus", true);
    setBool("IsPassword", false);
  });

  emailInput.addEventListener("blur", () => {
    setBool("isFocus", false);
  });

  // ✅ Reaction 2: focus password => bunny closes eyes
  passwordInput.addEventListener("focus", () => {
    setBool("IsPassword", true);
    setBool("isFocus", true);
  });

  passwordInput.addEventListener("blur", () => {
    setBool("IsPassword", false);
    setBool("isFocus", false);
  });

  window.addEventListener("resize", () => {
    riveInstance.resizeDrawingSurfaceToCanvas();
  });
});
