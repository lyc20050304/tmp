const sideBar = document.querySelector(".sidebar");
const sideLinks = document.querySelectorAll(".side-menu li a:not(.logout)");
const menuBar = document.querySelector(".content nav .bx-menu");
const searchForm = document.querySelector(".content nav form");
const searchBtn = document.querySelector(".form-input button");
const searchBtnIcon = document.querySelector(".form-input button .bx");
const toggler = document.getElementById("theme-toggle");

sideLinks.forEach((item) => {
  const li = item.parentElement;
  item.addEventListener("click", () => {
    sideLinks.forEach((i) => {
      i.parentElement.classList.remove("active");
    });
    li.classList.add("active");
  });
});

window.addEventListener("resize", () => {
  if (window.innerWidth < 768) {
    sideBar.classList.add("close");
  } else {
    sideBar.classList.remove("close");
  }

  if (window.innerWidth > 576) {
    searchForm.classList.remove("show");
    searchBtnIcon.classList.replace("bx-x", "bx-search");
  }
});
menuBar.addEventListener("click", () => {
  sideBar.classList.toggle("close");
});
searchBtn.addEventListener("click", (event) => {
  if (window.innerWidth < 576) {
    event.preventDefault();

    searchForm.classList.toggle("show");
    if (searchForm.classList.contains("show")) {
      searchBtnIcon.classList.replace("bx-search", "bx-x");
    } else {
      searchBtnIcon.classList.replace("bx-x", "bx-search");
    }
  }
});
toggler.addEventListener("change", function () {
  if (this.checked) {
    document.body.classList.add("dark");
  } else {
    document.body.classList.remove("dark");
  }
});
