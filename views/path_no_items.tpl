% rebase('layout.tpl', title="Mnemotechnics")








<main role="main" class="flex-shrink-0">
  <div class="container">
    <h1 class="mt-5">Path Items</h1>
    <p class="lead">Add a new item to the Path:</p>

    <form action="/path/{{path_id}}" method="POST">
    <input type="text" size="100" maxlength="100" name="item">
    <input type="submit" value="save">

</form>
  </div>
</main>




