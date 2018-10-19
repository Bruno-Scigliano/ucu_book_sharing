function search() {
  const filterBy = document.getElementById("search_concept").textContent;
  const searchTerm = document.querySelector("input.form-control").value;
  const Http = new XMLHttpRequest();
  const url = `/search?q=${filterBy}&name=${searchTerm}`;
  Http.open("GET", url);
  Http.send();
  Http.onreadystatechange = e => {
    console.log(Http.responseText);
  };
}
