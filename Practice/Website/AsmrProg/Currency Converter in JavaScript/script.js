const amount = document.querySelector(".amount input");
const fromCur = document.querySelector(".from select");
const exIcon = document.querySelector(".reverse");
const toCur = document.querySelector(".to select");
const exRateTxt = document.querySelector(".result");
const getBtn = document.querySelector(".convert-box button");

[fromCur, toCur].forEach((select, i) => {
  for (const curCode in Country_List) {
    const selected =
      (i === 0 && curCode === "USD") || (i === 1 && curCode === "GBP")
        ? "selected"
        : "";
    select.insertAdjacentHTML(
      "beforeend",
      `<option value="${curCode}" ${selected}>${curCode}</option>`
    );
  }
  select.addEventListener("change", () => {
    const imgTag = select.parentElement.querySelector("img");
    const code = select.value;
    imgTag.src = `https://flagcdn.com/48x36/${Country_List[
      code
    ].toLowerCase()}.png`;
  });
});

async function getExchangeRate() {
  const amountVal = amount.value || 1;
  exRateTxt.innerText = "Getting exchange rate...";

  try {
    const response = await fetch(
      `https://v6.exchangerate-api.com/v6/ef1e85f5fc05a6536458d968/latest/${fromCur.value}`
    );
    const result = await response.json();
    const exchangeRate = result.conversion_rates[toCur.value];
    const totalExRate = (amountVal * exchangeRate).toFixed(2);
    exRateTxt.innerText = `${amountVal} ${fromCur.value} = ${totalExRate} ${toCur.value}`;
  } catch (error) {
    exRateTxt.innerText = "Something went wrong...";
  }
}
window.addEventListener("load", getExchangeRate);
exIcon.addEventListener("click", () => {
  [fromCur.value, toCur.value] = [toCur.value, fromCur.value];
  [fromCur, toCur].forEach((select) => {
    const imgTag = select.parentElement.querySelector("img");
    const code = select.value;
    imgTag.src = `https://flagcdn.com/48x36/${Country_List[
      code
    ].toLowerCase()}.png`;
  });

  getExchangeRate();
});
getBtn.addEventListener("click", (event) => {
  event.preventDefault();

  getExchangeRate();
});
