const apiUrl = "https://somestore.onrender.com/"

const productsList = document.querySelector(".products-list")
const productBox = document.querySelector(".product-box")

fetch(apiUrl, {method: "GET"})
.then(response => response.json())
.then(data => {
  const results = data.data
  
  for (let i of results) {
    productsList.innerHTML += `
<div class="product-box">
  <img src="../img/icons/product.jpg" alt="">
  <h4 class="product-title">${i[1]}</h4>
  <div>
    <h5 class="product-price">${i[3]}</h5>
    <img src="../img/add_basket_white.png" alt="">
  </div>
</div>
    `
  }
})