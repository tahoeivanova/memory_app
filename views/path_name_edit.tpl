% rebase('layout.tpl', title="Mnemotechnics")

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
<div style="text-align:center; padding-top: 30px">
    <h1 class="mt-5">Изменение названия таблицы</h1>
    <p class="lead">Изменить название цепочки образов: "{{path}}"</p>
</div>



<form action="/path_name_edit/{{path.id}}" method="GET">
    <input type="submit" name="edit" value="Изменить">
</form>
</div>


    
  </div>
</main>