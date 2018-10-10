$("#exampleModal").on("show.bs.modal", function(event) {
  var button = $(event.relatedTarget);
  var recipient = button.data("whatever");
});

document.querySelectorAll(".star").forEach(element =>
  element.addEventListener("click", function(event) {
    const id = event.srcElement.id;
    const number = parseInt(id[id.length - 1]);
    for (i = 1; i <= 5; i++) {
      let path = "../icons/";
      path += i <= number ? "star_fill.png" : "star_empty.png";
      const star = document.querySelector(`#star${i}`);
      star.src = path;
      star.classList += i <= number ? "filled" : "empty";
    }
    document.querySelector("#rate").disabled = false;
  })
);

function rateBook() {
  const text = document.querySelector("textarea").value;
  if (getStars()) {
    console.log("error");
  } else {
    alert("success");
  }
}

function getStars() {
  let stars = 0;
  document.querySelectorAll(".star").forEach(function(element) {
    if (element.classList.contains("filled")) {
      stars += 1;
    }
  });
  return stars;
}
