document.addEventListener("DOMContentLoaded", () => {
  const typeSelect = document.getElementById("txType");
  const incomeSelect = document.getElementById("incomeCategory");
  const expenseSelect = document.getElementById("expenseCategory");
  const finalInput = document.getElementById("categoryFinal");

  if (!typeSelect || !incomeSelect || !expenseSelect || !finalInput) return;

  function syncCategory() {
    const isIncome = typeSelect.value === "income";

    incomeSelect.classList.toggle("d-none", !isIncome);
    expenseSelect.classList.toggle("d-none", isIncome);

    const activeSelect = isIncome ? incomeSelect : expenseSelect;
    finalInput.value = activeSelect.value;
  }

  incomeSelect.addEventListener("change", syncCategory);
  expenseSelect.addEventListener("change", syncCategory);
  typeSelect.addEventListener("change", syncCategory);

  // init on load
  syncCategory();
});
