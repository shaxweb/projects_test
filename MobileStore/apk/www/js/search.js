const input = document.querySelector(".search-input");
const resultsDiv = document.querySelector(".products-list");
let preLoaderBox = document.querySelector(".preloader")
preLoaderBox.style.display = "none"
let timeout = null;

input.addEventListener("input", () => {
  preLoaderBox.style.display = "flex"
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    const q = input.value.trim();
    if (!q) {
      preLoaderBox.style.display = "none"
      resultsDiv.innerHTML = "";
      return;
    }
    // encodeURIComponent(q)
    fetch(`https://somestore.onrender.com/search/?q=${q}`)
      .then(response => response.json())
      .then(data => {
        resultsDiv.innerHTML = "";
        if (data.data.length == 0) {
          preLoaderBox.style.display = "none"
          resultsDiv.innerHTML = "<h2>❌ Ничего не найдено</h2>";
          return;
        }
        
        data.data.forEach(product => {
          const div = document.createElement("div");
          div.className = "product-box";
          div.innerHTML = `
              <img src="../img/icons/product.jpg" alt="" onclick="openProduct(${product[0]})">
              <h4 class="product-title" onclick="openProduct(${product[0]})">${product[1]}</h4>
              <div>
                <h5 class="product-price">$${product[3]}</h5>
                <img src="../img/add_basket_white.png" alt="" onclick="addToCard(${product[0]})">
              </div>
              `;
              preLoaderBox.style.display = "none"
          resultsDiv.appendChild(div);
        });
      });
  }, 300); // Задержка 300мс — debounce
});

let addToCard = (id) => {
  let db = localStorage;
  let basket = JSON.parse(db.getItem("basket")) || []
  basket.push(id)
  db.setItem("basket", JSON.stringify(basket))
}
  
let openProduct = (id) => {
  let sdb = sessionStorage;
  sdb.setItem("product_id", id)
  window.location.href = "product_view.html"
}