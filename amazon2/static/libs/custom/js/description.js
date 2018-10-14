$(document).ready(function() {
  const condition = document.getElementById("book-condition").textContent;
  const title = document.querySelector("h3.card-title");
  const badgeContainer = document.createElement("h4");
  badgeContainer.style = "display: inline; margin-left: 7px;";
  badgeContainer.classList = ["align-top"];
  const badge = document.createElement("span");
  badge.classList = ["badge"];
  badgeContainer.appendChild(badge);
  switch(condition) {
    case "new":
      badge.classList.add("badge-primary");
      badge.appendChild(document.createTextNode("New"));
      break;
    case "used":
      badge.classList.add("badge-warning");
      badge.appendChild(document.createTextNode("Used"));
      break;
    case "damaged":
      badge.classList.add("badge-danger");
      badge.appendChild(document.createTextNode("Damaged"));
      break;
  }
  title.appendChild(badgeContainer)
});

// <span class="text-warning">&#9733; &#9733; &#9733; &#9733; &#9734;</span>

$(document).ready(function() {
  const rating = parseInt(document.getElementById("book-rating").textContent);
  const starsStr = document.createTextNode("★ ".repeat(rating) + "☆ ".repeat(5 - rating));
  const starsContainer = document.querySelector(".mt-4 > div.card-body");
  const starsElement = document.createElement("h5");
  starsElement.classList = ["text-warning"];
  starsElement.appendChild(starsStr);
  starsContainer.appendChild(starsElement);
});