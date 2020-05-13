% rebase('layout.tpl', title="Mnemotechnics")

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
<div style="text-align:center; padding-top: 30px">
    <h1 class="mt-5">Удаление образа</h1>
    <p class="lead">Удалить образ: "{{path_item}}"</p>
</div>



<form action="/path_item_delete/{{path_id}}/{{item_id}}" method="GET">
    <input type="submit" name="delete" value="Удалить">
</form>
</div>


    
  </div>
</main>