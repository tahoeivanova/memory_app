% rebase('layout.tpl', title="Mnemonistka")

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">


<div style="text-align:center; padding-top: 30px">
    <h1 class="mt-5">Цепочка опорных образов</h1>
    <p class="lead">Вы можете добавить свои образы в цепочку опорных образов.</p>

</div>
<br>


		<div style="text-align:center">
			<ul  style = "list-style-type:none">
		% for item in path:
			<li style="font-size: 24px;">{{item.name}}<a href="/path_item_delete/{{path_id}}/{{item.id}}">Удалить</a> || <a href="/path_item_edit/{{path_id}}/{{item.id}}">Изменить</a></li>

		% end
			</ul>
		</div>
		<br>
		<br>
		<div>
		<p>Добавить образ в цепочку опорных образов:</p>

		<form action="/path/{{path_id}}" method="POST">
			<input type="text" size="50" maxlength="100" name="item">
		    <input type="submit" value="Сохранить название">
		</form>

		</div>


    
  </div>
</main>