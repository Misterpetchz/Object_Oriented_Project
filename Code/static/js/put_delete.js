function updateItem(name) {
  const book_item = name
  const url = `/add_amount`;
  const data = {name: book_item}
  fetch(url,{
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  window.location.replace("/basket");
}

<script>
        const book_name = {book.name}
</script>

  function updateItem() {
    const book_item = document.getElementById("book_item").value;
    const url = `/add_amount`;
    const data = {name: book_item}
    fetch(url,{
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    window.location.replace("/basket");
  }